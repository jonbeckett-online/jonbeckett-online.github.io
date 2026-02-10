# File Structure

## Repository Organization

The blog follows Jekyll's standard directory structure with Minimal Mistakes theme conventions and GitHub Pages compatibility.

```
jonbeckett.github.io/
├── _config.yml                 # Jekyll configuration
├── _data/                      # YAML data files
│   └── navigation.yml          # Site navigation menu
├── _includes/                  # Reusable template components
│   ├── breadcrumbs.html        # Breadcrumb navigation
│   └── head/
│       └── custom.html         # Custom head elements
├── _pages/                     # Static pages
│   ├── about.md               # About page
│   ├── categories.md          # Categories archive
│   ├── disclaimer.md          # Legal disclaimer
│   ├── posts.md              # Posts archive
│   └── tags.md               # Tags archive
├── _posts/                     # Blog posts (organized by year)
│   ├── 2025/                  # 2025 posts
│   └── 2026/                  # 2026 posts
├── _site/                      # Generated site (excluded from repo)
├── assets/                     # Static assets
│   ├── css/
│   │   └── main.scss          # Main stylesheet
│   └── images/                # Image assets
│       └── banners/           # Banner images
├── docs/                       # Technical documentation
├── CNAME                       # Custom domain configuration
├── Gemfile                     # Ruby dependencies
├── index.html                  # Homepage template
└── README.md                   # Repository documentation
```

## Core Configuration Files

### Jekyll Configuration
- **_config.yml** - Main Jekyll configuration file
  - Site metadata and settings
  - Theme configuration (Minimal Mistakes)
  - Plugin configuration
  - Default layouts and values
  - Analytics and comments setup

### Ruby Dependencies
- **Gemfile** - Ruby gem dependencies
  - github-pages gem (includes Jekyll)
  - jekyll-feed plugin
  - Platform-specific dependencies
- **Gemfile.lock** - Locked dependency versions (auto-generated)

### Domain Configuration
- **CNAME** - Custom domain configuration for GitHub Pages
  - Contains: `jonbeckett.com`

## Content Organization

### Posts Directory Structure
```
_posts/
├── 2025/                       # Year-based organization
│   ├── 2025-01-05-linux-history-evolution.md
│   ├── 2025-05-01-note-taking.md
│   ├── 2025-06-01-getting-things-done.md
│   └── ...
└── 2026/                       # Current year posts
    ├── 2026-01-02-flexible-bdd-solutions.md
    ├── 2026-01-03-ai-note-taking-revolution.md
    └── ...
```

### Post Naming Convention
```
YYYY-MM-DD-post-title.md
```
- **YYYY**: Four-digit year
- **MM**: Two-digit month
- **DD**: Two-digit day  
- **post-title**: Hyphen-separated slug
- **.md**: Markdown file extension

### Static Pages
```
_pages/
├── about.md                    # Author and site information
├── categories.md               # Category taxonomy page
├── disclaimer.md               # Legal disclaimer
├── posts.md                   # All posts archive
└── tags.md                    # Tag taxonomy page
```

## Template Structure

### Data Files
```
_data/
└── navigation.yml              # Site navigation configuration
```

**Navigation Structure:**
```yaml
main:
  - title: "About"
    url: /about/
  - title: "Posts"  
    url: /posts/
  - title: "Categories"
    url: /categories/
  - title: "Tags"
    url: /tags/
```

### Include Files
```
_includes/
├── breadcrumbs.html           # Custom breadcrumb navigation
└── head/
    └── custom.html            # Custom HTML head elements
```

## Asset Organization

### Stylesheets
```
assets/
└── css/
    └── main.scss              # Main stylesheet entry point
```

**SCSS Structure:**
```scss
---
# Front matter required for Jekyll processing
---

@charset "utf-8";

@import "minimal-mistakes/skins/{{ site.minimal_mistakes_skin | default: 'default' }}";
@import "minimal-mistakes";
```

### Images
```
assets/
└── images/
    ├── banners/               # Banner images for posts
    │   └── README.txt         # Banner usage documentation
    └── jonbeckett.jpg         # Author profile image
```

## Generated Content

### Build Output
- **_site/** - Generated static site (excluded from repository)
  - Complete HTML/CSS/JS output
  - Processed by Jekyll during build
  - Deployed to GitHub Pages automatically

### Cache Directories (Excluded)
- **.sass-cache/** - SCSS compilation cache
- **.jekyll-cache/** - Jekyll build cache
- **node_modules/** - Node.js dependencies (if used)
- **vendor/** - Bundler vendor directory

## Documentation Structure

### Technical Documentation
```
docs/                           # Comprehensive technical docs
├── README.md                   # Documentation index
├── technology-stack.md         # Technologies overview
├── github-pages-hosting.md     # Hosting configuration
├── jekyll-configuration.md     # Jekyll setup details
├── file-structure.md          # This file
└── ...                        # Additional documentation files
```

## File Permissions & Ownership

### Jekyll Processing
- **Processed Files**: Markdown files with front matter
- **Static Files**: Assets copied directly to _site/
- **Excluded Files**: Listed in _config.yml exclude section

### Front Matter Requirements
```yaml
---
# Minimal front matter for Jekyll processing
# Required for .md files in _posts/ and _pages/
---
```

## Backup & Version Control

### Git Tracking
- **Tracked**: All source files and content
- **Ignored**: Generated files and caches
  - _site/
  - .sass-cache/
  - .jekyll-cache/
  - Gemfile.lock (platform-specific)
  - vendor/

### .gitignore Pattern
```gitignore
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata
vendor/
node_modules/
.DS_Store
```

## File Size Considerations

### GitHub Pages Limits
- **Single File**: 100MB maximum
- **Repository Size**: 1GB soft limit
- **Build Time**: 10 minutes maximum

### Optimization Strategies
- **Image Compression**: Optimize images before upload
- **Asset Minification**: SCSS compiled to compressed CSS
- **HTML Compression**: Enabled via compress_html setting

## Access Patterns

### URL Structure
```
https://jonbeckett.com/
├── /                          # Homepage (index.html)
├── /about/                    # About page (_pages/about.md)
├── /posts/                    # Posts archive (_pages/posts.md)
├── /categories/               # Categories page (_pages/categories.md)
├── /tags/                     # Tags page (_pages/tags.md)
├── /disclaimer/               # Disclaimer (_pages/disclaimer.md)
├── /YYYY/MM/DD/post-title/    # Individual posts
├── /categories/category-name/ # Category archives
└── /tags/tag-name/           # Tag archives
```

### Asset URLs
```
https://jonbeckett.com/assets/
├── /css/main.css             # Compiled stylesheet
└── /images/                  # Image assets
```

---

**Directory Structure**: Standard Jekyll with Minimal Mistakes theme  
**Content Organization**: Year-based post organization  
**Asset Management**: SCSS preprocessing with compression  
**Version Control**: Git with appropriate .gitignore patterns