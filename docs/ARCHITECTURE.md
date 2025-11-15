# Yellow Key AMRC - Architecture Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Project Structure](#project-structure)
3. [Django Apps](#django-apps)
4. [Database Schema](#database-schema)
5. [Frontend Architecture](#frontend-architecture)
6. [Static Files Organization](#static-files-organization)
7. [Template System](#template-system)
8. [URL Routing](#url-routing)
9. [Authentication & Authorization](#authentication--authorization)
10. [API Architecture](#api-architecture)

---

## System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│  (Bootstrap 5, Custom CSS, JavaScript, Font Awesome)        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Django Templates Layer                    │
│  (base.html, base_dashboard.html, app-specific templates)  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      Django Views Layer                      │
│        (Function-based & Class-based views)                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                     Django Models Layer                      │
│              (ORM - PostgreSQL Database)                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    PostgreSQL Database                       │
│  (Property data, User profiles, Portions, Inquiries, etc.)  │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Backend Framework** | Django | 5.1.7 |
| **Language** | Python | 3.12.7 |
| **Database** | PostgreSQL | 12+ |
| **Frontend Framework** | Bootstrap | 5.0.2 |
| **Icons** | Font Awesome | 6.6.0 |
| **Forms** | Crispy Forms + Bootstrap5 | Latest |
| **Authentication** | Django Allauth | Latest |
| **API** | Django REST Framework | 3.15.2 |
| **Async Tasks** | Celery | 5.4.0 |
| **Image Processing** | Pillow | 11.1.0 |
| **Geocoding** | Geopy | 2.4.1 |

---

## Project Structure

```
yk/                                    # Project root
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── .env                              # Environment variables (not in git)
├── .gitignore                        # Git ignore rules
├── .claudeignore                     # Claude AI ignore rules
│
├── docs/                             # Documentation
│   ├── PROJECT_SETUP_GUIDE.md       # Setup instructions
│   ├── ARCHITECTURE.md              # This file
│   ├── DEVELOPMENT_WORKFLOW.md      # Development guide
│   └── VSCODE_SETUP_AND_WORKFLOW.md # VS Code configuration
│
├── yk/                               # Main project configuration
│   ├── __init__.py
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # Root URL configuration
│   ├── wsgi.py                       # WSGI configuration
│   └── asgi.py                       # ASGI configuration
│
├── accounts/                         # User authentication & profiles
│   ├── models.py                     # Profile, Roles, Agent models
│   ├── views.py                      # Authentication views
│   ├── forms.py                      # User forms
│   ├── urls.py                       # Account URLs
│   ├── admin.py                      # Admin configuration
│   └── templates/accounts/           # Account templates
│
├── property/                         # Property management
│   ├── models.py                     # Property, Portions, Inquire
│   ├── views.py                      # Property CRUD views
│   ├── forms.py                      # Property forms
│   ├── urls.py                       # Property URLs
│   └── templates/property/           # Property templates (18 files)
│
├── realtor/                          # Real estate agent dashboard
│   ├── views.py                      # Realtor dashboard views
│   ├── urls.py                       # Realtor URLs
│   └── templates/realtor/            # Realtor templates (17 files)
│
├── clients/                          # Property owner portal
│   ├── views.py                      # Client dashboard views
│   ├── urls.py                       # Client URLs
│   └── templates/clients/            # Client templates (12 files)
│
├── workman/                          # Service provider network
│   ├── views.py                      # Workman views
│   ├── urls.py                       # Workman URLs
│   └── templates/workman/            # Workman templates
│
├── webpages/                         # Public-facing website
│   ├── models.py                     # Contact, Jobs, Subscribers
│   ├── views.py                      # Public page views (24K+ lines)
│   ├── urls.py                       # Public URLs
│   └── templates/webpages/           # Public templates (21 files)
│
├── help/                             # Help & support system
│   ├── views.py                      # Help page views
│   ├── urls.py                       # Help URLs
│   └── templates/help/               # Role-based help pages
│
├── templates/                        # Global templates
│   ├── base.html                     # Base template (public)
│   ├── base_dashboard.html           # Dashboard base template
│   ├── includes/                     # Reusable components
│   │   ├── head.html                # SEO & meta tags
│   │   ├── navbar.html              # Navigation bar
│   │   ├── footer.html              # Footer
│   │   ├── scripts.html             # Global scripts
│   │   └── css/
│   │       ├── style.html           # Global styles
│   │       └── dashboard_style.html # Dashboard styles
│   ├── account/                      # Allauth templates (17 files)
│   └── socialaccount/               # Social auth templates
│
├── static/                           # Static files
│   ├── assets/                       # Shared assets
│   │   └── css/
│   │       └── brandkit.css         # Brand design system
│   ├── accounts/                     # Account app static files
│   │   ├── css/accounts.css
│   │   └── js/accounts.js
│   ├── property/
│   │   └── css/property.css
│   ├── realtor/
│   │   └── css/realtor_dashboard.css
│   ├── clients/
│   │   └── css/clients_dashboard.css
│   ├── workman/
│   │   └── css/workman_dashboard.css
│   ├── webpages/
│   │   ├── css/
│   │   │   ├── main.css
│   │   │   ├── modern-forms.css
│   │   │   └── base.css
│   │   ├── js/bundle.js
│   │   └── img/
│   ├── help/
│   │   └── css/help_dashboard.css
│   └── fontawesomefree/              # Font Awesome 6.6.0
│
└── media/                            # User uploads
    ├── accounts/                     # Profile pictures
    ├── property/                     # Property images
    └── webpages/                     # Website assets
        └── brand/                    # Brand logos
```

---

## Django Apps

### 1. **accounts** - User Authentication & Profiles

**Purpose**: User authentication, profile management, and role assignment

**Key Models**:
- `Profile` - Extended user profile with role information
- `ProfilePicture` - User profile images
- `Roles` - User role definitions (Admin, Realtor, Client, Workman)
- `Spoken_Languages` - Multi-language support
- `Agent` - Real estate agent profiles

**Key Features**:
- Django Allauth integration (Google OAuth)
- Custom user profiles with images
- Role-based access control
- Multi-language preferences

**URL Prefix**: `/accounts/`

---

### 2. **property** - Property & Portion Management

**Purpose**: Core property listing and management system

**Key Models**:
- `Property_data` - Main property information
  - Fields: Property name, zone, owner details, photos
  - Relations: ForeignKey to Zone_names, OneToOne to User
- `Portions` - Individual units within properties
  - Fields: Portion number, floor, area, rent, status
  - Relations: ForeignKey to Property_data
- `Portions_status` - Available/Occupied/Maintenance statuses
- `Zone_names` - Geographic zones in Qatar
- `Inquire` - Property inquiries from potential tenants

**Key Features**:
- Property CRUD operations
- Portion (unit) management
- Zone-based filtering
- Inquiry management
- Photo upload and management
- Status tracking

**URL Prefix**: `/property/`

---

### 3. **realtor** - Real Estate Agent Dashboard

**Purpose**: Tools and interface for real estate agents

**Key Features**:
- Agent dashboard with statistics
- Property listings (vacant properties)
- Inquiry management
- Booking management
- Contact management
- Report generation
- Collaboration tools

**URL Prefix**: `/realtor/`

---

### 4. **clients** - Property Owner Portal

**Purpose**: Interface for property owners to manage their properties

**Key Features**:
- Client dashboard
- Property portfolio view
- Portion management
- Property and portion CRUD
- Financial overview

**URL Prefix**: `/clients/`

---

### 5. **workman** - Service Provider Network

**Purpose**: Platform for service providers and maintenance workers

**Key Models**:
- Service provider profiles
- Job listings

**Key Features**:
- Workman dashboard
- Job listings by location
- Service provider profiles

**URL Prefix**: `/workman/`

---

### 6. **webpages** - Public Website

**Purpose**: Public-facing pages and marketing content

**Key Models**:
- `GroupList` - Group listings
- `JobList` - Career opportunities
- `MobSubscriber` - Newsletter subscribers
- `Contact` - Contact form submissions
- `CareersApplication` - Job applications

**Key Features**:
- Homepage
- About page
- Services page
- Contact form
- Careers/jobs portal
- SEO optimization
- Sitemap generation
- Social media integration

**URL Prefix**: `/` (root level)

---

### 7. **help** - Support System

**Purpose**: Role-based help and documentation

**Key Features**:
- Client help pages
- Realtor help pages
- Workman help pages
- FAQ sections
- Tutorial content

**URL Prefix**: `/help/`

---

## Database Schema

### Core Tables

#### accounts_profile
```sql
- id (PK)
- user_id (FK → auth_user)
- roles_id (FK → accounts_roles)
- phone
- bio
- location
- profile_picture_id (FK → accounts_profilepicture)
- created_at
- updated_at
```

#### property_property_data
```sql
- id (PK)
- owner_id (FK → auth_user)
- zone_name_id (FK → property_zone_names)
- property_name
- property_photo_1, _2, _3, _4, _5
- building_no
- street_no
- zone_no
- unit_no
- created_at
- updated_at
```

#### property_portions
```sql
- id (PK)
- property_id (FK → property_property_data)
- status_id (FK → property_portions_status)
- portion_number
- floor
- bedrooms
- bathrooms
- area_sqm
- monthly_rent
- portion_photo_1, _2, _3, _4
- created_at
- updated_at
```

#### property_inquire
```sql
- id (PK)
- property_id (FK → property_property_data)
- portion_id (FK → property_portions, nullable)
- inquirer_name
- inquirer_email
- inquirer_phone
- message
- status (pending/contacted/closed)
- created_at
```

### Relationships

```
auth_user (1) ─────── (1) accounts_profile
    │
    └──── (1) ──────── (N) property_property_data
                            │
                            └──── (1) ──────── (N) property_portions
                                                    │
                                                    └──── (1) ──── (N) property_inquire
```

---

## Frontend Architecture

### CSS Architecture

**Load Order** (defined in [templates/includes/head.html](templates/includes/head.html:61-93)):
1. **brandkit.css** - Design tokens and CSS variables (MUST load first)
2. **Bootstrap 5** - Base framework
3. **Font Awesome 6.6.0** - Icon library
4. **Google Fonts** - Poppins font family
5. **Bootstrap Icons** - Additional icons
6. **App-specific CSS** - Feature styling
7. **modern-forms.css** - Form styling

### CSS Files

| File | Purpose | Lines |
|------|---------|-------|
| `assets/css/brandkit.css` | Brand design system, CSS variables, utility classes | 700+ |
| `webpages/css/modern-forms.css` | Modern form styling with animations | 631 |
| `property/css/property.css` | Property card layouts | 726 |
| `realtor/css/realtor_dashboard.css` | Realtor dashboard | 193 |
| `clients/css/clients_dashboard.css` | Client dashboard | 79 |
| `workman/css/workman_dashboard.css` | Workman dashboard | 229 |
| `help/css/help_dashboard.css` | Help system | 752 |
| `accounts/css/accounts.css` | Authentication & profiles | NEW |

### Brand Design System (brandkit.css)

**CSS Custom Properties**:
```css
--brand-primary: #ebcb1b          /* Yellow Key Gold */
--brand-primary-dark: #e4ac14     /* Darker Yellow */
--brand-secondary: #232c3d        /* Dark Navy */
--text-primary: #232c3d           /* Main text */
--text-secondary: #727982         /* Secondary text */
```

**Utility Classes**:
- Text colors: `.text-primary`, `.text-secondary`, `.text-muted`
- Backgrounds: `.bg-primary`, `.bg-gradient-primary`
- Spacing: `.m-{0-8}`, `.p-{0-8}`, `.mt-{0-8}`, `.pt-{0-8}`
- Shadows: `.shadow-sm`, `.shadow`, `.shadow-lg`
- Borders: `.rounded-sm`, `.rounded`, `.rounded-lg`

---

## Template System

### Template Hierarchy

```
base.html                              # Public pages base
├── webpages/home.html                # Homepage
├── webpages/about.html               # About page
├── webpages/services.html            # Services
├── account/login.html                # Login
└── account/signup.html               # Signup

base_dashboard.html                    # Authenticated dashboards
├── realtor/realtor_dashboard.html    # Realtor dashboard
├── clients/clients_dashboard.html    # Client dashboard
├── property/property_list.html       # Property list
├── property/property_add.html        # Add property
└── workman/workman_dashboard.html    # Workman dashboard
```

### Template Blocks

**base.html** blocks:
- `{% block title %}` - Page title
- `{% block meta %}` - Custom meta tags
- `{% block og_meta %}` - OpenGraph meta
- `{% block extra_css %}` - Additional CSS
- `{% block content %}` - Main content
- `{% block extra_js %}` - Additional JavaScript

**base_dashboard.html** additional blocks:
- `{% block sidebar %}` - Sidebar navigation
- `{% block account_content %}` - Dashboard content

### Includes

**Global includes** (used in base templates):
- `includes/head.html` - SEO meta tags, CSS includes
- `includes/navbar.html` - Navigation bar
- `includes/footer.html` - Footer with social links
- `includes/scripts.html` - Global JavaScript
- `includes/css/style.html` - Inline styles
- `includes/css/dashboard_style.html` - Dashboard styles

---

## URL Routing

### Root URLs ([yk/urls.py](yk/urls.py))

```python
urlpatterns = [
    path('admin/', admin.site.urls),           # Admin panel
    path('accounts/', include('allauth.urls')), # Authentication
    path('property/', include('property.urls')), # Properties
    path('realtor/', include('realtor.urls')),  # Realtor
    path('clients/', include('clients.urls')),  # Clients
    path('workman/', include('workman.urls')),  # Workman
    path('help/', include('help.urls')),        # Help
    path('', include('webpages.urls')),         # Public pages
    path('sitemap.xml', sitemap_view),          # SEO sitemap
    path('robots.txt', robots_txt),             # SEO robots
]
```

### Static & Media Files

```python
# Development
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Production
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## Authentication & Authorization

### Authentication System

**Provider**: Django Allauth

**Supported Methods**:
- Email/Password authentication
- Google OAuth (Social authentication)

**User Model**: Extended with `Profile` model (OneToOne relationship)

### Authorization Levels

**Roles** (defined in `accounts.models.Roles`):
1. **Admin** - Full system access
2. **Realtor** - Real estate agent access
3. **Client** - Property owner access
4. **Workman** - Service provider access

### Permission System

**View-level permissions**:
```python
@login_required
@user_passes_test(lambda u: u.profile.roles.name == 'Realtor')
def realtor_dashboard(request):
    # Realtor-only view
    pass
```

---

## API Architecture

**Framework**: Django REST Framework (DRF)

**API Endpoints** (if implemented):
- `/api/properties/` - Property listings
- `/api/portions/` - Portion data
- `/api/inquiries/` - Inquiry submissions

**Authentication**: Token-based or Session-based

---

## Performance Considerations

### Database Optimization
- Indexed fields: Property name, zone, status
- `select_related()` for ForeignKey relationships
- `prefetch_related()` for reverse ForeignKey and ManyToMany

### Caching Strategy
- Template fragment caching
- Database query caching
- Static file caching (CDN ready)

### Static File Management
- Collected via `collectstatic`
- Served via CDN in production
- Compressed CSS/JS in production

---

## Security Measures

1. **CSRF Protection** - Django middleware enabled
2. **XSS Protection** - Template auto-escaping
3. **SQL Injection** - ORM prevents injection
4. **Secure Headers** - Security middleware configured
5. **HTTPS Only** - In production
6. **Password Hashing** - PBKDF2 algorithm
7. **Environment Variables** - Sensitive data in `.env`

---

## Deployment Architecture

```
                     Internet
                        │
                        ↓
                   Load Balancer
                        │
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
    Django App     Django App     Django App
    (Gunicorn)     (Gunicorn)     (Gunicorn)
        │               │               │
        └───────────────┼───────────────┘
                        ↓
                  PostgreSQL Database
                        │
                  Redis (Celery)
```

---

**Last Updated**: November 15, 2025
**Version**: 1.0
**Maintainer**: AMRC Development Team
