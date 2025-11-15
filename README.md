# Yellow Key AMRC - All-in-One Real Estate Platform

**Comprehensive Real Estate Management Platform for Qatar**

---

## About

**Yellow Key AMRC** is a comprehensive real estate management platform specifically designed for the Qatar market. The platform connects property holders, real estate agents (realtors), and service providers (workmen) in a unified ecosystem.

### Target Users

- **Property Owners**: Manage properties and portions (units) with ease
- **Real Estate Agents (Realtors)**: Access vacant property listings, manage inquiries
- **Service Providers (Workmen)**: Find location-based jobs and service opportunities
- **Property Seekers**: Browse available properties and submit inquiries

---

## Technology Stack

### Backend
- Django 5.1.7
- Python 3.12.7
- PostgreSQL 12+
- Celery 5.4.0
- Django REST Framework 3.15.2

### Frontend
- Bootstrap 5.0.2
- Font Awesome 6.6.0
- Vanilla JavaScript (ES6+)
- Google Fonts (Poppins)

---

## Quick Start

```bash
# 1. Activate virtual environment
cd c:\00-web-dev\django-ykqaenv
.\Scripts\activate               # Windows
source bin/activate              # Linux/macOS

# Alternative: If using venvykqa for testing
cd c:\00-web-dev\django-ykenv
.\venvykqa\Scripts\activate      # Windows
source venvykqa/bin/activate     # Linux/macOS

# 2. Navigate to project
cd yk

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup database
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```

Visit http://127.0.0.1:8000/

---

## Documentation

Comprehensive documentation is available in the `/docs/` directory:

- **[PROJECT_SETUP_GUIDE.md](docs/PROJECT_SETUP_GUIDE.md)**: Complete setup instructions
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)**: System architecture and design
- **[DEVELOPMENT_WORKFLOW.md](docs/DEVELOPMENT_WORKFLOW.md)**: Development best practices
- **[VSCODE_SETUP_AND_WORKFLOW.md](docs/VSCODE_SETUP_AND_WORKFLOW.md)**: VS Code configuration
- **[CSS_LOADING_ORDER.md](docs/CSS_LOADING_ORDER.md)**: ⚠️ Critical CSS load order (MUST READ)
- **[JAVASCRIPT_MODULES_GUIDE.md](docs/JAVASCRIPT_MODULES_GUIDE.md)**: Complete JavaScript reference
- **[URL_TESTING_REPORT.md](docs/URL_TESTING_REPORT.md)**: URL testing results and fixes

---

## Features

### For Property Owners
- Property Management (CRUD operations)
- Portion (Unit) Management
- Photo Upload (5 per property, 4 per portion)
- Owner Dashboard
- Inquiry Management

### For Realtors
- Realtor Dashboard with statistics
- Vacant Property Listings
- Inquiry System
- Booking Management
- Contact Management
- Collaboration Tools

### For Service Providers
- Workman Dashboard
- Location-Based Job Listings
- Service Provider Profiles
- Verified Job Opportunities

### General Features
- Multi-Role System (Admin, Realtor, Client, Workman)
- Google OAuth Integration
- SEO Optimized (comprehensive meta tags, structured data)
- Mobile Responsive
- Multi-Language Support (English/Arabic)
- RESTful API

---

## Project Structure

```
yk/
├── accounts/               # Authentication & profiles
├── property/               # Property & portion management
├── realtor/                # Realtor dashboard
├── clients/                # Property owner portal
├── workman/                # Service provider network
├── webpages/               # Public website
├── help/                   # Help system
├── templates/              # Global templates
├── static/                 # Static files
│   └── assets/css/brandkit.css  # Design system
├── media/                  # User uploads
└── docs/                   # Documentation
```

---

## Design System

The project uses a comprehensive brand design system with **critical CSS load order**:

### ⚠️ Critical: CSS Loading Order
```html
1. brandkit.css              → CSS variables & design tokens (FIRST)
2. Bootstrap 5               → Third-party framework
3. brandkit-overrides.css    → Override Bootstrap styles
4. Font Awesome              → Icon library
5. Google Fonts              → Typography
6. Application CSS           → Page-specific styles
7. brandkit-overrides.css    → FINAL override (MUST BE LAST!)
```

**Important:** `brandkit-overrides.css` loads TWICE - once after Bootstrap and once at the very end to override ALL styles. See [CSS_LOADING_ORDER.md](docs/CSS_LOADING_ORDER.md) for details.

### 🎨 Brand Colors (Version 3.0 - Yellow/Red/Blue)

**Primary Palette - Vibrant Yellow**
- Yellow: `#F3C130` - Brand primary color (buttons, highlights)
- Yellow Dark: `#D8A500` - Hover states and active elements

**Secondary Palette - Vibrant Red**
- Red: `#FF5851` - Brand secondary color (accents, alerts)
- Deep Red: `#E63F38` - Hover states

**Tertiary Palette - Professional Blue**
- Blue: `#414A6B` - Brand tertiary color (navigation, headings)
- Black: `#1C1B20` - Primary text color

**Neutral Palette - Clean Grays**
- Light Grey: `#F4F4F4` - Page backgrounds
- Medium Grey: `#E4E4E4` - Borders and dividers
- Dark Grey: `#C2C2C2` - Secondary borders
- White: `#FFFFFF` - Card backgrounds

### ✨ Modern Design Features

- **Vibrant Gradients** - Yellow-to-red gradient combinations
- **Glassmorphism Cards** - Frosted glass effect with backdrop blur
- **Animated Buttons** - Shimmer effects and 3D hover lift
- **Accent Shadows** - Multi-layer depth with yellow/red glows
- **Gradient Typography** - H1 headings with yellow-to-red gradient text

### 📁 CSS Files
- `static/assets/css/brandkit.css` - Complete color system (590+ lines)
- `static/assets/css/brandkit-overrides.css` - Component overrides (830+ lines)
- All !important flags ensure brand styles override everything

---

## Contact

- **Email**: contact@yellowkey.qa
- **Phone**: +974-33430001
- **Website**: https://www.yellowkey.qa
- **Address**: 534 Al Sadd, Doha, Qatar

---

**© 2025 Yellowkey Holdings. All Rights Reserved.**
