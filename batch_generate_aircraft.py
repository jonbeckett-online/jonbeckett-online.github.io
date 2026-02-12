#!/usr/bin/env python3
"""
Simple batch processor for aircraft pages - generates basic content for all files quickly.
"""

import os
from pathlib import Path

def parse_filename(filename):
    """Extract developer and aircraft name from filename."""
    # Remove .md extension
    slug = filename.replace('.md', '')
    
    # Split on hyphens
    parts = slug.split('-')
    
    # Find likely developer name (usually first 1-3 words)
    # Common patterns: "developer-aircraft" or "developer-manufacturer-aircraft"
    if len(parts) >= 2:
        # Try to identify where developer ends
        developer_parts = []
        aircraft_parts = []
        
        # Known multi-word developers
        multi_word = {
            'a1r-design-bureau': 3,
            'a2a-simulations': 2,
            'aeroplane-heaven': 2,
            'microsoft-aeroplane-heaven': 3,
            'microsoft-oliver-moser': 3,
            'miltech-blackbird-simulations': 3,
            'miltech-simulations': 2,
            'black-square': 2,
            'big-radials': 2,
            'big-tire-studio': 3,
            'golden-age-simulations': 3,
            'golden-key-studio': 3,
            'flight-replicas': 2,
            'flyingiron-simulations': 2,
            'hype-performance-group': 3,
            'rotor-sim-pilot': 3,
            'sim-skunk-works': 3,
            'erasam-aerosachs': 2,
        }
        
        # Check if starts with known multi-word
        dev_len = 1
        for prefix, length in multi_word.items():
            if slug.startswith(prefix):
                dev_len = length
                break
        
        developer_parts = parts[:dev_len]
        aircraft_parts = parts[dev_len:]
    
    # Format names
    developer = ' '.join(word.capitalize() for word in developer_parts)
    aircraft = ' '.join(word.upper() if len(word) <= 4 and word.isalpha() and word.isupper() 
                       else word.capitalize() 
                       for word in aircraft_parts)
    
    # Handle special cases
    aircraft = aircraft.replace('Msfs', 'MSFS').replace('Crj', 'CRJ').replace('Md-', 'MD-')
    aircraft = aircraft.replace('Dhc', 'DHC').replace('Dh.', 'DH.').replace('Cri Cri', 'Cri-Cri')
    
    developer_slug = '-'.join(developer_parts)
    
    return developer, aircraft, developer_slug

def generate_content(slug, developer, aircraft, developer_slug):
    """Generate basic markdown content."""
    
    title = f"{developer} {aircraft}"
    
    # Generic aircraft image
    generic_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Airplane_silhouette.svg/1200px-Airplane_silhouette.svg.png"
    
    content = f"""---
layout: single
title: "{title}"
permalink: /aircraft/{slug}/
excerpt: "{aircraft} for Microsoft Flight Simulator"
header:
  overlay_image: "{generic_image}"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 100%)"
  teaser: "{generic_image}"
---

# {aircraft}

## The Real Aircraft

The {aircraft} is a notable aircraft in aviation history. This aircraft has been recreated for Microsoft Flight Simulator to allow virtual pilots to experience its unique characteristics and flight dynamics.

**Key Features:**
- Authentic flight dynamics
- Detailed systems modeling
- High-quality 3D modeling
- Comprehensive cockpit simulation

---

## The Simulation

The **{title}** brings this aircraft to Microsoft Flight Simulator with attention to detail and realistic flight characteristics.

**Features:**
- Detailed exterior and interior modeling
- Realistic flight dynamics
- Functional systems and avionics
- Multiple livery options
- Compatible with MSFS 2020/2024

**Developer:** [{developer}](/aircraft-developers/{developer_slug}/)

---

## Developer

For more aircraft from this developer, visit the [{developer}](/aircraft-developers/{developer_slug}/)  developer page.
"""
    
    return content

def main():
    """Process all aircraft files."""
    aircraft_dir = Path("/Users/jonbeckett/Projects/jonbeckett-online.github.io/_pages/resources/aircraft")
    
    # Get all markdown files
    all_files = sorted(aircraft_dir.glob("*.md"))
    
    processed = 0
    skipped = 0
    
    for filepath in all_files:
        # Check if file is essentially empty (< 10 lines means it needs content)
        with open(filepath, 'r', encoding='utf-8') as f:
            line_count = len(f.readlines())
        
        if line_count < 10:
            # Parse filename
            slug = filepath.stem
            developer, aircraft, developer_slug = parse_filename(filepath.name)
            
            # Generate content
            content = generate_content(slug, developer, aircraft, developer_slug)
            
            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            processed += 1
            if processed % 50 == 0:
                print(f"Processed {processed} files...")
        else:
            skipped += 1
    
    print(f"\n{'='*60}")
    print(f"Complete!")
    print(f"  Processed: {processed} files")
    print(f"  Skipped (already complete): {skipped} files")
    print(f"  Total: {len(all_files)} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
