# Yellow Key AMRC - Development Workflow Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Coding Standards](#coding-standards)
3. [Git Workflow](#git-workflow)
4. [Development Process](#development-process)
5. [Testing Guidelines](#testing-guidelines)
6. [Code Review Process](#code-review-process)
7. [Deployment Process](#deployment-process)

---

## Getting Started

### Daily Setup

```bash
# 1. Navigate to project directory
cd c:\00-web-dev\django-ykenv

# 2. Activate virtual environment (ALWAYS REQUIRED)
.\venvykqa\Scripts\activate      # Windows
source venvykqa/bin/activate     # Linux/macOS

# 3. Navigate to Django project
cd yk

# 4. Pull latest changes
git pull origin master

# 5. Install any new dependencies
pip install -r requirements.txt

# 6. Run migrations
python manage.py migrate

# 7. Start development server
python manage.py runserver
```

---

## Coding Standards

### Python Code Style

**Follow PEP 8** - Python Enhancement Proposal 8

#### Key Guidelines:

1. **Indentation**: 4 spaces (no tabs)
2. **Line Length**: Maximum 79 characters for code, 72 for comments
3. **Imports**: Grouped and ordered (standard library → third-party → local)
4. **Naming Conventions**:
   - `snake_case` for functions and variables
   - `PascalCase` for classes
   - `UPPER_CASE` for constants

#### Example:

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

# Constants
MAX_PROPERTY_PHOTOS = 5
DEFAULT_RENT_AMOUNT = 0

class PropertyData(models.Model):
    """
    Model representing a property listing.

    Attributes:
        owner (User): The property owner
        property_name (str): Name of the property
        created_at (datetime): When property was created
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='properties'
    )
    property_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Properties'

    def __str__(self):
        return f"{self.property_name} - {self.owner.username}"

    def get_absolute_url(self):
        """Return the canonical URL for this property."""
        return reverse('property:detail', kwargs={'pk': self.pk})
```

### Django-Specific Standards

#### Views

```python
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PropertyData
from .forms import PropertyForm

@login_required
def property_create(request):
    """
    Create a new property listing.

    GET: Display empty property creation form
    POST: Process form submission and create property
    """
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.save()

            messages.success(request, 'Property created successfully!')
            return redirect('property:detail', pk=property_obj.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PropertyForm()

    context = {
        'form': form,
        'title': 'Create Property'
    }
    return render(request, 'property/property_add.html', context)
```

#### Forms

```python
# forms.py
from django import forms
from .models import PropertyData

class PropertyForm(forms.ModelForm):
    """Form for creating and updating property listings."""

    class Meta:
        model = PropertyData
        fields = [
            'property_name',
            'zone_name',
            'building_no',
            'street_no',
            'property_photo_1',
        ]
        widgets = {
            'property_name': forms.TextInput(attrs={
                'class': 'modern-input',
                'placeholder': 'Enter property name'
            }),
            'zone_name': forms.Select(attrs={
                'class': 'modern-select'
            }),
        }
        labels = {
            'property_name': 'Property Name *',
            'zone_name': 'Zone *',
        }

    def clean_property_name(self):
        """Validate property name is not empty and unique."""
        name = self.cleaned_data.get('property_name')
        if not name or not name.strip():
            raise forms.ValidationError('Property name cannot be empty.')
        return name.strip()
```

#### URLs

```python
# urls.py
from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('', views.property_list, name='list'),
    path('add/', views.property_create, name='create'),
    path('<int:pk>/', views.property_detail, name='detail'),
    path('<int:pk>/edit/', views.property_update, name='update'),
    path('<int:pk>/delete/', views.property_delete, name='delete'),
]
```

### Template Standards

#### Template Structure

```django
{% extends 'base_dashboard.html' %}
{% load static %}

{% block title %}Property List - Yellow Key{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'property/css/property.css' %}">
{% endblock %}

{% block sidebar %}
{% include 'property/includes/property_sidebar.html' %}
{% endblock %}

{% block content %}
<div class="container-fluid py-4">
    <div class="row">
        <div class="col-12">
            <h1 class="h2 mb-4">Property Listings</h1>

            {% if messages %}
                {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
                {% endfor %}
            {% endif %}

            <!-- Content here -->
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'property/js/property.js' %}"></script>
{% endblock %}
```

### CSS Standards

#### BEM Methodology (Block Element Modifier)

```css
/* property-card.css */

/* Block */
.property-card {
    background: var(--bg-white);
    border-radius: var(--border-radius-lg);
    box-shadow: var(--shadow-md);
    transition: all var(--transition-base);
}

/* Element */
.property-card__header {
    padding: var(--space-4);
    border-bottom: 1px solid var(--border-color);
}

.property-card__title {
    font-size: var(--font-size-xl);
    font-weight: var(--font-weight-semibold);
    color: var(--text-primary);
    margin: 0;
}

.property-card__image {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.property-card__body {
    padding: var(--space-4);
}

/* Modifier */
.property-card--featured {
    border: 2px solid var(--brand-primary);
}

.property-card--vacant {
    background: var(--bg-primary-pale);
}

/* State */
.property-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}
```

#### CSS Variable Usage

```css
/* Always use CSS variables from brandkit.css */

/* ✅ GOOD */
.button {
    background: var(--brand-primary);
    color: var(--text-inverse);
    padding: var(--space-3) var(--space-6);
    border-radius: var(--border-radius-md);
}

/* ❌ BAD */
.button {
    background: #ebcb1b;
    color: #ffffff;
    padding: 12px 24px;
    border-radius: 6px;
}
```

### JavaScript Standards

#### Modern ES6+ JavaScript

```javascript
// property.js

/**
 * Property management JavaScript module
 */
(function() {
  'use strict';

  /**
   * Property card interactions
   */
  const PropertyCard = {
    init: function() {
      this.attachEventListeners();
    },

    attachEventListeners: function() {
      const cards = document.querySelectorAll('.property-card');
      cards.forEach(card => {
        card.addEventListener('click', (e) => this.handleCardClick(e));
      });
    },

    handleCardClick: function(event) {
      const card = event.currentTarget;
      const propertyId = card.dataset.propertyId;

      if (propertyId) {
        window.location.href = `/property/${propertyId}/`;
      }
    }
  };

  /**
   * Initialize when DOM is ready
   */
  document.addEventListener('DOMContentLoaded', () => {
    PropertyCard.init();
  });

})();
```

---

## Git Workflow

### Branch Strategy

**Main Branches**:
- `master` - Production-ready code
- `develop` - Integration branch for features

**Supporting Branches**:
- `feature/feature-name` - New features
- `bugfix/bug-name` - Bug fixes
- `hotfix/issue-name` - Critical production fixes

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic change)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples**:

```bash
# Good commit messages
git commit -m "feat(property): add property photo upload functionality"
git commit -m "fix(realtor): resolve dashboard statistics calculation error"
git commit -m "docs(setup): update virtual environment activation instructions"
git commit -m "refactor(accounts): optimize profile query performance"

# Bad commit messages (avoid these)
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "asdfasdf"
```

### Git Workflow Steps

#### 1. Creating a New Feature

```bash
# 1. Make sure you're on master and up to date
git checkout master
git pull origin master

# 2. Create and switch to feature branch
git checkout -b feature/property-search

# 3. Make your changes...
# Edit files, add features

# 4. Stage and commit changes
git add .
git commit -m "feat(property): add advanced search functionality with filters"

# 5. Push to remote
git push origin feature/property-search

# 6. Create Pull Request on GitHub/GitLab
```

#### 2. Updating Your Branch

```bash
# Get latest changes from master
git checkout master
git pull origin master

# Switch back to your feature branch
git checkout feature/property-search

# Merge master into your branch
git merge master

# Resolve any conflicts, then push
git push origin feature/property-search
```

#### 3. Merging to Master

```bash
# After PR is approved
git checkout master
git pull origin master
git merge feature/property-search
git push origin master

# Delete the feature branch
git branch -d feature/property-search
git push origin --delete feature/property-search
```

### Common Git Commands

```bash
# Check status
git status

# View commit history
git log --oneline --graph --all

# Discard changes in file
git checkout -- filename.py

# Unstage file
git reset HEAD filename.py

# Amend last commit (only if not pushed)
git commit --amend -m "New commit message"

# Stash changes temporarily
git stash
git stash pop

# View differences
git diff
git diff --staged
```

---

## Development Process

### Adding a New Feature

#### Step 1: Planning
1. Define feature requirements
2. Design database schema (if needed)
3. Plan URL structure
4. Sketch UI/UX

#### Step 2: Create Branch
```bash
git checkout -b feature/feature-name
```

#### Step 3: Backend Development

**A. Create/Update Models**
```python
# property/models.py
class PropertyFeature(models.Model):
    property = models.ForeignKey(PropertyData, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
```

**B. Create Migrations**
```bash
python manage.py makemigrations property
python manage.py migrate
```

**C. Create Forms**
```python
# property/forms.py
class PropertyFeatureForm(forms.ModelForm):
    class Meta:
        model = PropertyFeature
        fields = ['feature_name', 'is_available']
```

**D. Create Views**
```python
# property/views.py
@login_required
def property_feature_add(request, property_pk):
    # View logic here
    pass
```

**E. Configure URLs**
```python
# property/urls.py
path('<int:property_pk>/features/add/', views.property_feature_add, name='feature_add'),
```

#### Step 4: Frontend Development

**A. Create Template**
```django
{% extends 'base_dashboard.html' %}
<!-- Template content -->
```

**B. Add CSS**
```css
/* static/property/css/property-features.css */
.property-feature { }
```

**C. Add JavaScript**
```javascript
// static/property/js/property-features.js
```

#### Step 5: Testing
```bash
# Run tests
python manage.py test property

# Manual testing
python manage.py runserver
# Test in browser
```

#### Step 6: Commit & Push
```bash
git add .
git commit -m "feat(property): add property features management"
git push origin feature/property-features
```

### Fixing a Bug

#### Step 1: Reproduce the Bug
1. Document steps to reproduce
2. Identify affected components
3. Check error logs

#### Step 2: Create Bugfix Branch
```bash
git checkout -b bugfix/property-photo-upload
```

#### Step 3: Fix the Bug
```python
# Make necessary code changes
```

#### Step 4: Test Fix
```bash
# Verify bug is fixed
# Test related functionality
```

#### Step 5: Commit & Push
```bash
git add .
git commit -m "fix(property): resolve property photo upload validation error"
git push origin bugfix/property-photo-upload
```

---

## Testing Guidelines

### Unit Tests

```python
# property/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import PropertyData, Portions

class PropertyModelTest(TestCase):
    """Test cases for Property model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.property = PropertyData.objects.create(
            owner=self.user,
            property_name='Test Property',
            building_no='123'
        )

    def test_property_creation(self):
        """Test property is created correctly."""
        self.assertEqual(self.property.property_name, 'Test Property')
        self.assertEqual(self.property.owner, self.user)

    def test_property_str_method(self):
        """Test property string representation."""
        expected = f"Test Property - {self.user.username}"
        self.assertEqual(str(self.property), expected)
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test property

# Run specific test class
python manage.py test property.tests.PropertyModelTest

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

---

## Code Review Process

### Before Submitting PR

**Checklist**:
- [ ] Code follows PEP 8 standards
- [ ] All tests pass
- [ ] No console errors
- [ ] Documentation updated
- [ ] Migration files included (if models changed)
- [ ] No sensitive data (passwords, API keys) in code
- [ ] CSS uses brandkit variables
- [ ] JavaScript is modular and documented

### Reviewing Code

**What to Check**:
1. **Functionality**: Does it work as intended?
2. **Code Quality**: Is it readable and maintainable?
3. **Performance**: Are there any performance issues?
4. **Security**: Any security vulnerabilities?
5. **Tests**: Are there adequate tests?
6. **Documentation**: Is it well-documented?

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Refactoring
- [ ] Documentation

## Testing
- [ ] Unit tests pass
- [ ] Manual testing completed
- [ ] Browser compatibility checked

## Screenshots
(if UI changes)

## Checklist
- [ ] Code follows project standards
- [ ] Self-review completed
- [ ] Documentation updated
```

---

## Deployment Process

### Pre-Deployment Checklist

```bash
# 1. Run all tests
python manage.py test

# 2. Check for migrations
python manage.py makemigrations --check --dry-run

# 3. Collect static files
python manage.py collectstatic --noinput

# 4. Check deployment settings
python manage.py check --deploy
```

### Environment Configuration

**Production .env**:
```env
DEBUG=False
ALLOWED_HOSTS=yellowkey.qa,www.yellowkey.qa
SECRET_KEY=<strong-secret-key>
DATABASE_URL=postgres://user:pass@host:5432/dbname
```

### Deployment Steps

```bash
# 1. Pull latest code
git pull origin master

# 2. Activate virtual environment
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Collect static files
python manage.py collectstatic --noinput

# 6. Restart application server
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

---

## Best Practices

### Do's ✅
- Always work in virtual environment
- Write meaningful commit messages
- Test before committing
- Use CSS variables from brandkit.css
- Document complex logic
- Keep functions small and focused
- Use Django's built-in security features
- Validate all user inputs
- Handle errors gracefully

### Don'ts ❌
- Don't commit directly to master
- Don't commit `.env` files
- Don't hard-code sensitive data
- Don't skip migrations
- Don't use inline styles
- Don't write long functions (>50 lines)
- Don't ignore security warnings
- Don't commit commented-out code
- Don't use `print()` for debugging (use logging)

---

**Last Updated**: November 15, 2025
**Version**: 1.0
**Maintainer**: AMRC Development Team
