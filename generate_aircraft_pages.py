#!/usr/bin/env python3
"""
Script to generate aircraft pages for Microsoft Flight Simulator aircraft.
Parses filenames to generate structured content with Wiki attribution.
"""

import os
import re
from pathlib import Path
import glob

# Developer mapping (filename prefix to developer name and slug)
DEVELOPER_MAP = {
    "4simmers": ("4Simmers", "4simmers"),
    "a1r-design-bureau": ("A1R Design Bureau", "a1r-design-bureau"),
    "a2a-simulations": ("A2A Simulations", "a2a-simulations"),
    "aerial-simulations": ("Aerial Simulations", "aerial-simulations"),
    "aero-dynamics": ("Aero Dynamics", "aero-dynamics"),
    "aeroplane-heaven": ("Aeroplane Heaven", "aeroplane-heaven"),
    "aeroplane-heaven-microsoft": ("Aeroplane Heaven/Microsoft", "aeroplane-heaven"),
    "aerosachs": ("AeroSachs", "aerosachs"),
    "aerosoft": ("Aerosoft", "aerosoft"),
    "airfoillabs": ("Airfoil Labs", "airfoillabs"),
    "ants-airplanes": ("Ant's Airplanes", "ants-airplanes"),
    "arie-baba": ("Arie Baba", "arie-baba"),
    "asobo": ("Asobo Studio", "asobo-studio"),
    "asobo-microsoft": ("Asobo Studio/Microsoft", "asobo-studio"),
    "asobo-working-title": ("Asobo Studio/Working Title", "asobo-studio"),
    "atsimulations": ("ATSimulations", "atsimulations"),
    "azurpoly": ("AzurPoly", "azurpoly"),
    "big-radials": ("Big Radials", "big-radials"),
    "big-tire-studio": ("Big Tire Studio", "big-tire-studio"),
    "black-square": ("Black Square", "black-square"),
    "blackbird-simulations": ("Blackbird Simulations", "blackbird-simulations"),
    "blackbox-simulations": ("Blackbox Simulations", "blackbox-simulations"),
    "bluemesh": ("BlueMesh", "bluemesh"),
    "bluemesh-microsoft": ("BlueMesh/Microsoft", "bluemesh"),
    "bravoairspace": ("BravoAirspace", "bravoairspace"),
    "bredok3d": ("Bredok3D", "bredok3d"),
    "brsim-designs": ("BRSim Designs", "brsim-designs"),
    "brsimdesigns": ("BRSim Designs", "brsim-designs"),
    "captain-sim": ("Captain Sim", "captain-sim"),
    "carenado": ("Carenado", "carenado"),
    "carenado-microsoft": ("Carenado/Microsoft", "carenado"),
    "cera-sim": ("Cera Sim", "cera-sim"),
    "cj-simulations": ("CJ Simulations", "cj-simulations"),
    "classic-aircraft-simulations": ("Classic Aircraft Simulations", "classic-aircraft-simulations"),
    "classic-simulations": ("Classic Simulations", "classic-simulations"),
    "cowan-simulation": ("Cowan Simulation", "cowan-simulation"),
    "cows": ("Cows", "cows"),
    "dc-designs": ("DC Designs", "dc-designs"),
    "deimos": ("Deimos", "deimos"),
    "erasam-aerosachs": ("Erasam AeroSachs", "aerosachs"),
    "flight-replicas": ("Flight Replicas", "flight-replicas"),
    "flight-sim-labs": ("Flight Sim Labs", "flight-sim-labs"),
    "flightfx": ("FlightFX", "flightfx"),
    "flightsim-studio": ("FlightSim Studio", "flightsim-studio"),
    "flyboy-simulations": ("Flyboy Simulations", "flyboy-simulations"),
    "flybywire": ("FlyByWire", "flybywire"),
    "flyingiron-simulations": ("FlyingIron Simulations", "flyingiron-simulations"),
    "flyinside": ("FlyInside", "flyinside"),
    "flyndive": ("Flyndive", "flyndive"),
    "flysimware": ("Flysimware", "flysimware"),
    "flying-fries": ("Flying Fries", "flying-fries"),
    "fsreborn": ("FSReborn", "fsreborn"),
    "gks": ("GKS", "gks"),
    "golden-age-simulations": ("Golden Age Simulations", "golden-age-simulations"),
    "golden-key-studio": ("Golden Key Studio", "golden-key-studio"),
    "got-friends": ("Got Friends", "got-friends"),
    "hans-hartmann": ("Hans Hartmann", "hans-hartmann"),
    "hcg-digital-arts": ("HCG Digital Arts", "hcg-digital-arts"),
    "heaven-designs": ("Heaven Designs", "heaven-designs"),
    "horizon-simulations": ("Horizon Simulations", "horizon-simulations"),
    "hype-performance-group": ("Hype Performance Group", "hype-performance-group"),
    "indiafoxtecho": ("IndiaFoxtEcho", "indiafoxtecho"),
    "inibuilds": ("iniBuilds", "inibuilds"),
    "just-flight": ("Just Flight", "just-flight"),
    "kwikflight": ("KwikFlight", "kwikflight"),
    "latinvfr": ("LatinVFR", "latinvfr"),
    "lionheart-creations": ("Lionheart Creations", "lionheart-creations"),
    "livtoair": ("LivToAir", "livtoair"),
    "marwan-gharib": ("Marwan Gharib", "marwan-gharib"),
    "microsoft": ("Microsoft", "microsoft"),
    "microsoft-aeroplane-heaven": ("Microsoft/Aeroplane Heaven", "aeroplane-heaven"),
    "microsoft-oliver-moser": ("Microsoft/Oliver Moser", "oliver-moser"),
    "miltech-blackbird-simulations": ("Miltech/Blackbird Simulations", "miltech-simulations"),
    "miltech-simulations": ("Miltech Simulations", "miltech-simulations"),
    "mscenery": ("MScenery", "mscenery"),
    "nemeth-designs": ("Nemeth Designs", "nemeth-designs"),
    "oby1-eurofly": ("OBY1 Eurofly", "oby1-eurofly"),
    "orbx": ("Orbx", "orbx"),
    "pilot-experience-sim": ("Pilot Experience Sim", "pilot-experience-sim"),
    "pilots": ("Pilots", "pilots"),
    "pixel-planes": ("Pixel Planes", "pixel-planes"),
    "pmdg": ("PMDG", "pmdg"),
    "prestige-simulations": ("Prestige Simulations", "prestige-simulations"),
    "project-stratosphere": ("Project Stratosphere", "project-stratosphere"),
    "propair-flights": ("Propair Flights", "propair-flights"),
    "rara-avis-sims": ("Rara Avis Sims", "rara-avis-sims"),
    "redwing-simulations": ("Redwing Simulations", "redwing-simulations"),
    "restauravia": ("Restauravia", "restauravia"),
    "rhdsimulations": ("RHDSimulations", "rhdsimulations"),
    "rotor-sim-pilot": ("Rotor Sim Pilot", "rotor-sim-pilot"),
    "sc-designs": ("SC Designs", "sc-designs"),
    "shrike-simulations": ("Shrike Simulations", "shrike-simulations"),
    "sim-federation": ("Sim Federation", "sim-federation"),
    "sim-skunk-works": ("Sim Skunk Works", "sim-skunk-works"),
    "simsolutions": ("SimSolutions", "simsolutions"),
    "simworks-studios": ("SimWorks Studios", "simworks-studios"),
    "sky-simulations": ("Sky Simulations", "sky-simulations"),
    "swissmilsim": ("SwissMilSim", "swissmilsim"),
    "tangogolf": ("TangoGolf", "tangogolf"),
    "taogs-hangar": ("TaoGS Hangar", "taogs-hangar"),
    "tfdi-design": ("TFDI Design", "tfdi-design"),
    "top-mach-studios": ("Top Mach Studios", "top-mach-studios"),
    "touching-cloud": ("Touching Cloud", "touching-cloud"),
    "tukanflightsim": ("TukanFlightSim", "tukanflightsim"),
    "vflyteairs": ("VFlyteAirs", "vflyteairs"),
    "virtavia": ("Virtavia", "virtavia"),
    "virtualcol": ("VirtualCol", "virtualcol"),
    "vrilleplat": ("Vrilleplat", "vrilleplat"),
    "working-title": ("Working Title", "working-title"),
    "xtreme-prototypes": ("Xtreme Prototypes", "xtreme-prototypes"),
    "ysim": ("YSim", "ysim"),
}

