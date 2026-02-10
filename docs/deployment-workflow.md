# Deployment Workflow

## Overview

The jonbeckett.com blog uses an automated deployment workflow through GitHub Pages, which builds and deploys the site automatically whenever changes are pushed to the main branch.

## Git-Based Deployment

### Standard Deployment Process
1. **Local Development**: Write and test content locally
2. **Git Commit**: Commit changes to local repository
3. **Git Push**: Push changes to GitHub main branch
4. **Automatic Build**: GitHub Pages triggers Jekyll build
5. **Deployment**: Built site deployed to GitHub's CDN

### Command Sequence
```bash
# 1. Check status and stage changes
git status
git add .

# 2. Commit with descriptive message
git commit -m "Add post: Web request journey"

# 3. Push to GitHub (triggers deployment)
git push origin main

# 4. Monitor deployment status
# Check GitHub repository "Actions" tab
```

## GitHub Pages Build Process

### Build Trigger Events
- **Push to main branch**: Immediate build trigger
- **Manual trigger**: Via GitHub repository settings
- **Schedule**: Not configured (on-demand builds only)

### Build Environment
- **Jekyll Version**: Latest supported by github-pages gem
- **Ruby Version**: GitHub Pages default environment
- **Build Location**: GitHub's servers
- **Build Time**: Typically 30-60 seconds

### Build Steps
1. **Environment Setup**: Initialize build environment
2. **Dependency Installation**: Install gems via Bundler
3. **Content Processing**: Parse Markdown and front matter
4. **Asset Compilation**: Process SCSS to CSS
5. **Site Generation**: Generate static HTML files
6. **HTML Compression**: Minify output (if enabled)
7. **Deployment**: Deploy to CDN edge locations

## Build Status Monitoring

### GitHub Actions Tab
View build status at: `https://github.com/jonbeckett/jonbeckett.github.io/actions`

### Build Status Indicators
- **✅ Green**: Successful build and deployment
- **🟡 Yellow**: Build in progress
- **❌ Red**: Build failed (check logs for errors)

### Build Notifications
- **Email Notifications**: Sent on build failures (if enabled)
- **GitHub Notifications**: In-app notifications for repository watchers
- **Webhook Integration**: Can be configured for external monitoring

## Deployment Verification

### Post-Deployment Checklist
1. **Site Accessibility**: Verify https://jonbeckett.com loads
2. **New Content**: Check new posts appear correctly
3. **Navigation**: Verify menu links work
4. **Feed Updates**: Confirm RSS feed includes new content
5. **Archive Pages**: Check category/tag pages update
6. **Mobile Responsiveness**: Test on mobile devices

### Automated Verification
```bash
# Check site status
curl -I https://jonbeckett.com

# Verify RSS feed
curl -s https://jonbeckett.com/feed.xml | head -20

# Test specific post URL
curl -I https://jonbeckett.com/2026/01/28/web-request-journey/
```

## Branch Management

### Main Branch Protection
- **Direct pushes**: Allowed (no branch protection currently)
- **Pull requests**: Not required for single author
- **Review requirements**: Not configured
- **Status checks**: Basic build status only

### Development Workflow Options

#### Option 1: Direct to Main (Current)
```bash
# Work directly on main branch
git checkout main
git pull origin main
# Make changes
git add .
git commit -m "Update content"
git push origin main
```

#### Option 2: Feature Branch Workflow
```bash
# Create feature branch
git checkout -b feature/new-post
# Make changes
git add .
git commit -m "Add new post"
git push origin feature/new-post
# Create pull request via GitHub interface
# Merge after review
```

## Rollback Procedures

### Quick Rollback via Git
```bash
# Revert to previous commit
git revert HEAD
git push origin main

# Or reset to specific commit (destructive)
git reset --hard [commit-hash]
git push origin main --force
```

### Content-Only Rollback
```bash
# Remove problematic post
git rm _posts/2026/2026-XX-XX-problematic-post.md
git commit -m "Remove problematic post"
git push origin main
```

