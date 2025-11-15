# Yellow Key AMRC - Complete Workflow Documentation

## Overview
This document describes the complete workflows and processes across all apps in the Yellow Key AMRC real estate management platform, from user registration to property management and inquiry handling.

---

## System Architecture

### Apps Involved:
1. **accounts** - User authentication, profiles, and role management
2. **property** - Property and portion (unit) management
3. **realtor** - Real estate agent dashboard and tools
4. **clients** - Property owner portal and management
5. **workman** - Service provider network and job listings
6. **webpages** - Public-facing website and content
7. **help** - Role-based help and support system

---

## Complete User Workflows

### 1. User Registration & Authentication

#### 1.1 New User Registration

**Entry Points:**
- Public signup page: `/accounts/signup/`
- Google OAuth: `/accounts/google/login/`

**Process:**
1. User submits registration form (email/password or Google OAuth)
2. Django Allauth creates `User` account
3. Signal `create_user_profile` automatically creates:
   - `Profile` record linked to user
   - Default role assignment (if specified)
   - Empty `ProfilePicture` placeholder
4. User receives verification email (if email verification enabled)
5. User confirms email and account is activated

**Models Involved:**
- `User` (Django auth user)
- `Profile` (accounts app)
- `ProfilePicture` (accounts app)
- `Roles` (accounts app)

**URLs:**
```
/accounts/signup/              # Registration form
/accounts/login/               # Login form
/accounts/google/login/        # Google OAuth
/accounts/password/reset/      # Password reset
```

#### 1.2 User Login

**Process:**
1. User enters credentials or uses Google OAuth
2. Django Allauth validates credentials
3. User is redirected to role-specific dashboard:
   - Property Owner → `/clients/dashboard/`
   - Realtor → `/realtor/dashboard/`
   - Workman → `/workman/dashboard/`
   - Admin → `/admin/`
4. Session is created and maintained

#### 1.3 Profile Management

**Process:**
1. User navigates to `/accounts/profile/`
2. User can update:
   - Profile picture
   - Bio and description
   - Contact information (phone)
   - Location
   - Spoken languages
   - Role-specific information (Agent details, etc.)
3. Changes are saved to `Profile` and related models
4. Profile picture uploaded to `media/accounts/`

---

### 2. Property Management Workflow (Property Owner)

#### 2.1 Property Creation

**Entry Point:** `/property/add/`

**Process:**
1. **Property Owner** navigates to "Add Property"
2. Fills out `PropertyForm`:
   - Property name
   - Zone selection (from `Zone_names`)
   - Building, street, zone numbers
   - Upload up to 5 photos
3. Form is validated:
   - Required fields checked
   - Photo file size validated
   - Zone must exist
4. `Property_data` record is created:
   - `owner` = current user
   - `created_at` = timestamp
   - Photos saved to `media/property/`
5. User redirected to property detail page
6. Property appears in owner's portfolio

**Models:**
- `Property_data` (main property model)
- `Zone_names` (zones in Qatar)
- User as foreign key (owner)

**Validation Rules:**
- Property name required
- Zone must be selected
- At least 1 photo required
- Max 5 photos per property
- Each photo max 5MB

#### 2.2 Portion (Unit) Management

**Entry Point:** `/property/<property_id>/portions/add/`

**Process:**
1. Owner selects a property
2. Clicks "Add Portion/Unit"
3. Fills out `PortionsForm`:
   - Portion number
   - Floor
   - Bedrooms, bathrooms
   - Area (sqm)
   - Monthly rent
   - Status (Available/Occupied/Maintenance)
   - Upload up to 4 photos
4. `Portions` record is created:
   - Linked to `Property_data` via foreign key
   - Linked to `Portions_status`
5. Portion appears in property details
6. Available portions visible to realtors

**Models:**
- `Portions` (unit/portion model)
- `Portions_status` (status options)
- Foreign key to `Property_data`

**Status Options:**
- Available (vacant, ready for rent)
- Occupied (currently rented)
- Maintenance (under repair/renovation)
- Reserved (held for specific tenant)

---

### 3. Realtor Workflow

#### 3.1 Accessing Vacant Properties

