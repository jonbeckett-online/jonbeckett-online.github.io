# Jekyll Configuration

## Core Configuration (_config.yml)

The Jekyll configuration file defines all site-wide settings, theme configuration, and build parameters for the blog.

## Site Settings

### Basic Site Information
```yaml
# Site Identity
title: jonbeckett.com
title_separator: "-"
name: "Jonathan Beckett"
description: "Software and Web Developer"
url: "https://jonbeckett.com"
baseurl: ""
repository: "jonbeckett/jonbeckett.github.io"

# Localization
locale: "en-US"
timezone: # Uses system timezone (GMT/BST for UK)
words_per_minute: 200
```

### Theme Configuration
```yaml
# Remote Theme Setup
remote_theme: mmistakes/minimal-mistakes
minimal_mistakes_skin: "default"

# Navigation & Structure
breadcrumbs: true
masthead_title: # Uses site title by default
logo: # No custom logo configured
teaser: # No default teaser image
```

## Content Processing

### Markdown Configuration
```yaml
# Markdown Processing
markdown: kramdown
highlighter: rouge
excerpt_separator: "\n\n"

# Kramdown Settings
kramdown:
  input: GFM                    # GitHub Flavored Markdown
  hard_wrap: false
  auto_ids: true               # Automatic heading IDs
  footnote_nr: 1
  entity_output: as_char
  toc_levels: 1..6
  smart_quotes: lsquo,rsquo,ldquo,rdquo
  enable_coderay: false
```

### File Handling
```yaml
# File Processing
include:
  - .htaccess
  - _pages
keep_files:
  - .git
  - .svn
encoding: "utf-8"
markdown_ext: "markdown,mkdown,mkdn,mkd,md"
```

## Site Structure & URLs

### Permalink Structure
```yaml
# URL Structure
permalink: /:year/:month/:day/:title/
# Example: /2026/01/28/web-request-journey/
```

### Pagination
```yaml
# Post Pagination
paginate: 10
paginate_path: /page:num/
# Creates: /page1/, /page2/, etc.
```

### Archives & Taxonomies
```yaml
# Category Archives
category_archive:
  type: liquid                 # GitHub Pages compatible
  path: /categories/

# Tag Archives  
tag_archive:
  type: liquid                 # GitHub Pages compatible
  path: /tags/
```

## Author Configuration

### Author Profile
```yaml
author:
  name: "Jonathan Beckett"
  avatar: "/assets/images/jonbeckett.jpg"
  bio: "Software and Web Developer"
  location: "UK"
  email: "jonathan.beckett@gmail.com"
  
  # Social Links
  links:
    - label: "LinkedIn"
      icon: "fab fa-fw fa-linkedin"
      url: "https://linkedin.com/in/jonathanbeckett"
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/jonbeckett"
    - label: "BlueSky"
      icon: "fab fa-fw fa-bluesky"
      url: "https://bsky.app/profile/jonbeckett.bsky.social"
```

## Comments & Engagement

### Giscus Comments Configuration
```yaml
comments:
  provider: false # Disabled by default, enabled per post
  giscus:
    repo_id: "R_kgDOQxyHhg"
    category_name: "General"
    category_id: "DIC_kwDOQxyHhs4C03Y9"
    discussion_term: "pathname"
    reactions_enabled: '1'
    theme: "light"
```

## Analytics & Tracking

### Google Analytics 4
```yaml
analytics:
  provider: "google-gtag"
  google:
    tracking_id: "G-0J6K0088RD"
    anonymize_ip: false
```

## Jekyll Plugins

### Plugin Configuration
```yaml
plugins:
  - jekyll-paginate          # Post pagination
  - jekyll-sitemap           # XML sitemap generation
  - jekyll-gist              # GitHub Gist embedding
  - jekyll-feed              # RSS/Atom feeds
  - jekyll-include-cache     # Performance optimization
  - jekyll-archives          # Archive generation

# GitHub Pages Whitelist (safety)
whitelist:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jekyll-include-cache
  - jekyll-archives
```

### Feed Configuration
```yaml
atom_feed:
  path: # Uses default feed.xml
  hide: false
  excerpt_only: false        # Show full content in feeds
```

## Default Layout Configuration

### Post Defaults
```yaml
defaults:
  # All Posts
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: true           # Giscus comments enabled
      share: false            # Social sharing disabled
      related: true           # Related posts shown
      show_date: true
      toc: false             # Table of contents per post
      toc_label: "Table of Contents"
      toc_icon: "cog"
      toc_sticky: false
```

### Page Defaults  
```yaml
  # Static Pages
  - scope:
      path: "_pages"
      type: pages
    values:
      layout: single
      author_profile: true
```

## Styling & Assets

### SCSS Configuration
```yaml
sass:
  sass_dir: _sass
  style: compressed          # Minified CSS output
```

### Footer Configuration
```yaml
footer:
  links:
    - label: "Email"
      icon: "fas fa-fw fa-envelope-square"
      url: "mailto:jonathan.beckett@gmail.com"
    - label: "LinkedIn"  
      icon: "fab fa-fw fa-linkedin"
      url: "https://linkedin.com/in/jonathanbeckett"
    - label: "GitHub"
      icon: "fab fa-fw fa-github" 
      url: "https://github.com/jonbeckett"
    - label: "BlueSky"
      icon: "fab fa-fw fa-bluesky"
      url: "https://bsky.app/profile/jonbeckett.bsky.social"
    - label: "Disclaimer"
      icon: "fas fa-fw fa-info-circle"
      url: "/disclaimer/"
```

## Performance Optimization

### HTML Compression
```yaml
compress_html:
  clippings: all
  ignore:
    envs: development        # No compression in dev mode
```

### Build Optimization
```yaml
# Performance Settings
lsi: false                   # Latent Semantic Indexing disabled
incremental: false           # Full rebuilds for consistency
```

## Excluded Files

### Build Exclusions
```yaml
exclude:
  - .sass-cache/
  - .jekyll-cache/
  - gemfiles/
  - Gemfile
  - Gemfile.lock
  - node_modules/
  - vendor/bundle/
  - vendor/cache/
  - vendor/gems/
  - vendor/ruby/
  - README.md
  - agent.md
```

## Search Configuration

```yaml
# Site Search (disabled)
search: false                # No built-in search functionality
```

## Security Settings

### ReCaptcha (Not Configured)
```yaml
reCaptcha:
  siteKey:                   # Not configured
  secret:                    # Not configured
```

---

**Configuration File**: `_config.yml`  
**Jekyll Version**: 4.x (via github-pages gem)  
**Theme**: Minimal Mistakes (remote)  
**Last Updated**: February 1, 2026