### Emergency Procedures
1. **Identify Issue**: Determine the problematic commit
2. **Local Fix**: Make corrective changes locally
3. **Emergency Push**: Push fix immediately
4. **Verification**: Confirm site recovery
5. **Post-Mortem**: Document issue and prevention

## Deployment Environments

### Production Environment
- **URL**: https://jonbeckett.com
- **Branch**: main
- **Build**: Automatic on push
- **Environment**: JEKYLL_ENV=production

### Development Environment  
- **URL**: http://127.0.0.1:4000
- **Branch**: Local working directory
- **Build**: Manual `bundle exec jekyll serve`
- **Environment**: JEKYLL_ENV=development

### Staging Environment
Currently not configured. Could be set up using:
- **GitHub Pages**: Additional branch (gh-pages-staging)
- **Netlify**: Deploy previews for pull requests
- **Vercel**: Branch-based preview deployments

## Performance Optimization

### Build Performance
- **Incremental Builds**: Not available on GitHub Pages
- **Build Caching**: Handled automatically by GitHub
- **Asset Optimization**: SCSS compression enabled
- **HTML Minification**: Enabled via compress_html

### Deployment Performance
- **CDN Distribution**: Global edge locations
- **Cache Headers**: Automatic cache control
- **GZIP Compression**: Automatic compression
- **HTTP/2 Support**: Modern protocol support

## Monitoring & Analytics

### Build Monitoring
```bash
# GitHub CLI for build status
gh run list --repo jonbeckett/jonbeckett.github.io

# View specific build details
gh run view [run-id] --repo jonbeckett/jonbeckett.github.io
```

### Site Monitoring
- **Google Analytics**: Traffic and performance monitoring
- **Google Search Console**: SEO and indexing status
- **Uptime Monitoring**: Third-party services (optional)

## Error Handling

### Common Build Errors

#### YAML Front Matter Errors
```yaml
# Invalid YAML (missing quote)
title: This is a "quoted title
# Fix: Properly escape quotes
title: "This is a \"quoted\" title"
```

#### Liquid Template Errors
```liquid
<!-- Invalid liquid syntax -->
{{ site.posts | where: category, "web-development" }}
<!-- Fix: Proper liquid filter syntax -->
{{ site.posts | where: "category", "web-development" }}
```

#### Plugin Errors
```yaml
# Unsupported plugin
plugins:
  - jekyll-unsupported-plugin
# Fix: Use only whitelisted plugins
plugins:
  - jekyll-feed
  - jekyll-sitemap
```

### Error Resolution Process
1. **Check Build Logs**: Review GitHub Actions build output
2. **Identify Error**: Locate specific error message and file
3. **Fix Locally**: Correct the issue in local development
4. **Test Locally**: Verify fix with `bundle exec jekyll build`
5. **Deploy Fix**: Commit and push corrected code

## Backup Strategy

### Git-Based Backup
- **Repository History**: Complete change history in Git
- **GitHub Backup**: Repository hosted on GitHub's infrastructure
- **Local Clones**: Multiple developer machines with full history

### Content Backup
```bash
# Clone repository for backup
git clone https://github.com/jonbeckett/jonbeckett.github.io.git backup/

# Export content only
cp -r _posts/ backup-posts-$(date +%Y%m%d)/
cp -r _pages/ backup-pages-$(date +%Y%m%d)/
```

### Recovery Procedures
1. **Repository Recovery**: Clone from GitHub backup
2. **Content Recovery**: Restore from Git history
3. **Configuration Recovery**: Restore _config.yml from version control
4. **Asset Recovery**: Restore from assets directory backup

---

**Deployment Method**: GitHub Pages automatic builds  
**Trigger**: Push to main branch  
**Build Time**: 30-60 seconds  
**Global Distribution**: GitHub's CDN network  
**Rollback**: Git-based version control