**Entry Point:** `/realtor/properties/vacant/`

**Process:**
1. **Realtor** logs into dashboard
2. Navigates to "Vacant Properties"
3. System queries:
   ```python
   available_portions = Portions.objects.filter(
       status__status_name='Available'
   ).select_related('property', 'status')
   ```
4. Realtor can filter by:
   - Zone
   - Price range
   - Bedroom count
   - Property type
5. Realtor views property details
6. Realtor can contact property owner or submit inquiry

#### 3.2 Inquiry Management

**Entry Point:** `/realtor/inquiries/`

**Process:**
1. Customer submits inquiry via public form
2. `Inquire` record is created:
   - Linked to property and/or portion
   - Customer name, email, phone
   - Message content
   - Status: `pending`
3. Inquiry appears in realtor dashboard
4. Realtor can:
   - View inquiry details
   - Change status (pending → contacted → closed)
   - Reply to customer (email integration)
   - Mark as resolved
5. Inquiry log is maintained for tracking

**Models:**
- `Inquire` (inquiry/lead model)
- Foreign keys to `Property_data` and `Portions`

**Inquiry Statuses:**
- Pending (new inquiry)
- Contacted (realtor reached out)
- Qualified (potential client)
- Closed (deal done or lost)

#### 3.3 Booking Management

**Entry Point:** `/realtor/bookings/`

**Process:**
1. Realtor schedules property viewing
2. Creates booking record:
   - Customer details
   - Property/portion
   - Viewing date and time
   - Status
3. Calendar integration shows upcoming viewings
4. Realtor can:
   - Confirm booking
   - Reschedule
   - Mark as completed
   - Add notes

---

### 4. Client (Property Owner) Dashboard Workflow

#### 4.1 Portfolio Overview

**Entry Point:** `/clients/dashboard/`

**Process:**
1. Owner views all properties
2. Dashboard displays:
   - Total properties count
   - Total portions/units
   - Occupied vs available portions
   - Total monthly rental income
   - Recent inquiries
3. Quick actions available:
   - Add new property
   - Add portions to existing property
   - View inquiries
   - View financial reports

#### 4.2 Property & Portion CRUD

**Available Actions:**

**Create:**
- Add new property
- Add portions to property

**Read:**
- View property details
- View portion details
- View property photos
- View inquiry history

**Update:**
- Edit property information
- Edit portion details
- Update photos
- Change portion status

**Delete:**
- Delete portion (if not occupied)
- Delete property (if no portions or all portions deleted)
- Soft delete with confirmation

---

### 5. Workman (Service Provider) Workflow

#### 5.1 Job Discovery

**Entry Point:** `/workman/jobs/`

**Process:**
1. **Workman** logs into dashboard
2. Views available jobs:
   - Location-based (nearest first)
   - Service type filtering (plumbing, cleaning, etc.)
   - Zone filtering
3. Job listings show:
   - Job title/description
   - Location (zone, area)
   - Service type required
   - Date posted
   - Apply button

#### 5.2 Job Application

**Process:**
1. Workman clicks "Apply" on job
2. Application modal opens
3. Workman can:
   - View full job details
   - Attach portfolio/credentials
   - Submit application
4. Application is sent to property owner
5. Status tracked in workman dashboard:
   - Applied
   - Under Review
   - Accepted
   - Rejected
   - Completed

#### 5.3 Profile & Skills Management

**Entry Point:** `/workman/profile/`

**Process:**
1. Workman updates profile:
   - Service types offered
   - Skills and certifications
   - Availability status
   - Service areas (zones)
   - Portfolio photos
   - Experience level
2. Profile is visible to property owners when hiring
3. Verification badges (if verified by admin)

---

### 6. Public Website Workflow (Webpages App)

#### 6.1 Homepage Visitor Journey

**Entry Point:** `/` (homepage)

**Process:**
1. Visitor lands on homepage
2. Sees hero section with property search
3. Can search properties by:
   - Zone
   - Bedrooms
   - Price range
4. Search redirects to `/property/` with filters
5. Visitor can:
   - Browse featured properties
   - View services offered
   - Read about Yellow Key
   - Contact via form
   - Subscribe to newsletter

