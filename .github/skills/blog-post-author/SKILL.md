---
name: Blog Post Creation
description: Complete creation of new blog posts for jonbeckett.com, including file naming conventions, front matter templates, and initial structure setup
---

# Blog Post Creation Skill

This skill handles the complete creation of new blog posts for jonbeckett.com, including file naming, front matter, and initial structure.

## File Naming Convention

All blog posts must follow this exact naming pattern:
```
_posts/YYYY/YYYY-MM-DD-slug-title.md
```

- Posts are organized by year in subdirectories under `_posts/`
- Date format: `YYYY-MM-DD` (e.g., `2026-01-13`)
- Slug: lowercase with hyphens, descriptive and SEO-friendly
- Extension: `.md` (Markdown)

**Examples**:
- `_posts/2026/2026-01-13-kubernetes-evolution.md`
- `_posts/2026/2026-01-14-testing-strategies-modern-web.md`

## Front Matter Template

Every blog post MUST start with YAML front matter using this exact structure:

```yaml
---
title: "Main Title: Subtitle for Context"
layout: single
date: YYYY-MM-DD
categories:
  - primary-category
  - secondary-category
tags:
  - tag1
  - tag2
  - tag3
excerpt: "A compelling one-sentence description that appears in post previews and social media shares. Should be engaging and informative."
header:
  overlay_image: "https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Photographer Name](https://unsplash.com/@photographer) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
---
```

## Front Matter Guidelines

- **title**: Use quotation marks, can include colons and subtitles
- **layout**: Always `single` for blog posts
- **date**: Format as `YYYY-MM-DD` (must match filename date)
- **categories**: 1-3 categories, lowercase with hyphens
- **tags**: 3-6 relevant tags, lowercase with hyphens
- **excerpt**: Single sentence, 120-200 characters, compelling summary
- **header images**: Use Unsplash images with proper attribution
  - overlay_image: 1200x400px for desktop headers
  - teaser: 600x300px for thumbnails and archive listings
  - Always include photographer credit in caption
  - Both overlay_image and teaser use same photo ID with different dimensions

## Common Categories

- artificial-intelligence
- enterprise
- software-development
- productivity
- web-development
- cloud-computing
- devops
- testing
- automation

## Creating New Posts Workflow

### Step-by-Step Process

1. **Create file structure**:
   - Create file in `_posts/YYYY/` following naming convention
   - Ensure filename matches: `YYYY-MM-DD-slug-title.md`

2. **Add complete front matter**:
   - Copy template and customize all fields
   - Ensure date matches filename date
   - Choose 1-3 relevant categories from common list
   - Select 3-6 descriptive tags
   - Write compelling 120-200 character excerpt

3. **Configure images** (see [Image Management skill](image-management.md)):
   - Find suitable Unsplash image
   - Extract correct photo ID from page source  
   - Test both header (1200x400) and teaser (600x300) URLs
   - Get photographer name and username for attribution
   - Verify images display correctly

4. **Write content following style guidelines**:
   - Start with engaging hook/scenario
   - Include historical context and evolution
   - Provide technical depth with code examples
   - Add practical applications and use cases
   - Conclude with future implications
   - Use British English spelling throughout

5. **Pre-publication validation**:
   - Test locally with `bundle exec jekyll serve`
   - Verify images load correctly
   - Check for YAML syntax errors
   - Validate British English spelling
   - Review content structure and flow
   - Complete quality control checklist

6. **Commit and deploy**:
   - Git add, commit with descriptive message
   - Push to trigger automatic deployment
   - Monitor for build success

## Content Creation Guidelines Summary

### Target Specifications
- **Length**: 2,000-5,000+ words for comprehensive coverage
- **Structure**: Hook → History → Technical → Applications → Future
- **Language**: British English spelling exclusively
- **Tone**: Professional but accessible, narrative-driven with technical depth

### Required Elements
- **Opening hook**: Compelling scenario or observation
- **Historical context**: Evolution and background of the topic
- **Technical explanations**: Detailed analysis with code/architecture examples
- **Practical applications**: Real-world implications and use cases  
- **Future outlook**: Forward-looking analysis and predictions
- **Code examples**: Proper syntax highlighting and context

### Content Patterns
Refer to [Writing Style Guidelines](writing-style-guidelines.md) for:
- Detailed voice and tone standards
- Stylistic patterns and examples
- Markdown formatting requirements
- Author expertise context

## SEO Best Practices

- Write descriptive, keyword-rich titles
- Create compelling excerpts (shown in search results)
- Use relevant categories and tags
- Include meta descriptions via excerpt
- Use descriptive file names (slug becomes URL)
- Ensure headers create logical hierarchy