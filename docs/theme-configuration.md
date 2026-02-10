# Theme Configuration

## Minimal Mistakes Theme

### Theme Setup
The blog uses the **Minimal Mistakes** Jekyll theme configured as a remote theme, which provides automatic updates and reduced repository size.

```yaml
# _config.yml theme configuration
remote_theme: mmistakes/minimal-mistakes
minimal_mistakes_skin: "default"
```

### Theme Benefits
- **Responsive Design**: Mobile-first approach with excellent cross-device compatibility
- **SEO Optimization**: Built-in structured data and meta tags
- **Social Integration**: Author profiles and social media links
- **Archive Support**: Category and tag taxonomy pages
- **Comment System**: Multiple comment providers supported
- **Performance**: Optimized CSS and JavaScript

## Theme Customization

### Skin Selection
Available skins in Minimal Mistakes:
```yaml
minimal_mistakes_skin: "default"    # Current selection
# Options: "air", "aqua", "contrast", "dark", 
#          "dirt", "neon", "mint", "plum", "sunrise"
```

### Layout Options
The theme provides several layout types:
- **single**: Default for posts and pages
- **archive**: For category/tag pages
- **home**: Homepage layout
- **posts**: Posts archive layout
- **categories**: Category archive layout
- **tags**: Tag archive layout
- **collection**: For collections
- **search**: Search results layout

### Color Scheme (Default Skin)
```scss
// Default skin variables
$background-color: #fff
$text-color: #222831
$primary-color: #7c4dff
$border-color: mix(#fff, #222831, 75%)
$footer-background-color: mix(#000, $background-color, 10%)
$link-color: #0366d6
$masthead-link-color: $text-color
$masthead-link-color-hover: mix(#000, $text-color, 20%)
$navicon-link-color-hover: mix(#fff, $text-color, 80%)
```

## Custom Styling

### Main Stylesheet Structure
```scss
// assets/css/main.scss
---
---

@charset "utf-8";

@import "minimal-mistakes/skins/{{ site.minimal_mistakes_skin | default: 'default' }}";
@import "minimal-mistakes";

// Custom overrides would go here
```

### Custom CSS Additions
To add custom styling, append to `assets/css/main.scss`:
```scss
// Custom styles
.custom-class {
  // Custom styling here
}

// Override theme variables
$primary-color: #your-color !default;

// Import theme after variable overrides
@import "minimal-mistakes";
```

### Font Customization
```scss
// Custom font imports
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

// Override theme font variables
$serif: "Inter", serif;
$sans-serif: "Inter", sans-serif;
$monospace: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
```

## Layout Configuration

### Site Header (Masthead)
```yaml
# _config.yml masthead settings
title: jonbeckett.com           # Site title in header
masthead_title:                 # Override title (empty = use title)
logo:                          # Logo image path (not configured)
```

### Navigation Menu
```yaml
# _data/navigation.yml
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

### Author Profile Sidebar
```yaml
# _config.yml author settings
author:
  name: "Jonathan Beckett"
  avatar: "/assets/images/jonbeckett.jpg"
  bio: "Software and Web Developer"
  location: "UK"
  email: "jonathan.beckett@gmail.com"
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

### Footer Configuration
```yaml
# _config.yml footer settings
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

## Page Layout Defaults

### Post Layout Configuration
```yaml
# _config.yml defaults for posts
defaults:
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: true      # Show author sidebar
      read_time: true          # Show estimated reading time
      comments: true           # Enable comments (Giscus)
      share: false            # Disable social sharing buttons
      related: true           # Show related posts
      show_date: true         # Show publication date
      toc: false             # Table of contents (per-post)
      toc_label: "Table of Contents"
      toc_icon: "cog"
      toc_sticky: false
```

### Page Layout Configuration
```yaml
# _config.yml defaults for pages
defaults:
  - scope:
      path: "_pages"
      type: pages
    values:
      layout: single
      author_profile: true
```

## Feature Configuration

### Archive Pages
```yaml
# _config.yml archive settings
category_archive:
  type: liquid              # GitHub Pages compatible
  path: /categories/
tag_archive:
  type: liquid              # GitHub Pages compatible
  path: /tags/
```

### Breadcrumb Navigation
```yaml
# _config.yml breadcrumb settings
breadcrumbs: true           # Enable breadcrumb navigation
```

Custom breadcrumb template at `_includes/breadcrumbs.html` provides enhanced navigation.

### Search Functionality
```yaml
# _config.yml search settings
search: false               # Disabled (no search provider configured)
```

### Pagination
```yaml
# _config.yml pagination settings
paginate: 10                # Posts per page
paginate_path: /page:num/   # Pagination URL structure
```

## Social Integration

### Social Sharing
```yaml
# Disabled in post defaults
share: false                # No social sharing buttons
```

### Open Graph Configuration
The theme automatically generates Open Graph tags from:
- Post title
- Post excerpt  
- Author information
- Site configuration

### Twitter Cards
Automatic Twitter Card generation using:
- Site title and description
- Author Twitter handle (if configured)
- Post excerpts and images

## Responsive Design

### Breakpoints
The theme uses these responsive breakpoints:
```scss
$small: 600px !default;
$medium: 768px !default;
$medium-wide: 900px !default;
$large: 1024px !default;
$x-large: 1280px !default;
$max-width: $x-large !default;
```

### Mobile Optimization
- **Mobile-first CSS**: Progressive enhancement approach
- **Touch-friendly**: Appropriate touch target sizes
- **Fast Loading**: Optimized assets and minimal dependencies
- **Readable Typography**: Responsive font scaling

## Asset Management

### Image Handling
```yaml
# Example post header image configuration
header:
  image: /assets/images/banners/post-banner.jpg
  teaser: /assets/images/banners/post-teaser.jpg
  overlay_image: /assets/images/banners/post-overlay.jpg
  overlay_filter: 0.4
  caption: "Photo credit: [Source](https://example.com)"
```

### Icon Integration
- **Font Awesome**: Integrated icon library
- **Social Icons**: Automatic icon selection for social links
- **Custom Icons**: Support for custom icon classes

## Performance Optimization

### CSS Optimization
```yaml
# _config.yml SCSS settings
sass:
  sass_dir: _sass
  style: compressed         # Minified CSS output
```

### HTML Compression
```yaml
# _config.yml HTML compression
compress_html:
  clippings: all
  ignore:
    envs: development       # Only compress in production
```

### Asset Loading
- **Critical CSS**: Above-the-fold CSS inlined
- **Non-blocking JS**: JavaScript loaded asynchronously
- **Web Fonts**: Optimized font loading strategies

---

**Theme**: Minimal Mistakes (Remote)  
**Skin**: Default  
**Customization**: CSS overrides in main.scss  
**Layout**: Single-column with sidebar  
**Responsive**: Mobile-first design