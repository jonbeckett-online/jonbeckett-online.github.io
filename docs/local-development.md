# Local Development

## Prerequisites

### Required Software
- **Ruby 2.7+** - Required for Jekyll
- **RubyGems** - Ruby package manager (included with Ruby)
- **Bundler** - Dependency management for Ruby projects
- **Git** - Version control system

### Installation on macOS
```bash
# Install Ruby via Homebrew (recommended)
brew install ruby

# Add Homebrew Ruby to PATH
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Install Bundler
gem install bundler

# Verify installations
ruby --version
gem --version
bundle --version
```

### Installation on Linux (Ubuntu/Debian)
```bash
# Update package list
sudo apt update

# Install Ruby and development tools
sudo apt install ruby-full build-essential zlib1g-dev

# Configure gem installation directory (avoid sudo)
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Install Bundler
gem install bundler
```

### Installation on Windows
```powershell
# Install Ruby via RubyInstaller
# Download from: https://rubyinstaller.org/
# Choose Ruby+Devkit version

# Verify installation
ruby --version
gem --version

# Install Bundler
gem install bundler
```

## Repository Setup

### Clone Repository
```bash
# Clone the repository
git clone https://github.com/jonbeckett/jonbeckett.github.io.git
cd jonbeckett.github.io

# Or if you have SSH configured
git clone git@github.com:jonbeckett/jonbeckett.github.io.git
cd jonbeckett.github.io
```

### Install Dependencies
```bash
# Install all gem dependencies
bundle install

# Alternative: Install without production gems
bundle install --without production
```

### Dependency Resolution Issues
```bash
# If bundle install fails, try:
bundle update
bundle install

# Clear bundle cache if needed
bundle clean --force
```

## Development Server

### Start Local Server
```bash
# Start Jekyll development server
bundle exec jekyll serve

# With live reload (if supported)
bundle exec jekyll serve --livereload

# On specific port
bundle exec jekyll serve --port 4001

# With drafts included
bundle exec jekyll serve --drafts

# With incremental builds (faster)
bundle exec jekyll serve --incremental
```

### Server Output
```
Configuration file: /path/to/site/_config.yml
            Source: /path/to/site
       Destination: /path/to/site/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
       Jekyll Feed: Generating feed for posts
                    done in 2.134 seconds.
 Auto-regeneration: enabled for '/path/to/site'
    Server address: http://127.0.0.1:4000/
  Server running... press ctrl-c to stop.
```

### Access Local Site
- **Local URL**: http://127.0.0.1:4000/
- **Network URL**: http://[your-ip]:4000/ (for testing on mobile devices)

## Development Workflow

### Content Creation
```bash
# Create new post file
touch _posts/$(date +%Y-%m-%d)-post-title.md

# Or use a script to generate with front matter
cat > _posts/$(date +%Y-%m-%d)-post-title.md << 'EOF'
---
title: "Post Title"
layout: single
date: $(date +%Y-%m-%d)
categories:
  - category
tags:
  - tag1
  - tag2
excerpt: "Post excerpt here"
---

Content here...
EOF
```

### Live Development
1. **Start Development Server**: `bundle exec jekyll serve`
2. **Edit Content**: Modify Markdown files in `_posts/` or `_pages/`
3. **Auto-Regeneration**: Changes automatically trigger rebuilds
4. **Browser Refresh**: Refresh browser to see changes
5. **Configuration Changes**: Require server restart

### Asset Development
```bash
# SCSS files are processed automatically
# Edit assets/css/main.scss or create new SCSS files

# Images can be added to assets/images/
# Reference in posts: ![Alt text](/assets/images/filename.jpg)
```

## Build Commands

### Development Build
```bash
# Build site in development mode
bundle exec jekyll build

# Build with drafts
bundle exec jekyll build --drafts

# Build with future posts
bundle exec jekyll build --future
```

### Production Build
```bash
# Build for production (matches GitHub Pages)
JEKYLL_ENV=production bundle exec jekyll build

# Build with specific destination
bundle exec jekyll build --destination /path/to/output
```

## Testing & Validation

### Local Testing Checklist
- [ ] All pages load without errors
- [ ] Navigation links work correctly
- [ ] Post pagination functions properly
- [ ] Category and tag archives display correctly
- [ ] RSS feed validates (http://127.0.0.1:4000/feed.xml)
- [ ] Images load and display properly
- [ ] Mobile responsiveness works
- [ ] Comments system loads (Giscus)

### HTML Validation
```bash
# Install html-proofer for link checking
gem install html-proofer

# Run after building the site
htmlproofer ./_site --check-html --check-links --assume-extension
```

### Performance Testing
- **Lighthouse**: Chrome DevTools > Lighthouse tab
- **PageSpeed Insights**: Test at https://pagespeed.web.dev/
- **GTmetrix**: Performance analysis at https://gtmetrix.com/

## Debugging Common Issues

### Build Failures
```bash
# Verbose output for debugging
bundle exec jekyll build --verbose

# Check for configuration errors
bundle exec jekyll doctor

# Trace build process
bundle exec jekyll build --trace
```

### Port Conflicts
```bash
# If port 4000 is in use
bundle exec jekyll serve --port 4001

# Find process using port 4000
lsof -i :4000

# Kill process if needed
kill -9 [PID]
```

### Gem Conflicts
```bash
# Update all gems
bundle update

# Check for outdated gems
bundle outdated

# Clean bundle cache
bundle clean
rm -rf vendor/bundle
bundle install
```

### Theme Issues
```bash
# Clear Jekyll cache
rm -rf _site
rm -rf .jekyll-cache
bundle exec jekyll build
```

## Development Environment Variables

### Jekyll Environment
```bash
# Development (default)
JEKYLL_ENV=development bundle exec jekyll serve

# Production (for testing production builds)
JEKYLL_ENV=production bundle exec jekyll build
```

### Custom Environment Variables
```bash
# Set in .env file (if using dotenv gem)
GOOGLE_ANALYTICS_ID=G-0J6K0088RD
SITE_URL=http://127.0.0.1:4000
```

## File Watching Issues

### macOS File Watching
```bash
# Install fswatch for better file watching
brew install fswatch

# Or use polling method
bundle exec jekyll serve --force_polling
```

### Windows File Watching
```bash
# Install wdm gem for Windows directory monitoring
gem install wdm
bundle exec jekyll serve
```

## VS Code Integration

### Recommended Extensions
- **Jekyll Snippets**: Syntax highlighting and snippets
- **YAML**: YAML syntax support for front matter
- **Markdown All in One**: Enhanced Markdown editing
- **Live Server**: Alternative local server for static files

### VS Code Tasks (tasks.json)
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Jekyll Serve",
            "type": "shell",
            "command": "bundle exec jekyll serve",
            "group": "build",
            "isBackground": true
        }
    ]
}
```

---

**Development Server**: Jekyll with Bundler  
**Default Port**: 4000  
**Live Reload**: Automatic file watching  
**Build Time**: ~2-5 seconds for incremental builds