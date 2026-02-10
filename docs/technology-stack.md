# Technology Stack

## Core Technologies

### Static Site Generator
- **Jekyll 4.x** - Ruby-based static site generator
- **GitHub Pages compatibility** - Uses github-pages gem for deployment
- **Liquid templating engine** - For dynamic content generation
- **Kramdown** - Markdown processor with GFM (GitHub Flavored Markdown) support

### Programming Languages & Markup
- **Ruby** - Jekyll's underlying language
- **HTML5** - Semantic markup structure
- **SCSS/Sass** - CSS preprocessing for styling
- **YAML** - Configuration and front matter data
- **Markdown** - Content authoring format
- **Liquid** - Template language for dynamic content

### Frontend Framework & Theme
- **Minimal Mistakes** - Remote Jekyll theme
  - Version: Latest stable from mmistakes/minimal-mistakes
  - Skin: Default theme variant
  - Responsive design with mobile optimization
  - Built-in SEO optimization
  - Social media integration
  - Archive and taxonomy support

### Build & Deployment Platform
- **GitHub Pages** - Automated Jekyll building and hosting
- **GitHub Actions** - Automated deployment pipeline
- **Git version control** - Source code management

## Dependencies & Gems

### Core Jekyll Dependencies (via github-pages gem)
```ruby
# Primary dependency that includes Jekyll and GitHub Pages compatible gems
gem "github-pages", group: :jekyll_plugins
```

### Jekyll Plugins
- **jekyll-feed** (~> 0.12) - RSS/Atom feed generation
- **jekyll-paginate** - Post pagination support
- **jekyll-sitemap** - XML sitemap generation
- **jekyll-gist** - GitHub Gist embedding
- **jekyll-include-cache** - Performance optimization for includes
- **jekyll-archives** - Category and tag archive generation

### Platform-Specific Dependencies
- **tzinfo** - Timezone information (Windows/JRuby)
- **tzinfo-data** - Timezone data files
- **wdm** - Windows directory monitoring for file watching
- **http_parser.rb** - HTTP parsing for JRuby compatibility

## Third-Party Services

### Analytics
- **Google Analytics 4** (G-0J6K0088RD)
- **Google Tag Manager** integration
- Anonymous IP tracking disabled for privacy

### Comments System
- **Giscus** - GitHub Discussions-powered commenting
  - Repository: Connected to GitHub repository discussions
  - Theme: Light theme matching site design
  - Reactions enabled for user engagement

### Content Delivery
- **GitHub's CDN** - Asset delivery and caching
- **Font Awesome** - Icon library (via theme)

## Development Tools

### Version Control
- **Git** - Source code versioning
- **GitHub** - Repository hosting and collaboration

### Package Management
- **Bundler** - Ruby gem dependency management
- **RubyGems** - Ruby package repository

### Local Development
- **Ruby 2.7+** - Required Ruby version
- **Jekyll serve** - Local development server
- **Bundle exec** - Isolated gem environment execution

## Browser Compatibility

### Modern Browser Support
- Chrome 70+
- Firefox 65+
- Safari 12+
- Edge 79+

### Mobile Compatibility
- iOS Safari 12+
- Chrome Mobile 70+
- Android Browser 8+

## Performance Features

### Optimization
- **HTML compression** - Automated minification
- **SCSS compilation** - Compressed CSS output
- **Image optimization** - Responsive image handling
- **Caching headers** - Browser caching optimization

### SEO Features
- **Structured data** - JSON-LD markup for search engines
- **Open Graph** - Social media sharing optimization
- **Twitter Cards** - Enhanced Twitter link previews
- **Canonical URLs** - Duplicate content prevention
- **XML sitemaps** - Search engine crawling support

## Security Considerations

### Content Security
- **GitHub Pages security** - Automated security updates
- **HTTPS enforcement** - SSL/TLS encryption for all traffic
- **Safe gem whitelist** - Only approved Jekyll plugins

### Privacy Features
- **IP anonymization** - Google Analytics privacy setting
- **No third-party tracking** - Minimal external dependencies
- **GDPR considerations** - Privacy-focused analytics setup

---

**Technology Stack Version**: February 1, 2026  
**Jekyll Version**: 4.x (via github-pages gem)  
**Ruby Version**: 2.7+ required  
**Theme Version**: mmistakes/minimal-mistakes (remote)