#### 6.2 Property Search & Inquiry

**Entry Point:** `/property/`

**Process:**
1. Visitor browses property listings
2. Filters by zone, price, bedrooms
3. Clicks on property card
4. Views property details and photos
5. Views available portions
6. Clicks "Inquire" button
7. Fills inquiry form:
   - Name, email, phone
   - Message
   - Preferred contact method
8. Inquiry is saved to database
9. Property owner and realtors notified
10. Confirmation email sent to visitor

**Models:**
- `Inquire` (inquiry model)
- Linked to property and portion

#### 6.3 Contact Form Submission

**Entry Point:** `/contact/`

**Process:**
1. Visitor fills contact form
2. `Contact` model saves submission:
   - Name, email, phone
   - Subject
   - Message
   - Timestamp
3. Admin receives notification
4. Confirmation email sent to visitor
5. Admin can reply from dashboard

**Models:**
- `Contact` (contact form submissions)

#### 6.4 Newsletter Subscription

**Entry Point:** Footer on any page

**Process:**
1. Visitor enters email in newsletter form
2. `MobSubscriber` record created:
   - Email
   - Subscription date
   - Active status
3. Welcome email sent
4. User added to mailing list
5. Can unsubscribe via email link

**Models:**
- `MobSubscriber` (newsletter subscribers)

---

### 7. Help System Workflow

#### 7.1 Role-Based Help Access

**Entry Points:**
- `/help/client/` - Client help
- `/help/realtor/` - Realtor help
- `/help/workman/` - Workman help

**Process:**
1. User navigates to Help section
2. System detects user role from `Profile.roles`
3. Displays role-specific help articles:
   - Getting started guide
   - Feature tutorials
   - FAQ sections
   - Video tutorials
   - Troubleshooting guides
4. User can:
   - Search help articles
   - Watch video tutorials
   - Submit feedback
   - Vote on helpfulness

#### 7.2 Help Article Search

**Process:**
1. User enters search query
2. JavaScript searches across:
   - Article titles
   - Article content
   - Tags
3. Results displayed with highlighting
4. Popular searches suggested
5. "Was this helpful?" voting system

---

## Data Flow Diagrams

### Property Creation Flow

```
Property Owner Login
    ↓
Navigate to Add Property
    ↓
Fill PropertyForm
    ↓
Upload Photos (max 5)
    ↓
Validate Form
    ↓
Create Property_data Record
    ↓
Save Photos to media/property/
    ↓
Redirect to Property Detail
    ↓
Property Visible in Portfolio
    ↓
Property Visible to Realtors (if portions available)
```

### Inquiry Flow

```
Visitor Browses Properties
    ↓
Views Property Details
    ↓
Clicks "Inquire" Button
    ↓
Fills Inquiry Form
    ↓
Submit Inquiry
    ↓
Create Inquire Record
    ↓
Email Notification to Owner
    ↓
Email Notification to Realtors
    ↓
Inquiry Appears in Dashboards
    ↓
Realtor Contacts Customer
    ↓
Update Inquiry Status
    ↓
Close Inquiry (Deal/No Deal)
```

### Portion Rental Flow

```
Property Owner Adds Portion
    ↓
Portion Status = Available
    ↓
Portion Visible to Realtors
    ↓
Realtor Finds Tenant
    ↓
Realtor Updates Status = Occupied
    ↓
Owner Receives Notification
    ↓
Portion No Longer Listed as Available
    ↓
Financial Dashboard Updated
```

---

## Key Features & Business Rules

### 1. Role-Based Access Control

**Permissions:**
- **Property Owner (Client)**:
  - Create/edit/delete own properties
  - Manage portions for own properties
  - View inquiries for own properties
  - Access client dashboard

- **Realtor**:
  - View all available properties/portions
  - Manage inquiries (all)
  - Contact property owners
  - Access realtor dashboard
  - Generate reports

- **Workman**:
  - View job listings
  - Apply for jobs
  - Manage own profile
  - Access workman dashboard

- **Admin**:
  - Full system access
  - User management
  - Content management
  - System configuration

