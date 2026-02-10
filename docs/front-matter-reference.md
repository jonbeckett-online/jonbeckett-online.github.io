# Front Matter Reference

## Overview

Front matter is YAML metadata placed at the beginning of Jekyll content files (posts and pages) between triple-dashed lines. It configures how Jekyll processes and displays the content.

## Basic Structure

```yaml
---
# YAML front matter goes here
title: "Post Title"
layout: single
date: 2026-02-01
---

Content starts here after the front matter...
```

## Required Fields

### Essential Front Matter
```yaml
---
title: "Post Title"              # Required: Post/page title
layout: single                   # Required: Layout template
date: 2026-02-01                # Required for posts: Publication date
---
```

### Post-Specific Requirements
```yaml
---
# Posts in _posts/ directory require:
title: "Post Title"
layout: single
date: 2026-02-01
categories:                      # Recommended: Broad topic categories
  - web-development
tags:                           # Recommended: Specific topic tags
  - jekyll
  - blogging
excerpt: "Brief summary"        # Recommended: SEO and archive displays
---
```

## Layout Options

### Available Layouts
```yaml
layout: single                  # Default: Single-column with sidebar
layout: archive                 # Archive page with post listings
layout: home                    # Homepage layout
layout: posts                   # Posts archive
layout: categories              # Category taxonomy
layout: tags                    # Tag taxonomy
layout: collection              # Collection archive
layout: search                  # Search results
```

### Layout-Specific Settings
```yaml
# Single layout options
layout: single
author_profile: true            # Show author sidebar
read_time: true                # Show reading time estimate
comments: true                 # Enable comments
share: false                   # Social sharing buttons
related: true                  # Show related posts
toc: true                      # Table of contents
toc_sticky: true               # Sticky TOC navigation
```

## Content Metadata

### SEO & Social
```yaml
title: "Primary Title"
description: "SEO meta description"    # If different from excerpt
excerpt: "Archive and social summary"  # Used in post lists and social cards
permalink: /custom/url/                # Override default URL structure
canonical_url: https://example.com/    # Canonical URL for duplicate content
```

### Publication Details
```yaml
date: 2026-02-01                       # Publication date (YYYY-MM-DD)
last_modified_at: 2026-02-02          # Last update date
published: true                        # false for drafts
author: "Author Name"                  # Override default author
```

## Taxonomy Classification

### Categories
```yaml
categories:
  - web-development                    # Broad subject areas
  - software-engineering
  - productivity
```

**Category Guidelines:**
- Use 1-3 categories per post
- Represent broad subject areas
- Use lowercase with hyphens
- Create archive pages at `/categories/category-name/`

### Tags
```yaml
tags:
  - jekyll                            # Specific technologies/concepts
  - ruby
  - github-pages
  - markdown
  - blogging
  - automation
```

**Tag Guidelines:**
- Use 3-8 tags per post
- Specific technologies, tools, or concepts
- Lowercase with hyphens for multi-word tags
- Create archive pages at `/tags/tag-name/`

## Visual Elements

### Header Images
```yaml
header:
  image: /assets/images/banners/post-banner.jpg         # Large header image
  teaser: /assets/images/banners/post-teaser-400x200.jpg # Archive thumbnail
  overlay_image: /assets/images/banners/overlay.jpg     # Background image
  overlay_filter: 0.4                                   # Darken overlay (0.0-1.0)
  overlay_color: "#333"                                 # Solid color overlay
  caption: "Photo credit: [Photographer](https://example.com)"
  actions:
    - label: "Learn More"
      url: "https://example.com"
```

### Image Guidelines
- **Header Image**: 1200x400px recommended
- **Teaser Image**: 400x200px for archive displays
- **Overlay Filter**: 0.4 provides good text contrast
- **File Formats**: JPG for photos, PNG for graphics
- **File Size**: Optimize for web (< 200KB recommended)

## Table of Contents

### TOC Configuration
```yaml
toc: true                              # Enable table of contents
toc_label: "Contents"                  # TOC heading text
toc_icon: "cog"                       # Font Awesome icon name
toc_sticky: true                       # Stick TOC to sidebar when scrolling
```

