# GitHub Pages Hosting

## Overview

The jonbeckett.com blog is hosted on **GitHub Pages**, GitHub's free static site hosting service that provides automated Jekyll building, global CDN distribution, and seamless integration with Git-based workflows.

## Hosting Architecture

### GitHub Pages Infrastructure
- **Global CDN**: Content delivered from edge locations worldwide
- **Automatic SSL**: HTTPS enforcement with Let's Encrypt certificates  
- **Custom Domain**: jonbeckett.com configured via CNAME file
- **Build System**: Automated Jekyll compilation on every push

### Repository Configuration
- **Repository**: jonbeckett/jonbeckett.github.io
- **Branch**: main (default GitHub Pages branch)
- **Build Source**: Root directory of main branch
- **Custom Domain**: jonbeckett.com (via CNAME file)

## Domain Configuration

### Custom Domain Setup
```
# CNAME file content
jonbeckett.com
```

### DNS Configuration Required
```
# DNS A Records (pointing to GitHub Pages IPs)
jonbeckett.com → 185.199.108.153
jonbeckett.com → 185.199.109.153
jonbeckett.com → 185.199.110.153
jonbeckett.com → 185.199.111.153

# CNAME Record for www subdomain
www.jonbeckett.com → jonbeckett.github.io
```

### HTTPS Configuration
- **SSL Certificate**: Automatically provided by GitHub Pages
- **HTTPS Enforcement**: Enabled in repository settings
- **HTTP Redirects**: Automatic redirect from HTTP to HTTPS

## Deployment Process

### Automated Deployment
1. **Code Push**: Changes pushed to main branch
2. **Build Trigger**: GitHub Pages detects changes automatically
3. **Jekyll Build**: Site compiled using GitHub Pages Jekyll environment
4. **Content Deployment**: Built site deployed to GitHub's CDN
5. **Cache Invalidation**: CDN caches updated globally

### Build Environment
- **Jekyll Version**: Latest supported by github-pages gem
- **Ruby Version**: GitHub Pages default Ruby environment
- **Build Time**: Typically 30-60 seconds for full site rebuild
- **Build Limits**: 10 builds per hour, 100GB bandwidth per month

## GitHub Pages Limitations

### Technical Constraints
- **Plugin Restrictions**: Only whitelisted Jekyll plugins allowed
- **Build Time Limit**: 10 minutes maximum per build
- **File Size Limit**: 100MB maximum per file
- **Repository Size**: 1GB soft limit, 5GB hard limit

### Supported Jekyll Plugins
```yaml
# GitHub Pages whitelisted plugins
plugins:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jekyll-include-cache
  - jekyll-archives
```

## Performance & Availability

### Global CDN Performance
- **Edge Locations**: 200+ locations worldwide
- **Response Time**: Sub-100ms from nearest edge
- **Uptime SLA**: 99.9% availability target
- **Bandwidth**: Unlimited (fair use policy)

### Caching Strategy
- **Static Assets**: Long-term caching (1 year)
- **HTML Content**: Short-term caching (5 minutes)
- **DNS TTL**: 24 hours for A records
- **CDN Purge**: Automatic on content updates

## Monitoring & Analytics

### GitHub Pages Status
- **Build Status**: Visible in repository Actions tab
- **Deploy History**: Complete deployment log available
- **Error Reporting**: Build failures reported via email/GitHub notifications

### Traffic Analytics
- **Google Analytics**: Integrated for visitor tracking
- **GitHub Insights**: Repository traffic and clone statistics
- **Performance Monitoring**: Core Web Vitals via Google Search Console

## Security Features

### GitHub Pages Security
- **DDoS Protection**: Automatic mitigation at CDN level
- **SSL/TLS**: Modern encryption protocols (TLS 1.2+)
- **Security Headers**: Basic security headers included
- **HSTS**: HTTP Strict Transport Security enabled

### Content Security
- **Safe Mode**: Jekyll runs in safe mode (no arbitrary code execution)
- **Dependency Scanning**: GitHub Dependabot for security updates
- **Branch Protection**: Optional branch protection rules

## Backup & Recovery

### Version Control Backup
- **Git History**: Complete change history preserved
- **Repository Cloning**: Full backup via git clone
- **GitHub Archive**: Repository download via GitHub interface

### Content Recovery
- **Commit History**: Point-in-time recovery via Git
- **Build Artifacts**: Previous builds accessible via Pages history
- **External Backups**: Automated backups to external services possible

## Cost Structure

### GitHub Pages Pricing
- **Public Repositories**: Free hosting with unlimited bandwidth
- **Custom Domains**: Free SSL certificates included
- **Build Minutes**: Unlimited for public repositories
- **Storage**: 1GB included, additional storage available

### Third-Party Costs
- **Domain Registration**: Annual domain renewal fees
- **External Analytics**: Google Analytics (free tier)
- **Monitoring Services**: Optional third-party monitoring

## Migration Considerations

### Moving From GitHub Pages
- **Static Export**: Site can be built locally and deployed elsewhere
- **Domain Transfer**: DNS changes required for new hosting
- **SSL Certificates**: New certificates needed for alternative hosting
- **Build Process**: May require custom CI/CD pipeline

### Alternative Hosting Options
- **Netlify**: Enhanced features and build customization
- **Vercel**: Performance optimization and edge functions
- **Cloudflare Pages**: Advanced security and edge computing
- **Self-Hosted**: Complete control with manual management

---

**Hosting Configuration**: GitHub Pages with Custom Domain  
**Primary Domain**: jonbeckett.com  
**Repository**: jonbeckett/jonbeckett.github.io  
**SSL Certificate**: GitHub Pages automatic SSL  
**CDN**: GitHub's global content delivery network