### 2. Property & Portion Rules

**Property:**
- Must have owner (User)
- Must have zone
- Can have 0-5 photos
- Can have multiple portions
- Cannot be deleted if has portions

**Portion:**
- Must belong to a property
- Must have status
- Can have 0-4 photos
- Status determines visibility to realtors
- Monthly rent required

### 3. Inquiry Rules

- Can be linked to property only
- Can be linked to specific portion
- Must have contact details
- Status tracking required
- Email notifications automatic

### 4. User Profile Rules

- One profile per user
- Role required
- Profile picture optional
- Contact info required for realtors/workmen
- Bio recommended

---

## API Endpoints (Future/Current)

### Authentication
```
POST   /api/auth/register/           # User registration
POST   /api/auth/login/              # User login
POST   /api/auth/logout/             # User logout
POST   /api/auth/password/reset/     # Password reset
GET    /api/auth/user/               # Current user info
```

### Properties
```
GET    /api/properties/              # List all properties
POST   /api/properties/              # Create property
GET    /api/properties/{id}/         # Property details
PUT    /api/properties/{id}/         # Update property
DELETE /api/properties/{id}/         # Delete property
GET    /api/properties/available/    # Available properties
```

### Portions
```
GET    /api/portions/                # List all portions
POST   /api/portions/                # Create portion
GET    /api/portions/{id}/           # Portion details
PUT    /api/portions/{id}/           # Update portion
DELETE /api/portions/{id}/           # Delete portion
GET    /api/portions/available/      # Available portions
```

### Inquiries
```
GET    /api/inquiries/               # List inquiries
POST   /api/inquiries/               # Create inquiry
GET    /api/inquiries/{id}/          # Inquiry details
PUT    /api/inquiries/{id}/          # Update inquiry status
DELETE /api/inquiries/{id}/          # Delete inquiry
```

### Zones
```
GET    /api/zones/                   # List all zones in Qatar
GET    /api/zones/{id}/              # Zone details
GET    /api/zones/{id}/properties/   # Properties in zone
```

---

## Database Relationships

### Core Relationships

```
User (Django Auth)
  ├─► Profile (1:1)
  │     └─► Roles (FK)
  │     └─► ProfilePicture (1:1)
  │     └─► Spoken_Languages (M2M)
  │     └─► Agent (1:1, optional)
  │
  └─► Property_data (1:N as owner)
        ├─► Zone_names (FK)
        └─► Portions (1:N)
              ├─► Portions_status (FK)
              └─► Inquire (1:N, optional)

Inquire
  ├─► Property_data (FK)
  └─► Portions (FK, optional)
```

### Key Fields

**Property_data:**
- owner (FK to User)
- property_name (CharField)
- zone_name (FK to Zone_names)
- building_no, street_no, zone_no
- property_photo_1 to property_photo_5
- created_at, updated_at

**Portions:**
- property (FK to Property_data)
- status (FK to Portions_status)
- portion_number (CharField)
- floor (IntegerField)
- bedrooms, bathrooms (IntegerField)
- area_sqm (DecimalField)
- monthly_rent (DecimalField)
- portion_photo_1 to portion_photo_4

**Inquire:**
- property (FK to Property_data)
- portion (FK to Portions, nullable)
- inquirer_name, inquirer_email, inquirer_phone
- message (TextField)
- status (CharField: pending/contacted/closed)
- created_at

---

## Email Notifications

### Automated Emails

1. **User Registration:**
   - Welcome email with account details
   - Email verification link (if enabled)

2. **New Inquiry:**
   - Email to property owner
   - Email to assigned realtors
   - Confirmation email to inquirer

3. **Inquiry Status Change:**
   - Email to inquirer when status changes
   - Email to owner when inquiry is closed

4. **Property Status Change:**
   - Email to owner when portion is rented
   - Email to realtors when new property added

5. **Newsletter:**
   - Welcome email on subscription
   - Weekly/monthly property updates

---

## Testing Checklist