# Specific aircraft data overrides with Wikimedia images
AIRCRAFT_SPECIFIC_DATA = {
    # Aeroplane Heaven / Microsoft
    "aeroplane-heaven-microsoft-curtiss-c-46-commando": {
        "title": "Aeroplane Heaven/Microsoft Curtiss C-46 Commando",
        "aircraft_name": "Curtiss C-46 Commando",
        "developer": "Aeroplane Heaven",
        "developer_slug": "aeroplane-heaven",
        "excerpt": "The legendary twin-engine cargo transport of World War II.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Curtiss_C-46A_Commando_USAF.jpg",
        "teaser": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Curtiss_C-46A_Commando_USAF.jpg/600px-Curtiss_C-46A_Commando_USAF.jpg",
        "manufacturer": "Curtiss-Wright",
        "first_flight": "March 26, 1940",
        "introduction": "1941",
        "type": "Twin-engine military transport",
        "description": "The Curtiss C-46 Commando was a military transport aircraft derived from the commercial CW-20 pressurized airliner design. Known as 'The Whale' due to its large fuselage, it served as a capable cargo transport during WWII, particularly famous for flying 'The Hump' over the Himalayas between India and China. With a larger cargo capacity than the C-47, it was particularly effective in high-altitude operations.",
        "specs": {
            "Length": "23.3 m (76 ft 4 in)",
            "Wingspan": "32.9 m (108 ft)",
            "Range": "4,750 km (2,950 mi)",
            "Cruise Speed": "278 km/h (173 mph)",
            "Engines": "2× Pratt & Whitney R-2800",
        },
        "sim_features": [
            "Detailed exterior and interior modeling",
            "Authentic flight dynamics",
            "Period-appropriate liveries",
            "Functional cargo compartment",
            "Compatible with MSFS 2020/2024"
        ]
    },
    
    "aeroplane-heaven-microsoft-douglas-c-47d-skytrain-waco-cg-4a": {
        "title": "Aeroplane Heaven/Microsoft Douglas C-47D Skytrain & Waco CG-4A",
        "aircraft_name": "Douglas C-47 Skytrain & Waco CG-4A Glider",
        "developer": "Aeroplane Heaven",
        "developer_slug": "aeroplane-heaven",
        "excerpt": "The iconic WWII transport and its accompanying combat glider.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/C-47_Skytrain_2.jpg",
        "teaser": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/C-47_Skytrain_2.jpg/600px-C-47_Skytrain_2.jpg",
        "manufacturer": "Douglas Aircraft Company",
        "first_flight": "December 23, 1941",
        "introduction": "1942",
        "type": "Military transport aircraft",
        "description": "The Douglas C-47 Skytrain, military version of the legendary DC-3, was the definitive military transport aircraft of WWII. Nicknamed 'Gooney Bird,' it dropped paratroopers, towed gliders, flew cargo over the Hump, and participated in every major Allied operation. This package includes both the C-47D and the Waco CG-4A combat glider that it towed into battle.",
        "specs": {
            "Length": "19.4 m (63 ft 9 in)",
            "Wingspan": "29.1 m (95 ft 6 in)",
            "Range": "2,600 km (1,600 mi)",
            "Cruise Speed": "269 km/h (167 mph)",
            "Engines": "2× Pratt & Whitney R-1830",
        },
        "sim_features": [
            "Both C-47D and Waco CG-4A glider included",
            "Authentic WWII liveries (D-Day, Market Garden)",
            "Functional tow cable system",
            "Detailed cockpit and cargo area",
            "Period-specific instruments",
            "Compatible with MSFS 2020/2024"
        ]
    },
    
    "aeroplane-heaven-microsoft-ford-trimotor": {
        "title": "Aeroplane Heaven/Microsoft Ford Trimotor",
        "aircraft_name": "Ford Trimotor",
        "developer": "Aeroplane Heaven",
        "developer_slug": "aeroplane-heaven",
        "excerpt": "The 'Tin Goose' - an American aviation icon from the golden age of aviation.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Ford_Tri-Motor_N414H.jpg",
        "teaser": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Ford_Tri-Motor_N414H.jpg/600px-Ford_Tri-Motor_N414H.jpg",
        "manufacturer": "Ford Motor Company",
        "first_flight": "June 11, 1926",
        "introduction": "1926",
        "type": "Three-engine transport",
        "description": "The Ford Trimotor, affectionately known as the 'Tin Goose,' was one of America's first all-metal airliners. Produced by Ford Motor Company from 1926 to 1933, it helped establish airline service across the United States. The distinctive corrugated metal skin and three radial engines made it instantly recognizable. Used by pioneers like Admiral Byrd and Amelia Earhart.",
        "specs": {
            "Length": "15.3 m (50 ft 3 in)",
            "Wingspan": "23.7 m (77 ft 10 in)",
            "Range": "900 km (560 mi)",
            "Cruise Speed": "170 km/h (107 mph)",
            "Passengers": "11-14",
            "Engines": "3× Wright J-6",
        },
        "sim_features": [
            "Authentic 1920s-era modeling",
            "Detailed corrugated metal skin",
            "Period-appropriate instruments",
            "Multiple historic liveries",
            "Passenger cabin interior",
            "Compatible with MSFS 2020/2024"
        ]
    },
    
    # AeroSachs
    "aerosachs-tecnam-p2002-jf-sierra": {
        "title": "AeroSachs Tecnam P2002 JF Sierra",
        "aircraft_name": "Tecnam P2002 Sierra",
        "developer": "AeroSachs",
        "developer_slug": "aerosachs",
        "excerpt": "Modern Italian light sport aircraft perfect for training and touring.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Tecnam_P2002_Sierra_OE-VGZ.jpg",
        "teaser": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Tecnam_P2002_Sierra_OE-VGZ.jpg/600px-Tecnam_P2002_Sierra_OE-VGZ.jpg",
        "manufacturer": "Tecnam",
        "first_flight": "1992",
        "introduction": "1994",
        "type": "Two-seat light aircraft",
        "description": "The Tecnam P2002 Sierra is an Italian light aircraft that has become one of the most popular training and recreational aircraft worldwide. Its modern all-metal design, excellent visibility, and benign handling characteristics make it ideal for flight training, with over 700 aircraft delivered globally.",
        "specs": {
            "Length": "6.5 m (21 ft 4 in)",
            "Wingspan": "9.0 m (29 ft 6 in)",
            "Range": "1,150 km (715 mi)",
            "Cruise Speed": "215 km/h (134 mph)",
            "Engine": "Rotax 912S (100 hp)",
        },
        "sim_features": [
            "Highly detailed exterior and interior",
            "Accurate flight dynamics",
            "G1000 avionics option",
            "Multiple liveries",
            "Training-focused features",
            "Compatible with MSFS 2020/2024"
        ]
    },
    
    "aerosachs-tecnam-p2010": {
        "title": "AeroSachs Tecnam P2010",
        "aircraft_name": "Tecnam P2010",
        "developer": "AeroSachs",
        "developer_slug": "aerosachs",
        "excerpt": "The modern four-seat single-engine aircraft designed for touring.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Tecnam_P2010_N123TE_%2827614078684%29.jpg",
        "teaser": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Tecnam_P2010_N123TE_%2827614078684%29.jpg/600px-Tecnam_P2010_N123TE_%2827614078684%29.jpg",
        "manufacturer": "Tecnam",
        "first_flight": "2009",
        "introduction": "2012",
        "type": "Four-seat touring aircraft",
        "description": "The Tecnam P2010 is a modern four-seat single-engine aircraft designed to compete with the Cessna 182 and Piper Archer. Featuring a composite fuselage mated to metal wings, modern Garmin avionics, and excellent performance, it represents the new generation of general aviation aircraft.",
        "specs": {
            "Length": "8.7 m (28 ft 7 in)",
            "Wingspan": "11.0 m (36 ft 1 in)",
            "Range": "1,650 km (1,025 mi)",
            "Cruise Speed": "230 km/h (143 mph)",
            "Engine": "Lycoming IO-360 (180 hp)",
        },
        "sim_features": [
            "Detailed G1000 NXi avionics",
            "Realistic flight model",
            "High-quality 3D modeling",
            "Comprehensive systems simulation",
            "Multiple paint schemes",
            "Compatible with MSFS 2020/2024"
        ]
    },
    
    "aerosachs-tecnam-p92": {
        "title": "AeroSachs Tecnam P92",
        "aircraft_name": "Tecnam P92 Echo",
        "developer": "AeroSachs",
        "developer_slug": "aerosachs",
        "excerpt": "Lightweight Italian ultralight perfect for recreational flying.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Tecnam_P92_Echo_D-MSPY.jpg",
        "teaser": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Tecnam_P92_Echo_D-MSPY.jpg/600px-Tecnam_P92_Echo_D-MSPY.jpg",
        "manufacturer": "Tecnam",
        "first_flight": "1992",
        "introduction": "1993",
        "type": "Ultralight aircraft",
        "description": "The Tecnam P92 Echo is a two-seat, high-wing ultralight aircraft that has become one of the most successful designs in its category. With excellent visibility, simple systems, and economical operation, it's a favorite among recreational pilots and flight schools worldwide.",
        "specs": {
            "Length": "6.4 m (21 ft)",
            "Wingspan": "9.6 m (31 ft 6 in)",
            "Range": "900 km (560 mi)",
            "Cruise Speed": "185 km/h (115 mph)",
            "Engine": "Rotax 912ULS (100 hp)",
        },
        "sim_features": [
            "Lightweight flight dynamics",
            "Detailed cockpit",
            "Various avionics configurations",
            "Multiple variants modeled",
            "Realistic Rotax engine simulation",
            "Compatible with MSFS 2020/2024"
        ]
    },
}


