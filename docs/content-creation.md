# Content Creation

## Writing Blog Posts

### Post Creation Process
1. **Create Post File**: Follow Jekyll naming convention `YYYY-MM-DD-post-title.md`
2. **Add Front Matter**: Configure post metadata
3. **Write Content**: Use Markdown with proper structure
4. **Preview Locally**: Test with `bundle exec jekyll serve`
5. **Commit & Push**: Deploy via Git to GitHub Pages

### Post File Naming
```
_posts/YYYY/YYYY-MM-DD-post-title.md
```
- **YYYY**: Four-digit year (also used for subdirectory)
- **MM**: Two-digit month (01-12)
- **DD**: Two-digit day (01-31)
- **post-title**: URL-friendly slug (lowercase, hyphens only)

### Directory Organization
Posts are organized by year in subdirectories:
```
_posts/
├── 2025/          # 2025 posts
├── 2026/          # 2026 posts  
└── YYYY/          # Future years
```

## Front Matter Configuration

### Required Front Matter
```yaml
---
title: "Post Title"
layout: single
date: 2026-02-01
categories:
  - web-development
tags:
  - jekyll
  - blogging
excerpt: "Brief post summary for archives and social sharing"
---
```

### Complete Front Matter Options
```yaml
---
# Required Fields
title: "Complete Post Title"
layout: single
date: 2026-02-01

# Taxonomy
categories:
  - software-development
  - web-development
tags:
  - jekyll
  - ruby
  - github-pages

# Content Description
excerpt: "Post summary that appears in archives and social media"
description: "SEO meta description (if different from excerpt)"

# Table of Contents
toc: true
toc_label: "Contents"
toc_icon: "cog"
toc_sticky: true

# Header Image
header:
  image: /assets/images/banners/post-banner.jpg
  teaser: /assets/images/banners/post-teaser.jpg
  overlay_image: /assets/images/banners/post-overlay.jpg
  overlay_filter: 0.4
  caption: "Photo credit: [Source](https://example.com)"

# Social & SEO
author_profile: true
read_time: true
comments: true
share: false
related: true
show_date: true

# Special Options
published: true          # false for drafts
permalink: /custom/url/  # Custom URL structure
redirect_from:          # URL redirects
  - /old-url/
  - /another-old-url/
---
```

## Content Structure

### Standard Post Structure
```markdown
---
# Front matter here
---

Brief introduction paragraph that hooks the reader and sets context.

## Main Section Heading

Content with proper paragraph breaks and flow.

### Subsection

More detailed content with examples.

## Code Examples

\```language
code block here
\```

## Conclusion

Summary and call to action.
```

### Markdown Best Practices

#### Headings
```markdown
# H1 - Reserved for post title (automatic)
## H2 - Main sections
### H3 - Subsections
#### H4 - Sub-subsections (avoid going deeper)
```

#### Links
```markdown
# Internal links (relative)
[About page](/about/)
[Previous post](/2026/01/27/how-ai-actually-works/)

# External links
[Jekyll Documentation](https://jekyllrb.com/docs/)

# Link with title attribute
[GitHub](https://github.com "GitHub Homepage")
```

#### Images
```markdown
# Simple image
![Alt text](/assets/images/filename.jpg)

# Image with caption (Minimal Mistakes syntax)
![Alt text](/assets/images/filename.jpg){: .align-center}
*Image caption text*

# Responsive image
![Alt text](/assets/images/filename.jpg){: .img-responsive}
```

#### Code Blocks
```markdown
# Inline code
Use the `jekyll serve` command to start the development server.

# Fenced code blocks
\```bash
bundle exec jekyll serve --livereload
\```

# Code with line numbers
\```ruby {linenos=true}
def hello_world
  puts "Hello, World!"
end
\```
```

#### Lists
```markdown
# Unordered lists
- First item
- Second item
  - Nested item
  - Another nested item

# Ordered lists
1. First step
2. Second step
   1. Sub-step
   2. Another sub-step

# Task lists
- [x] Completed task
- [ ] Pending task
```

#### Tables
```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

#### Blockquotes
```markdown
> This is a blockquote.
> It can span multiple lines.
>
> — Author Name
```

## Content Categories & Tags

### Category Guidelines
Categories represent broad subject areas:
```yaml
categories:
  - software-development
  - web-development  
  - productivity
  - technology
  - programming
  - devops
  - testing
```

### Tag Guidelines
Tags are specific topics within categories:
```yaml
tags:
  - jekyll
  - ruby
  - github-pages
  - markdown
  - css
  - javascript
  - automation
  - workflows
```

### Taxonomy Best Practices
- **Categories**: 1-3 per post, broad topics
- **Tags**: 3-8 per post, specific technologies/concepts
- **Consistency**: Use existing categories/tags when possible
- **Lowercase**: Use lowercase with hyphens for multi-word terms

## Static Pages

### Page Creation
```yaml
# _pages/page-name.md
---
title: "Page Title"
permalink: /page-url/
layout: single
author_profile: true
---

Page content here...
```

### Existing Pages
- **About** (`/about/`): Author and site information
- **Posts** (`/posts/`): Complete post archive
- **Categories** (`/categories/`): Category taxonomy
- **Tags** (`/tags/`): Tag taxonomy
- **Disclaimer** (`/disclaimer/`): Legal disclaimer

## Draft Management

### Creating Drafts
```bash
# Option 1: _drafts directory (not currently used)
mkdir _drafts
touch _drafts/draft-post-title.md

# Option 2: Future-dated post
touch _posts/2026/2026-03-01-future-post.md

# Option 3: Unpublished post
# Add to front matter: published: false
```

### Draft Testing
```bash
# Include drafts in build
bundle exec jekyll serve --drafts

# Include future posts
bundle exec jekyll serve --future
```

## Content Review Process

### Pre-Publication Checklist
- [ ] Front matter complete and accurate
- [ ] Title is descriptive and SEO-friendly
- [ ] Categories and tags are appropriate
- [ ] Excerpt summarizes the post effectively
- [ ] Content is well-structured with proper headings
- [ ] Code examples are tested and accurate
- [ ] Links are valid and working
- [ ] Images have alt text
- [ ] Spelling and grammar checked
- [ ] Local preview looks correct

### Quality Guidelines
- **Length**: Aim for 800-2000 words for in-depth posts
- **Structure**: Use clear headings and sections
- **Readability**: Short paragraphs, bullet points, examples
- **Value**: Provide actionable insights or knowledge
- **Originality**: Original content or unique perspectives
- **Updates**: Include publication date and update dates if revised

## SEO Optimization

### Title Optimization
- Keep under 60 characters for search results
- Include primary keyword naturally
- Make it compelling and clickable

### Meta Description (Excerpt)
- 150-160 characters optimal length
- Include primary keyword
- Summarize the post's value proposition

### URL Structure
Jekyll automatically creates URLs from:
```
/YYYY/MM/DD/post-title/
```
This provides good SEO structure with date and descriptive slug.

### Internal Linking
- Link to related posts within content
- Use descriptive anchor text
- Create topic clusters by linking related posts

---

**Content Format**: Markdown with YAML front matter  
**Organization**: Year-based directory structure  
**Publishing**: Git commit and push to deploy  
**Preview**: Local Jekyll development server