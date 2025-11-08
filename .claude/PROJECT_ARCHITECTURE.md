# Yellowkey Project Architecture & Workflows

**Project:** Yellowkey Real Estate Platform (yellowkey.qa)
**Framework:** Django 3.2+
**Database:** PostgreSQL
**Last Updated:** January 7, 2025
**Version:** 1.0

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Django Apps Structure](#django-apps-structure)
4. [Database Models](#database-models)
5. [User Roles & Permissions](#user-roles--permissions)
6. [Key Workflows](#key-workflows)
7. [URL Routing](#url-routing)
8. [Authentication Flow](#authentication-flow)
9. [File Structure](#file-structure)
10. [Third-Party Integrations](#third-party-integrations)

---

## Project Overview

Yellowkey is a comprehensive real estate platform for Qatar connecting three main user types:
1. **Property Holders/Landlords** (Clients) - Manage properties and tenants
2. **Realtors/Agents** - List and market properties
3. **Workmen/Service Providers** - Offer maintenance services

### Core Business Model
- Property holders list their buildings/units
- Realtors can view vacant properties and list them
- Workmen find verified maintenance jobs
- Platform facilitates tenant management, rent collection, and property services

---

## Tech Stack

### Backend
- **Framework:** Django 3.2+
- **Language:** Python 3.8+
- **Database:** PostgreSQL
- **ORM:** Django ORM

### Frontend
- **CSS Framework:** Bootstrap 5.0.2
- **Icons:** Font Awesome Free
- **Forms:** Crispy Forms with Bootstrap 5

### Authentication
- **Package:** Django Allauth
- **Social Auth:** Google OAuth
- **Features:** Email verification, password reset

### Other Libraries
- **django-filters** - Advanced filtering
- **python-decouple** - Environment configuration
- **Pillow** - Image processing

---

## Django Apps Structure

### 1. **accounts/** - User Management
**Purpose:** Handle user profiles, authentication, and role assignments

**Models:**
- `Profile` - Extended user profile
  - Fields: username, first_name, last_name, gender, date_of_birth, email, phone, whatsapp, instagram, nationality, address
  - Role Flags: is_business, is_staff, is_realtor, is_workman
- `ProfilePicture` - User avatar/photos
- `Roles` - System roles definition
- `Spoken_Languages` - Language preferences
- `Agent` - Real estate agent profiles

**Key Features:**
- Multi-role support (users can be client + realtor + workman)
- Profile management
- Agent verification system
- Language preferences

**URLs:**
- `/accounts/login/`
- `/accounts/signup/`
- `/accounts/profile/`
- `/accounts/logout/`

---

### 2. **property/** - Property Listings
**Purpose:** Manage properties, buildings, and individual units

**Models:**
- `Property_data` - Building/Property information
  - Fields: title, client_code, property_code, landmark, zone_no, street_no, property_no, photo_main, portion_count
- `Portions` - Individual units/apartments within a property
  - Fields: portion_code, unit_no, floor_no, description, price, bedrooms, bathrooms, portion_type, furnished_type, sqft, photos (main + 3 additional)
  - Types: BACHLOR_BEDSPACE, SINGLE_ROOM, STUDIO, 1BHK-5+BHK, VILLA, APARTMENT, OFFICE, SHOP, STORAGE
- `Portions_status` - Unit availability status
  - Status: OCCUPIED, VACANT, BOOKED, VACANT_SOON, CLOSED, NOT_SET
  - Fields: vacant_date, status
- `Zone_names` - Qatar zone/area mapping
- `Inquire` - Property inquiries/leads

**Key Features:**
- Multi-unit property management
- Status tracking (occupied/vacant/vacant soon)
- Photo galleries for each unit
- Price tracking
- Location-based organization

**URLs:**
- `/property/list/`
- `/property/add/`
- `/property/<id>/edit/`
- `/property/portions/`

---

### 3. **clients/** - Property Holders Dashboard
**Purpose:** Landlord/property owner interface

**Models:**
- Currently extends property and accounts models
- No custom models (uses Property_data and Profile)

**Key Features:**
- Property overview dashboard
- Tenant management
- Rent collection tracking
- Maintenance request management
- Property performance analytics

**URLs:**
- `/clients/dashboard/`
- `/clients/properties/`
- `/clients/tenants/`
- `/clients/maintenance/`

**Access Control:** Requires `is_business=True` in Profile

---

### 4. **realtor/** - Real Estate Agents Dashboard
**Purpose:** Agent interface for property listings and leads

**Models:**
- Currently extends property and accounts models
- Uses Agent model from accounts app

**Key Features:**
- View vacant properties
- View "vacant soon" properties
- Manage property inquiries
- Share leads with other agents
- Agent network/community
- Property listing tools

**URLs:**
- `/realtor/dashboard/`
- `/realtor/listings/`
- `/realtor/vacant-properties/`
- `/realtor/inquiries/`

**Access Control:** Requires `is_realtor=True` in Profile

---

### 5. **workman/** - Service Providers Dashboard
**Purpose:** Interface for maintenance workers and service providers

**Models:**
- Currently extends accounts models
- Uses Profile with `is_workman=True`

**Key Features:**
- View available service jobs
- Accept/decline jobs
- Location-based job listings
- Service request management
- Payment tracking
- Team building features

**URLs:**
- `/workman/dashboard/`
- `/workman/jobs/`
- `/workman/requests/`
- `/workman/payments/`

**Access Control:** Requires `is_workman=True` in Profile

---

### 6. **webpages/** - Public Pages & Marketing
**Purpose:** Public-facing pages, marketing, and content

**Models:**
- `GroupList` - WhatsApp groups for community
  - Fields: group_name, group_no, group_link, group_platform, member_count, description
- `JobList` - Career listings
  - Fields: job_title, company, job_nature, category, job_location, payment_range, job_description, job_tags, job_post_date, job_deadline
  - Categories: management, accounting, medical, services, technology, maintenance
- `MobSubscriber` - Lead capture/subscriptions
  - Fields: name, mobile_no, is_clients, is_realator, is_workman, date_subscribed
  - Links to WhatsApp groups
- `Contact` - Contact form submissions
- `CareersApplication` - Job applications

**Key Pages:**
- Home page with services overview
- Property services page
- Realtor services page
- Workman services page
- About us
- Contact us
- Services overview
- WhatsApp groups
- Careers/jobs listing

**URLs:**
- `/` - Home
- `/services/` - Services overview
- `/property-services/` - For property holders
- `/realtor-services/` - For realtors
- `/workman-services/` - For workmen
- `/about/` - About page
- `/contact/` - Contact form
- `/whatsapp_group/` - Community groups
- `/careers/` - Job listings
- `/robots.txt` - SEO robots file

**Forms:**
- `ContactForm` - Contact inquiries
- `SubscribeForm` - Lead capture
- `CareersApplicationForm` - Job applications
- `CareersAddForm` - Admin add jobs

---

### 7. **help/** - Support & Documentation
**Purpose:** Role-based help guides and workflow documentation

**Models:**
- No models (static help content)

**Views:**
- `help_view()` - General help page (not login required)
- `workman_help()` - Service Provider workflow guide (login required)
- `realtor_help()` - Agent workflow guide (login required)
- `client_help()` - Property Owner workflow guide (login required)

**Features:**
- **Service Provider Help** - 5-step workflow guide:
  1. View Assigned Tasks
  2. Accept/Reject Task
  3. Perform Task
  4. Update Task Status
  5. Mark Task as Complete

- **Agent Help** - 5-step workflow guide:
  1. Add New Property
  2. Manage Property Listings
  3. View Inquiries
  4. Communicate with Clients
  5. Close a Deal

- **Property Owner Help** - 5-step workflow guide:
  1. Register and Create Profile
  2. List a Property
  3. View Property Status
  4. Manage Inquiries
  5. Communicate with Agents

- Accordion-style detailed instructions for each step
- Tips and best practices for each role
- Dashboard-only access (login required)
- Contact information and support details

**URLs:**
- `/help/` - General help (public)
- `/help/workman/` - Service Provider help (dashboard only)
- `/help/realtor/` - Agent help (dashboard only)
- `/help/client/` - Property Owner help (dashboard only)

**Templates:**
- `help/templates/help/help.html` - General help page
- `help/templates/help/workman_help.html` - Service Provider guide
- `help/templates/help/realtor_help.html` - Agent guide
- `help/templates/help/client_help.html` - Property Owner guide

---

## Database Models

### Entity Relationship Overview

```
User (Django Auth)
  ├── Profile (1:1)
  │     ├── ProfilePicture (1:1)
  │     └── Agent (1:1) [if is_realtor=True]
  │
  ├── Property_data (1:Many)
  │     └── Portions (1:Many)
  │           └── Portions_status (1:1)
  │
  └── MobSubscriber (Many:Many with GroupList)
```

### Key Relationships

**User → Profile**
- One-to-one relationship
- Profile extends Django User model
- Stores role flags (is_business, is_realtor, is_workman)

**User → Property_data**
- One-to-many relationship
- A user (property holder) can own multiple properties

**Property_data → Portions**
- One-to-many relationship
- A building can have multiple units/apartments

**Portions → Portions_status**
- One-to-one relationship
- Each unit has one current status

**Profile → Spoken_Languages**
- Many-to-many relationship (through Agent)
- Agents can speak multiple languages

**MobSubscriber → GroupList**
- Many-to-many relationship
- Subscribers can join multiple WhatsApp groups

---

## User Roles & Permissions

### Role System

Yellowkey uses a **multi-role system** where users can have multiple roles simultaneously:

#### 1. **Property Holder/Landlord** (`is_business=True`)
**Permissions:**
- Add/edit/delete properties
- Add/edit units (portions)
- View tenant information
- Manage rent collection
- Request maintenance services
- View property analytics

**Dashboard:** `/clients/dashboard/`

#### 2. **Realtor/Agent** (`is_realtor=True`)
**Permissions:**
- View vacant properties
- View "vacant soon" properties
- Create property inquiries
- Share leads with other agents
- Manage client inquiries
- List properties for rent

**Dashboard:** `/realtor/dashboard/`

**Verification:** Requires admin approval (`Agent.verified='YES'`)

#### 3. **Workman/Service Provider** (`is_workman=True`)
**Permissions:**
- View service job listings
- Accept/decline jobs
- View location-based jobs
- Manage service requests
- Track payments

**Dashboard:** `/workman/dashboard/`

#### 4. **Staff** (`is_staff=True`)
**Permissions:**
- Access Django admin
- Manage all users
- Approve agents
- Manage properties
- View analytics

**Dashboard:** `/admin/`

### Multi-Role Example
A user can be:
- Property Holder + Realtor (owns properties AND sells others' properties)
- Realtor + Workman (sells properties AND provides maintenance)
- All three roles simultaneously

**Dashboard Selection:** `/choose_dashboard/` - Users select which dashboard to access

---

## Key Workflows

### 1. Property Listing Workflow

```
Property Holder:
1. Sign up → Profile created
2. Set is_business=True
3. Add Property_data (building info)
4. Add Portions (individual units)
5. Set Portions_status (VACANT/OCCUPIED)
6. Upload photos
7. Property visible to realtors

Realtor:
1. Sign up → Profile created
2. Set is_realtor=True
3. Apply for agent verification
4. Admin approves (Agent.verified='YES')
5. View vacant properties list
6. Contact property holder
7. List property externally
```

### 2. Tenant Management Workflow

```
Property Holder:
1. Add property and portions
2. Tenant moves in
3. Update Portions_status to OCCUPIED
4. Manage rent collection
5. Handle maintenance requests
6. Tenant moves out
7. Update to VACANT or VACANT_SOON
```

### 3. Maintenance Request Workflow

```
Property Holder/Tenant:
1. Submit maintenance request
2. Request visible to workmen in area

Workman:
1. View location-based jobs
2. Accept job
3. Complete service
4. Mark as complete
5. Payment processed
```

### 4. Lead Generation Workflow

```
Visitor:
1. Visit home page
2. Fill SubscribeForm (name, mobile)
3. Select role interest (client/realtor/workman)
4. MobSubscriber created
5. Added to relevant WhatsApp groups
6. Admin follows up
```

### 5. User Registration & Role Selection

```
New User:
1. Click "Join Now"
2. Allauth registration (email/Google)
3. Create Profile
4. Choose roles:
   - Property Holder (is_business)
   - Realtor (is_realtor)
   - Workman (is_workman)
5. Redirect to relevant dashboard
6. If multiple roles → /choose_dashboard/
```

---

## URL Routing

### Main URL Configuration (`yk/urls.py`)

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('webpages.urls')),
    path('property/', include('property.urls')),
    path('clients/', include('clients.urls')),
    path('realtor/', include('realtor.urls')),
    path('workman/', include('workman.urls')),
    path('help/', include('help.urls')),
]
```

### URL Namespaces

- `webpages:home` - Home page
- `webpages:services` - Services page
- `webpages:contact` - Contact page
- `accounts:profile` - User profile
- `clients:dashboard` - Property holder dashboard
- `realtor:dashboard` - Realtor dashboard
- `workman:dashboard` - Workman dashboard

---

## Authentication Flow

### Technology
- **Django Allauth** for authentication
- **Google OAuth** for social login
- **Email verification** enabled

### Flow

```
Registration:
1. User visits /accounts/signup/
2. Fills registration form OR uses Google OAuth
3. Email verification sent
4. User confirms email
5. Profile auto-created (signal)
6. Redirect to profile setup
7. User selects roles
8. Redirect to dashboard

Login:
1. User visits /accounts/login/
2. Enter credentials OR Google OAuth
3. Check if email verified
4. Successful login
5. Check user roles:
   - Single role → Redirect to that dashboard
   - Multiple roles → /choose_dashboard/
   - No roles → /accounts/profile/

Password Reset:
1. Click "Forgot Password"
2. Enter email
3. Reset link sent
4. User resets password
5. Confirmation
```

### Middleware
- `AccountMiddleware` (Allauth)
- `AuthenticationMiddleware` (Django)
- Session management
- CSRF protection

---

## File Structure

```
yk/
├── accounts/
│   ├── models.py (Profile, Agent, Roles)
│   ├── views.py (profile, registration)
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── accounts/
│
├── property/
│   ├── models.py (Property_data, Portions, Portions_status)
│   ├── views.py (CRUD operations)
│   ├── urls.py
│   └── templates/
│       └── property/
│
├── clients/
│   ├── models.py
│   ├── views.py (dashboard, properties)
│   ├── urls.py
│   └── templates/
│       └── clients/
│
├── realtor/
│   ├── models.py
│   ├── views.py (listings, inquiries)
│   ├── urls.py
│   └── templates/
│       └── realtor/
│
├── workman/
│   ├── models.py
│   ├── views.py (jobs, requests)
│   ├── urls.py
│   └── templates/
│       └── workman/
│
├── webpages/
│   ├── models.py (GroupList, JobList, MobSubscriber, Contact)
│   ├── views.py (home, services, contact)
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── webpages/
│           ├── home.html
│           ├── services.html
│           ├── property_services.html
│           ├── realtor_services.html
│           ├── workman_services.html
│           ├── contact.html
│           ├── about.html
│           ├── whatsapp/
│           └── careers/
│
├── help/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── templates/
│   ├── base.html (main template)
│   ├── includes/
│   │   ├── head.html (meta tags, SEO)
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   ├── scripts.html
│   │   └── css/
│   └── account/ (allauth templates)
│
├── static/
│   ├── webpages/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── assets/
│   └── fontawesomefree/
│
├── media/
│   ├── property/ (property photos)
│   ├── accounts/ (profile pictures)
│   └── agents/ (agent profiles)
│
├── yk/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── .claude/
    ├── SEO_OPTIMIZATION_GUIDE.md
    ├── PROJECT_ARCHITECTURE.md (this file)
    ├── COMMANDS.md
    ├── UPDATE_REMINDER.md
    └── SEO_CHANGELOG.md
```

---

## Third-Party Integrations

### Current Integrations

1. **Google OAuth** (allauth.socialaccount.providers.google)
   - Social login
   - Email verification

2. **Facebook Pages** (Meta tag integration)
   - FB page ID: 113704197128320

3. **WhatsApp Groups**
   - Community groups for clients/realtors/workmen
   - Managed through GroupList model

4. **Bootstrap 5.0.2** (CDN)
   - Frontend styling

5. **Font Awesome Free**
   - Icon library

6. **Crispy Forms**
   - Form rendering with Bootstrap 5

### Planned Integrations
- Payment gateway (for rent collection)
- SMS notifications
- Email marketing
- Google Maps API (location services)
- Document storage (contracts, agreements)

---

## Environment Configuration

### Required Environment Variables (`.env`)

```
# Django
SECRET_KEY=your-secret-key
DEBUG=True/False
ALLOWED_HOSTS=localhost,127.0.0.1,yellowkey.qa

# Database
DB_NAME=yellowkey_db
DB_USER=postgres_user
DB_PASSWORD=your-password
DB_HOST=localhost
PORT=5432

# Email (for allauth)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_SECRET=your-google-secret

# Static/Media
STATIC_URL=/static/
MEDIA_URL=/media/
```

---

## Database Schema

### accounts_profile
- user_id (FK to auth_user)
- username, first_name, last_name
- gender, date_of_birth
- email, phone, whatsapp, instagram
- nationality, address
- is_business, is_staff, is_realtor, is_workman (role flags)
- created_at, updated_at

### accounts_agent
- user_id (FK to auth_user)
- agent_name, marketing_name
- roles_id (FK to accounts_roles)
- email, phone, whatsapp
- profile_image
- active (YES/NO)
- verified (YES/NO)

### property_property_data
- user_id (FK to auth_user)
- title, client_code, property_code
- landmark
- zone_no, street_no, property_no
- photo_main
- portion_count
- date_created, date_updated

### property_portions
- property_data_id (FK to property_property_data)
- user_id (FK to auth_user)
- portion_code, unit_no, floor_no
- description, price
- bedrooms, bathrooms
- portion_type (STUDIO, 1BHK, 2BHK, etc.)
- furnished_type (Furnished, Semi-Furnished, UnFurnished)
- sqft
- photo_main, photo_1, photo_2, photo_3
- date_created, date_updated

### property_portions_status
- portions_id (FK to property_portions)
- vacant_date
- status (OCCUPIED, VACANT, BOOKED, VACANT_SOON, CLOSED)

### webpages_grouplist
- group_name, group_no
- group_link, group_platform
- member_count, description

### webpages_joblist
- job_title, company
- job_nature, category
- job_location
- payment_range
- job_description, job_tags
- job_post_date, job_deadline

### webpages_mobsubscriber
- name, mobile_no
- is_clients, is_realator, is_workman (interest flags)
- date_subscribed
- whatsapp_group_id (M2M to GroupList)

---

## Common Development Tasks

### Adding a New Property
```python
# In clients dashboard
property = Property_data.objects.create(
    user=request.user,
    title="My Building",
    client_code="BLD001",
    property_code="YK-BLD001",
    landmark="Near Pearl",
    zone_no=25,
    street_no=100,
    property_no=50
)

# Add units
portion = Portions.objects.create(
    property_data=property,
    user=request.user,
    portion_code="10001",
    unit_no=101,
    floor_no=1,
    price=3000,
    bedrooms=1,
    bathrooms=1,
    portion_type='1BHK',
    furnished_type='Furnished'
)

# Set status
status = Portions_status.objects.create(
    portions=portion,
    status='VACANT',
    vacant_date=datetime.now()
)
```

### Checking User Roles
```python
# In views
if request.user.profile.is_business:
    # Property holder features

if request.user.profile.is_realtor:
    # Realtor features

if request.user.profile.is_workman:
    # Workman features
```

### Filtering Vacant Properties
```python
# Get all vacant portions
vacant_portions = Portions.objects.filter(
    portions_status__status='VACANT'
)

# Get vacant soon
vacant_soon = Portions.objects.filter(
    portions_status__status='VACANT_SOON',
    portions_status__vacant_date__lte=datetime.now() + timedelta(days=30)
)
```

---

## API Endpoints (Future)

### Planned RESTful API

```
GET  /api/properties/          # List all properties
GET  /api/properties/:id/      # Get property details
POST /api/properties/          # Create property
PUT  /api/properties/:id/      # Update property
DEL  /api/properties/:id/      # Delete property

GET  /api/portions/            # List all portions
GET  /api/portions/vacant/     # Get vacant portions
GET  /api/portions/:id/        # Get portion details

GET  /api/inquiries/           # List inquiries
POST /api/inquiries/           # Create inquiry

GET  /api/jobs/                # List jobs (workman)
POST /api/jobs/:id/accept/     # Accept job
```

---

## Performance Considerations

### Current Setup
- PostgreSQL database
- Django ORM queries
- Static files served by Django (development)

### Production Optimizations Needed
1. **Database Indexing**
   - Add indexes on frequently queried fields
   - zone_no, street_no, property_no
   - portions.status
   - portions.portion_type

2. **Caching**
   - Redis for session storage
   - Cache vacant property lists
   - Cache user dashboards

3. **Static Files**
   - CDN for static assets
   - Image optimization
   - Lazy loading for property photos

4. **Query Optimization**
   - Use select_related() for foreign keys
   - Use prefetch_related() for M2M
   - Implement pagination for lists

---

## Security Considerations

### Current Security
- CSRF protection enabled
- Password hashing (Django default)
- Session management
- Email verification

### Additional Security Needed
1. Rate limiting on forms
2. File upload validation
3. SQL injection protection (using ORM)
4. XSS protection
5. HTTPS enforcement
6. Secure password reset flow

---

## Testing Strategy

### Unit Tests
- Test models (create, update, delete)
- Test views (response codes, redirects)
- Test forms (validation)
- Test authentication flow

### Integration Tests
- Test complete workflows
- Property listing flow
- User registration flow
- Inquiry submission flow

### Test Coverage Goals
- Models: 90%+
- Views: 80%+
- Forms: 90%+

---

## Deployment Checklist

### Pre-Deployment
- [ ] DEBUG=False
- [ ] ALLOWED_HOSTS configured
- [ ] Secret key secured
- [ ] Database backed up
- [ ] Static files collected
- [ ] Media files secured
- [ ] Email settings configured
- [ ] Google OAuth configured
- [ ] SSL certificate installed

### Post-Deployment
- [ ] Test all user flows
- [ ] Monitor error logs
- [ ] Set up backups
- [ ] Monitor performance
- [ ] Set up analytics

---

## Future Enhancements

### Planned Features
1. **Payment Integration**
   - Rent collection
   - Service payments
   - Commission tracking

2. **Tenant Portal**
   - Pay rent online
   - Submit maintenance requests
   - View lease agreement
   - Communication with landlord

3. **Advanced Search**
   - Filters (price, location, type)
   - Map view
   - Saved searches
   - Alerts for new listings

4. **Analytics Dashboard**
   - Property performance
   - Occupancy rates
   - Revenue tracking
   - Market insights

5. **Mobile App**
   - iOS and Android
   - Push notifications
   - Location services

6. **Document Management**
   - Lease agreements
   - Digital signatures
   - Contract templates
   - Document storage

7. **Communication**
   - In-app messaging
   - Email notifications
   - SMS alerts
   - WhatsApp integration

---

## Troubleshooting

### Common Issues

**Issue:** User can't access dashboard
**Solution:** Check role flags in Profile (is_business, is_realtor, is_workman)

**Issue:** Property not showing in vacant list
**Solution:** Check Portions_status is set to 'VACANT'

**Issue:** Photos not uploading
**Solution:** Check MEDIA_ROOT and MEDIA_URL settings, verify upload directory permissions

**Issue:** Email verification not working
**Solution:** Check EMAIL_BACKEND settings, verify SMTP credentials

---

## Contact & Support

### Development Team
- Backend: Django/Python developers
- Frontend: Bootstrap/HTML/CSS developers
- DevOps: Server management, deployment

### Documentation Updates
To update this documentation:
1. Edit `.claude/PROJECT_ARCHITECTURE.md`
2. Update "Last Updated" date
3. Commit changes
4. Notify team

### Claude Memory
This file serves as permanent memory for Claude AI assistant. Reference this file when:
- Understanding project structure
- Implementing new features
- Debugging issues
- Onboarding new developers

---

**End of Document**

For SEO documentation, see: `.claude/SEO_OPTIMIZATION_GUIDE.md`
For quick commands, see: `.claude/COMMANDS.md`
For update workflow, see: `.claude/UPDATE_REMINDER.md`