### TOC Behavior
- **Auto-generated**: From H2-H6 headings in content
- **Clickable Links**: Jump to sections
- **Highlight**: Current section highlighted when sticky
- **Mobile**: Collapses appropriately on mobile devices

## Comments & Social

### Comment Configuration
```yaml
comments: true                         # Enable comments (uses site default provider)
# Override comment provider per post:
comments:
  provider: giscus                     # Use specific provider
# Disable comments for specific post:
comments: false
```

### Social Sharing
```yaml
share: true                           # Enable social sharing buttons
# Customize sharing options (if supported by theme):
share:
  twitter: true
  facebook: false
  linkedin: true
```

## Content Display Options

### Reading Features
```yaml
author_profile: true                   # Show author sidebar
read_time: true                       # Show estimated reading time
words_per_minute: 200                 # Override reading speed calculation
show_date: true                       # Show publication date
```

### Related Posts
```yaml
related: true                         # Show related posts at end
# Configure related posts (theme-dependent):
related:
  limit: 4                           # Number of related posts
  threshold: 80                      # Similarity threshold
```

## URL Management

### Custom URLs
```yaml
permalink: /custom/url/               # Override default permalink
# Examples:
permalink: /tutorials/jekyll-guide/
permalink: /:year/:title/
permalink: /:categories/:title/
```

### URL Redirects
```yaml
redirect_from:                        # Redirect old URLs to this post
  - /old-url/
  - /another-old-url/
  - /2025/01/01/old-post-title/
redirect_to: https://example.com      # Redirect this post to external URL
```

## Advanced Options

### Custom Variables
```yaml
# Define custom variables for use in templates
sidebar_image: /assets/images/sidebar.jpg
featured: true
difficulty: intermediate
estimated_time: "30 minutes"
tools_needed:
  - Ruby
  - Git
  - Text editor
```

### Access Custom Variables in Content
```liquid
<!-- In post content or templates -->
{% if page.featured %}
  <div class="featured-badge">Featured Post</div>
{% endif %}

<p>Estimated time: {{ page.estimated_time }}</p>

{% for tool in page.tools_needed %}
  <span class="tool-tag">{{ tool }}</span>
{% endfor %}
```

### Conditional Content
```yaml
# Environment-specific content
development_only: true               # Show only in development
production_only: true               # Show only in production

# Date-based content
expires: 2026-12-31                 # Content expiration date
```

## Validation & Best Practices

### YAML Syntax Rules
```yaml
# Strings with special characters need quotes
title: "Post Title: With Colon"
excerpt: 'Single quotes work too'

# Multi-line strings
description: >
  This is a long description
  that spans multiple lines
  and will be joined with spaces.

# Preserve line breaks
content_note: |
  This content will preserve
  line breaks exactly as written
  in the YAML.

# Lists
categories:
  - web-development
  - programming
# Or inline: categories: [web-development, programming]

# Booleans
published: true                     # not "true"
comments: false                     # not "false"

# Numbers
reading_time: 5                     # not "5"
difficulty_rating: 7.5             # not "7.5"
```

### Common Mistakes
```yaml
# ❌ Incorrect
title: Post Title: With Colon        # Unquoted colon causes error
date: February 1, 2026               # Invalid date format
published: "true"                    # String instead of boolean

# ✅ Correct  
title: "Post Title: With Colon"      # Quoted string
date: 2026-02-01                     # ISO date format
published: true                      # Boolean value
```

### Validation Tools
```bash
# Validate YAML syntax locally
ruby -e "require 'yaml'; YAML.load_file('_posts/2026-02-01-post.md')"

# Jekyll doctor command
bundle exec jekyll doctor

# Build site to check for errors
bundle exec jekyll build --verbose
```

---

**Format**: YAML between `---` markers  
**Required Fields**: title, layout, date (for posts)  
**Encoding**: UTF-8  
**Syntax**: YAML 1.1 specification