### User Registration & Auth
- [ ] User can register with email/password
- [ ] User can register with Google OAuth
- [ ] Profile is created automatically
- [ ] Email verification works
- [ ] Password reset works
- [ ] User can login
- [ ] User can logout
- [ ] Session is maintained

### Property Management
- [ ] Owner can create property
- [ ] Photos upload correctly (max 5)
- [ ] Property appears in portfolio
- [ ] Owner can edit property
- [ ] Owner can delete property (if no portions)
- [ ] Zone dropdown populated correctly

### Portion Management
- [ ] Owner can add portion to property
- [ ] Photos upload correctly (max 4)
- [ ] Status updates correctly
- [ ] Available portions visible to realtors
- [ ] Occupied portions hidden from realtors
- [ ] Owner can edit portion
- [ ] Owner can delete portion

### Inquiry System
- [ ] Visitor can submit inquiry
- [ ] Email sent to owner
- [ ] Email sent to realtors
- [ ] Inquiry appears in dashboards
- [ ] Realtor can update status
- [ ] Status change emails sent
- [ ] Inquiry can be closed

### Realtor Dashboard
- [ ] Realtor sees vacant properties
- [ ] Filtering works correctly
- [ ] Realtor can view inquiries
- [ ] Realtor can manage bookings
- [ ] Statistics display correctly

### Workman System
- [ ] Workman sees job listings
- [ ] Location-based filtering works
- [ ] Workman can apply for jobs
- [ ] Application status tracked
- [ ] Profile updates correctly

### Public Website
- [ ] Homepage loads correctly
- [ ] Property search works
- [ ] Contact form submits
- [ ] Newsletter subscription works
- [ ] SEO meta tags present

---

## Performance Considerations

### Database Optimization
- Indexed fields: property_name, zone_name, status
- `select_related()` for foreign keys (owner, zone, status)
- `prefetch_related()` for reverse relationships (portions, inquiries)
- Database query optimization in views

### Caching Strategy
- Cache property listings for 15 minutes
- Cache zone list (rarely changes)
- Cache user profile for session duration
- Cache statistics for 5 minutes

### Media File Optimization
- Compress images on upload
- Generate thumbnails for listings
- Serve via CDN in production
- Lazy load images below fold

---

## Security Measures

### Authentication
- Password hashing (PBKDF2)
- Email verification (optional)
- Two-factor authentication (future)
- Session timeout

### Authorization
- Role-based permissions
- Object-level permissions (own properties only)
- CSRF protection
- XSS prevention

### Data Protection
- SQL injection prevention (ORM)
- File upload validation
- Email validation
- Phone number validation
- Sanitize user inputs

---

## Deployment Checklist

### Pre-Deployment
- [ ] All migrations applied
- [ ] Static files collected
- [ ] Media directory configured
- [ ] Environment variables set
- [ ] Database backups configured
- [ ] SSL certificate installed
- [ ] Email backend configured
- [ ] Google OAuth credentials set

### Post-Deployment
- [ ] Test all workflows
- [ ] Verify email sending
- [ ] Test file uploads
- [ ] Check mobile responsiveness
- [ ] Monitor error logs
- [ ] Set up monitoring (Sentry)
- [ ] Configure backups
- [ ] Load test critical paths

---

## Future Enhancements

### Phase 1 (Next 3 Months)
- [ ] Advanced search with maps (Leaflet.js)
- [ ] Property comparison tool
- [ ] Financial reporting dashboard
- [ ] Email notification system
- [ ] SMS notifications (Twilio)
- [ ] Multi-language support (Arabic)

### Phase 2 (6-12 Months)
- [ ] Mobile apps (iOS/Android)
- [ ] RESTful API completion
- [ ] Payment integration
- [ ] Contract generation
- [ ] Tenant portal
- [ ] Maintenance request system

### Phase 3 (12+ Months)
- [ ] AI-powered property recommendations
- [ ] Virtual property tours (360°)
- [ ] Blockchain for contracts
- [ ] Advanced analytics
- [ ] Machine learning price predictions

---

**Last Updated**: November 15, 2025
**Version**: 1.0
**Project**: Yellow Key AMRC Real Estate Platform

---

**© 2025 Yellowkey Holdings. All Rights Reserved.**
