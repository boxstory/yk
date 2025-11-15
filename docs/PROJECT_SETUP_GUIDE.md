# Yellow Key AMRC - Project Setup Guide

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Virtual Environment Setup](#virtual-environment-setup)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Database Setup](#database-setup)
7. [Running the Application](#running-the-application)
8. [Development Workflow](#development-workflow)

---

## Project Overview

**Yellow Key AMRC** is a comprehensive real estate management platform built with Django 5.1.7 for the Qatar market. The platform serves property holders, real estate agents (realtors), and service providers (workmen) with specialized dashboards and tools.

### Key Features
- **Multi-Role System**: Property owners, realtors, clients, and workmen
- **Property Management**: Complete CRUD for properties and portions (units)
- **Real Estate Collaboration**: Realtor dashboard with inquiry management
- **Service Provider Network**: Workman job listings and management
- **Public Website**: SEO-optimized pages for services and information
- **Role-Based Dashboards**: Customized interfaces for each user type

### Technology Stack
- **Backend**: Django 5.1.7 (Python 3.12.7)
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5, Font Awesome 6.6.0, vanilla JavaScript
- **Forms**: django-crispy-forms with Bootstrap5
- **Authentication**: django-allauth (Google OAuth + email)
- **API**: Django REST Framework
- **Async Tasks**: Celery

---

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python 3.12.7** (64-bit)
- **PostgreSQL 12+** (for production database)
- **Git** (for version control)
- **pip** (Python package manager)

### Recommended Software
- **VS Code** with Python extension
- **PostgreSQL GUI** (pgAdmin or DBeaver)
- **Postman** (for API testing)

---

## Virtual Environment Setup

### IMPORTANT: Always Work in Virtual Environment

**NEVER run Django commands without activating the virtual environment first!**

### Virtual Environment Locations

This project has two virtual environment options:

1. **Primary Environment**: `C:\00-web-dev\django-ykqaenv` (Production/Main)
2. **Testing Environment**: `C:\00-web-dev\django-ykenv\venvykqa` (Testing/Development)

### Windows Setup (Primary Environment)

```bash
# Navigate to the virtual environment directory
cd c:\00-web-dev\django-ykqaenv

# Activate the virtual environment
.\Scripts\activate

# You should see (django-ykqaenv) in your terminal prompt
# Example: (django-ykqaenv) C:\00-web-dev\django-ykqaenv>

# Navigate to Django project directory
cd ..\django-ykenv\yk
```

### Windows Setup (Testing Environment)

```bash
# Navigate to the project root directory
cd c:\00-web-dev\django-ykenv

# Activate the testing virtual environment
.\venvykqa\Scripts\activate

# You should see (venvykqa) in your terminal prompt
# Example: (venvykqa) C:\00-web-dev\django-ykenv\yk>

# Navigate to Django project directory
cd yk
```

### Linux/macOS Setup

```bash
# Primary environment
cd /path/to/django-ykqaenv
source bin/activate
cd ../django-ykenv/yk

# OR Testing environment
cd /path/to/django-ykenv
source venvykqa/bin/activate
cd yk
```

### Verify Virtual Environment

```bash
# Check Python version (should be 3.12.7)
python --version

# Check pip is using venv pip
where python  # Windows
which python  # Linux/macOS

# Should point to django-ykqaenv or venvykqa directory
```

### Deactivating Virtual Environment

```bash
# When you're done working
deactivate
```

---

## Installation

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd django-ykenv/yk
```

### Step 2: Activate Virtual Environment

```bash
# Windows
..\venvykqa\Scripts\activate

# Linux/macOS
source ../venvykqa/bin/activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install all project dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 4: Install Development Dependencies (Optional)

```bash
# For development and testing
pip install django-debug-toolbar pytest pytest-django black flake8
```

---

## Configuration

### Step 1: Environment Variables

Create a `.env` file in the project root (`yk/` directory):

```bash
# Navigate to project directory
cd c:\00-web-dev\django-ykenv\yk

# Create .env file (use your text editor or command)
# Windows
type nul > .env

# Linux/macOS
touch .env
```

### Step 2: Configure .env File

Edit `.env` and add the following configuration:

```env
# Django Settings
DEBUG=True
SECRET_KEY=django-insecure-your-secret-key-here-change-in-production
ALLOWED_HOSTS=127.0.0.1,localhost,yellowkey.qa,www.yellowkey.qa

# Database Configuration
ENGINE=django.db.backends.postgresql
DB_NAME=yk_db
DB_USER=ykadmin
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Email Configuration (for production)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Social Authentication (Google OAuth)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

### Step 3: Generate New Secret Key

```python
# Run in Python shell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Copy the output and paste into .env SECRET_KEY
```

---

## Database Setup

### Step 1: Install PostgreSQL

1. Download PostgreSQL from [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
2. Install with default settings
3. Remember the password you set for the `postgres` user

### Step 2: Create Database

```bash
# Open PostgreSQL command line (psql)
# Login as postgres user
psql -U postgres

# Create database
CREATE DATABASE yk_db;

# Create user
CREATE USER ykadmin WITH PASSWORD 'your_password';

# Grant privileges
GRANT ALL PRIVILEGES ON DATABASE yk_db TO ykadmin;

# Exit psql
\q
```

### Step 3: Run Migrations

```bash
# Make sure virtual environment is activated
# Navigate to project directory (where manage.py is located)
cd c:\00-web-dev\django-ykenv\yk

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# You should see output confirming migrations
```

### Step 4: Create Superuser

```bash
# Create admin user
python manage.py createsuperuser

# Follow prompts:
# Username: admin
# Email: admin@yellowkey.qa
# Password: (enter secure password)
# Password (again): (confirm password)
```

### Step 5: Collect Static Files

```bash
# Collect all static files
python manage.py collectstatic --noinput
```

---

## Running the Application

### Development Server

```bash
# Activate virtual environment (if not already activated)
# Windows
..\venvykqa\Scripts\activate

# Linux/macOS
source ../venvykqa/bin/activate

# Run development server
python manage.py runserver

# Server will start at http://127.0.0.1:8000/
```

### Access Points

- **Homepage**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Property Dashboard**: [http://127.0.0.1:8000/property/](http://127.0.0.1:8000/property/)
- **Realtor Dashboard**: [http://127.0.0.1:8000/realtor/](http://127.0.0.1:8000/realtor/)
- **Client Dashboard**: [http://127.0.0.1:8000/clients/](http://127.0.0.1:8000/clients/)

### Running Celery (Optional - for async tasks)

```bash
# In a separate terminal window
# Activate virtual environment
# Windows
..\venvykqa\Scripts\activate

# Start Celery worker
celery -A yk worker -l info

# In another terminal for Celery beat (scheduled tasks)
celery -A yk beat -l info
```

---

## Development Workflow

### Daily Workflow

#### Using Primary Environment

```bash
# 1. Activate virtual environment (Primary)
cd c:\00-web-dev\django-ykqaenv
.\Scripts\activate
cd ..\django-ykenv\yk

# 2. Pull latest changes
git pull origin master

# 3. Install any new dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start development server
python manage.py runserver

# 6. Make your changes...

# 7. Run tests
python manage.py test

# 8. Commit your changes
git add .
git commit -m "Your commit message"
git push origin master
```

#### Using Testing Environment

```bash
# 1. Activate virtual environment (Testing)
cd c:\00-web-dev\django-ykenv
.\venvykqa\Scripts\activate
cd yk

# 2-8. Same steps as above...
```

### Creating New App

```bash
# Activate virtual environment (choose one)
# Primary:
cd c:\00-web-dev\django-ykqaenv
.\Scripts\activate

# OR Testing:
cd c:\00-web-dev\django-ykenv
.\venvykqa\Scripts\activate

# Navigate to project
cd ..\django-ykenv\yk  # If using primary
cd yk                  # If using testing

# Create new Django app
python manage.py startapp app_name

# Add to INSTALLED_APPS in settings.py
# Create models, views, URLs, templates
# Run makemigrations and migrate
```

### Database Operations

```bash
# Create migrations after model changes
python manage.py makemigrations

# View SQL that will be executed
python manage.py sqlmigrate app_name migration_number

# Apply migrations
python manage.py migrate

# Reset database (CAUTION: Deletes all data)
python manage.py flush

# Create database backup
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json
```

### Shell Access

```bash
# Django shell
python manage.py shell

# Example queries
>>> from accounts.models import Profile
>>> Profile.objects.all()
>>> from property.models import Property_data
>>> Property_data.objects.filter(zone_name__zone_name='Doha')
```

---

## Common Issues & Solutions

### Issue: ModuleNotFoundError

**Solution**: Make sure virtual environment is activated
```bash
.\venvykqa\Scripts\activate  # Windows
source venvykqa/bin/activate  # Linux/macOS
```

### Issue: Database connection error

**Solution**:
1. Check PostgreSQL is running
2. Verify database credentials in `.env`
3. Test connection with `psql -U ykadmin -d yk_db`

### Issue: Static files not loading

**Solution**:
```bash
python manage.py collectstatic --clear --noinput
```

### Issue: Migration conflicts

**Solution**:
```bash
# Reset migrations (development only)
python manage.py migrate --fake app_name zero
python manage.py migrate app_name
```

---

## Next Steps

1. ✅ **Read**: [DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md) for coding standards
2. ✅ **Read**: [ARCHITECTURE.md](ARCHITECTURE.md) for project structure
3. ✅ **Read**: [VSCODE_SETUP_AND_WORKFLOW.md](VSCODE_SETUP_AND_WORKFLOW.md) for VS Code configuration
4. ✅ **Explore**: Admin panel at `/admin/`
5. ✅ **Test**: Create a property, add portions, test dashboards

---

## Support & Resources

- **Django Documentation**: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **Bootstrap 5 Docs**: [https://getbootstrap.com/docs/5.0/](https://getbootstrap.com/docs/5.0/)
- **Font Awesome Icons**: [https://fontawesome.com/icons](https://fontawesome.com/icons)
- **PostgreSQL Docs**: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)

---

**Last Updated**: November 15, 2025
**Version**: 1.0
**Maintainer**: AMRC Development Team