def create_aircraft_page(slug, data):
    """Generate markdown content for an aircraft page."""
    
    # Build specifications section
    specs_lines = []
    for key, value in data["specs"].items():
        specs_lines.append(f"- **{key}:** {value}")
    specs_text = "\n".join(specs_lines)
    
    # Build features section
    features_text = "\n".join([f"- {feature}" for feature in data["sim_features"]])
    
    # Generate the markdown content
    content = f"""---
layout: single
title: "{data['title']}"
permalink: /aircraft/{slug}/
excerpt: "{data['excerpt']}"
header:
  overlay_image: "{data['image']}"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 100%)"
  teaser: "{data['teaser']}"
---

# {data['aircraft_name']}

## The Real Aircraft

{data['description']}

**Key Specifications:**
- **Manufacturer:** {data['manufacturer']}
- **First Flight:** {data['first_flight']}
- **Introduction:** {data['introduction']}
- **Type:** {data['type']}
{specs_text}

---

## The Simulation

The **{data['title']}** brings this aircraft to Microsoft Flight Simulator with attention to detail and authentic flight characteristics.

**Features:**
{features_text}

**Developer:** [{data['developer']}](/aircraft-developers/{data['developer_slug']}/)

---

## Developer

For more aircraft from this developer, visit the [{data['developer']}](/aircraft-developers/{data['developer_slug']}/) developer page.
"""
    
    return content


def main():
    """Main function to generate aircraft pages."""
    aircraft_dir = Path("/Users/jonbeckett/Projects/jonbeckett-online.github.io/_pages/resources/aircraft")
    
    created_count = 0
    for slug, data in AIRCRAFT_DATA.items():
        filepath = aircraft_dir / f"{slug}.md"
        
        # Generate content
        content = create_aircraft_page(slug, data)
        
        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        created_count += 1
        print(f"✓ Created: {slug}")
    
    print(f"\n{'='*60}")
    print(f"Generated {created_count} aircraft pages")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
