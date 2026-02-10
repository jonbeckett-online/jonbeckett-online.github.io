# GitHub Copilot Instructions for jonbeckett.com

This is a personal flight simulation blog focusing on flight simulation, and aviation. The site is built with Jekyll and uses the Minimal Mistakes theme, hosted on GitHub Pages.

## Project Overview

**Author**: Jonathan Beckett  
**Tech Stack**: Jekyll, Minimal Mistakes theme, GitHub Pages  
**Content Focus**: Flight simulation, aviation
**Deployment**: Automated via GitHub Actions to GitHub Pages

## Specialized Skills

This project uses a modular skill-based approach for different aspects of blog management. Each skill contains detailed instructions for specific areas:

### 📝 [Blog Post Creation](skills/blog-post-creation.md)
- File naming conventions and organization
- Front matter template and configuration
- Category and tag management
- SEO optimization

### ✍️ [Writing Style Guidelines](skills/writing-style-guidelines.md)
- Voice, tone, and narrative approach
- Content structure and depth requirements
- Technical writing standards
- Common writing patterns and examples

### 🇬🇧 [British English Standards](skills/british-english-standards.md)
- Required British spelling conventions
- Common mistakes to avoid
- Verification checklist and quality control

### 🖼️ [Image Management](skills/image-management.md)
- Unsplash integration and photo ID extraction
- Image sizing and URL configuration
- Attribution requirements and quality standards

### ⚙️ [Jekyll Technical Setup](skills/jekyll-technical-setup.md)
- Local development commands
- Configuration and deployment
- Archive system requirements (GitHub Pages limitations)

### ✅ [Quality Control](skills/quality-control.md)
- Pre-publication checklist
- Common mistakes and best practices
- Review process and continuous improvement

## Quick Reference

### Essential File Pattern
```
_posts/YYYY/YYYY-MM-DD-slug-title.md
```

### Core Front Matter
```yaml
---
title: "Main Title: Subtitle"
layout: single
date: YYYY-MM-DD
categories: [primary-category]
tags: [tag1, tag2, tag3]
excerpt: "Compelling one-sentence description"
header:
  overlay_image: "https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  teaser: "https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
---
```

### Critical Reminders
- **British English spellings exclusively** (organise, colour, centre)
- **Target length**: 2,000-5,000+ words
- **Content structure**: Hook → History → Technical → Applications → Future
- **Archive type**: Must use `liquid` not `jekyll-archives` (GitHub Pages limitation)

## Author Expertise Context

Jonathan Beckett is a flight simulation content creator with extensive experience in aviation and flight simulation. He has a deep understanding of the technical aspects of flight simulation software, hardware, and the aviation industry. His writing style is engaging, informative, and accessible, aiming to educate and inspire both novice and experienced flight sim enthusiasts.

Draw from these areas when suggesting content or code examples while maintaining the established writing style.
