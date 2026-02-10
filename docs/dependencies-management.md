# Dependencies Management

## Ruby Gems Overview

The blog's dependencies are managed through **Bundler** and defined in the `Gemfile`. This ensures consistent gem versions across development and production environments.

## Gemfile Structure

### Primary Dependencies
```ruby
source "https://rubygems.org"

# GitHub Pages gem includes Jekyll and compatible plugins
gem "github-pages", group: :jekyll_plugins

# Additional Jekyll plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end
```

### Platform-Specific Dependencies
```ruby
# Windows and JRuby timezone support
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Windows file watching performance
gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]

# JRuby HTTP parser compatibility
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
```

## GitHub Pages Gem

### What's Included
The `github-pages` gem is a meta-gem that includes:
- **Jekyll**: Static site generator
- **Jekyll plugins**: GitHub Pages whitelisted plugins
- **Dependencies**: All required supporting gems
- **Version matching**: Exactly matches GitHub Pages environment

### Included Plugins
```ruby
# Automatically included with github-pages gem:
- jekyll-coffeescript
- jekyll-commonmark-ghpages
- jekyll-default-layout
- jekyll-gist
- jekyll-github-metadata
- jekyll-optional-front-matter
- jekyll-paginate
- jekyll-readme-index
- jekyll-redirect-from
- jekyll-relative-links
- jekyll-remote-theme
- jekyll-sass-converter
- jekyll-seo-tag
- jekyll-sitemap
- jekyll-swiss
- jekyll-theme-architect
- jekyll-theme-cayman
- jekyll-theme-dinky
- jekyll-theme-hacker
- jekyll-theme-leap-day
- jekyll-theme-merlot
- jekyll-theme-midnight
- jekyll-theme-minimal
- jekyll-theme-modernist
- jekyll-theme-primer
- jekyll-theme-slate
- jekyll-theme-tactile
- jekyll-theme-time-machine
- jekyll-titles-from-headings
- jemoji
- kramdown-parser-gfm
- liquid
- mercenary
- minima
- nokogiri
- rouge
- ruby
- safe_yaml
```

## Dependency Management Commands

### Install Dependencies
```bash
# Install all gems from Gemfile
bundle install

# Install without production dependencies (if applicable)
bundle install --without production

# Install to specific path
bundle install --path vendor/bundle
```

### Update Dependencies
```bash
# Update all gems to latest compatible versions
bundle update

# Update specific gem
bundle update jekyll-feed

# Update github-pages gem
bundle update github-pages

# Show outdated gems
bundle outdated
```

### Version Management
```bash
# Show current gem versions
bundle list

# Show dependency tree
bundle viz

# Check for security issues
bundle audit

# Clean unused gems
bundle clean
```

## Version Constraints

### GitHub Pages Compatibility
```ruby
# Use exact versions to match GitHub Pages
gem "github-pages", "~> 228", group: :jekyll_plugins

# Or use latest version (automatic updates)
gem "github-pages", group: :jekyll_plugins
```

### Plugin Version Constraints
```ruby
# Specific version
gem "jekyll-feed", "0.15.1"

# Compatible version range
gem "jekyll-feed", "~> 0.12"

# Minimum version
gem "jekyll-feed", ">= 0.12"
```

## Lock File Management

### Gemfile.lock Purpose
- **Exact Versions**: Records exact gem versions used
- **Reproducible Builds**: Ensures consistent dependencies
- **Nested Dependencies**: Tracks all transitive dependencies
- **Platform Specific**: Different locks for different platforms

### Lock File Operations
```bash
# Generate new lock file
bundle install

# Update lock file
bundle update

# Remove lock file (regenerates on next install)
rm Gemfile.lock
bundle install
```

### Version Control
```bash
# Commit lock file for reproducible builds
git add Gemfile.lock
git commit -m "Update dependencies"

# Or ignore lock file for flexible versions (not recommended)
echo "Gemfile.lock" >> .gitignore
```

## Development vs Production

### Environment-Specific Gems
```ruby
# Development only gems
group :development do
  gem "html-proofer"  # HTML validation
  gem "jekyll-admin"  # Admin interface
end

# Test gems
group :test do
  gem "rspec"
  gem "capybara"
end

# Jekyll plugins (loaded in all environments)
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-sitemap"
end
```

### Bundle Installation Flags
```bash
# Skip development and test groups
bundle install --without development test

# Only install specific groups
bundle install --with development

# Skip optional dependencies
bundle install --without optional
```

## Troubleshooting Dependencies

### Common Issues

#### Gem Version Conflicts
```bash
# Error: conflicting gem versions
bundle update
bundle install

# Nuclear option: clear everything
rm -rf vendor/bundle
rm Gemfile.lock
bundle install
```

#### Platform-Specific Issues
```bash
# macOS ARM (M1/M2) issues
bundle config set --local force_ruby_platform true
bundle install

# Windows issues
gem install wdm
bundle install
```

#### Build Tool Dependencies
```bash
# Ubuntu/Debian
sudo apt-get install build-essential zlib1g-dev

# macOS
xcode-select --install

# Install Ruby development headers
sudo apt-get install ruby-dev  # Ubuntu
brew install ruby              # macOS
```

### Dependency Resolution
```bash
# Check for dependency conflicts
bundle check

# Resolve conflicts interactively
bundle install --verbose

# Force specific gem version
bundle update gem_name --conservative
```

## Security Management

### Security Audits
```bash
# Install bundler-audit
gem install bundler-audit

# Check for vulnerabilities
bundle audit check

# Update vulnerability database
bundle audit update
```

### Automated Security Updates

#### Dependabot Configuration
Create `.github/dependabot.yml`:
```yaml
version: 2
updates:
  - package-ecosystem: "bundler"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
```

#### GitHub Security Alerts
- **Automatic Detection**: GitHub scans for vulnerabilities
- **Pull Request Creation**: Automated security update PRs
- **Notification System**: Email alerts for security issues

## Performance Optimization

### Bundle Configuration
```bash
# Configure bundle for performance
bundle config set --local path 'vendor/bundle'
bundle config set --local clean true
bundle config set --local without 'development test'

# Parallel installation
bundle config set --local jobs 4
```

### Gem Installation Optimization
```bash
# Skip documentation installation
bundle config set --local no-document true

# Use system gems when possible
bundle config set --local disable_shared_gems false
```

## CI/CD Integration

### GitHub Actions Integration
```yaml
# .github/workflows/build.yml
name: Build and Deploy
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: 2.7
          bundler-cache: true  # Automatically runs bundle install
      
      - name: Build site
        run: bundle exec jekyll build
```

### Caching Dependencies
```yaml
# Cache bundler gems
- name: Cache gems
  uses: actions/cache@v2
  with:
    path: vendor/bundle
    key: ${{ runner.os }}-gems-${{ hashFiles('**/Gemfile.lock') }}
    restore-keys: |
      ${{ runner.os }}-gems-
```

## Alternative Dependency Managers

### RubyGems Direct
```bash
# Install gems directly (not recommended)
gem install jekyll
gem install github-pages
```

### Docker Approach
```dockerfile
# Dockerfile for consistent environment
FROM ruby:2.7

WORKDIR /site
COPY Gemfile* ./
RUN bundle install

COPY . .
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
```

```bash
# Build and run with Docker
docker build -t jekyll-blog .
docker run -p 4000:4000 jekyll-blog
```

---

**Dependency Manager**: Bundler  
**Primary Gem**: github-pages (meta-gem)  
**Lock File**: Gemfile.lock (tracked in Git)  
**Security**: Bundler-audit and Dependabot  
**Platform Support**: Cross-platform compatibility