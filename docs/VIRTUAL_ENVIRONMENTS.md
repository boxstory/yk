# Virtual Environments Guide - Yellow Key AMRC

## Overview

This project uses **two separate virtual environments** for different purposes. This guide explains when and how to use each one.

---

## Virtual Environment Locations

### 1. Primary Environment (Production/Main)
- **Location**: `C:\00-web-dev\django-ykqaenv`
- **Purpose**: Main development and production testing
- **When to use**: Regular development work, production testing
- **Prompt indicator**: `(django-ykqaenv)`

### 2. Testing Environment (Development/Testing)
- **Location**: `C:\00-web-dev\django-ykenv\venvykqa`
- **Purpose**: Experimental features, testing, debugging
- **When to use**: Testing new packages, experimental features, debugging
- **Prompt indicator**: `(venvykqa)`

---

## Quick Reference

### Activate Primary Environment (Windows)

```bash
cd c:\00-web-dev\django-ykqaenv
.\Scripts\activate
cd ..\django-ykenv\yk
```

**Prompt will show**: `(django-ykqaenv) C:\00-web-dev\django-ykenv\yk>`

### Activate Testing Environment (Windows)

```bash
cd c:\00-web-dev\django-ykenv
.\venvykqa\Scripts\activate
cd yk
```

**Prompt will show**: `(venvykqa) C:\00-web-dev\django-ykenv\yk>`

### Activate Primary Environment (Linux/macOS)

```bash
cd /path/to/django-ykqaenv
source bin/activate
cd ../django-ykenv/yk
```

### Activate Testing Environment (Linux/macOS)

```bash
cd /path/to/django-ykenv
source venvykqa/bin/activate
cd yk
```

---

## When to Use Each Environment

### Use Primary Environment (`django-ykqaenv`) For:

✅ **Regular Development**
- Daily coding tasks
- Feature development
- Bug fixes
- Database migrations
- Git commits and pushes

✅ **Production Testing**
- Testing before deployment
- Final QA checks
- Performance testing
- Production-like environment

✅ **Stable Operations**
- Running the development server
- Creating migrations
- Collecting static files
- Admin tasks

### Use Testing Environment (`venvykqa`) For:

🧪 **Experimental Work**
- Testing new packages before adding to requirements.txt
- Trying different package versions
- Debugging package conflicts
- Prototyping new features

🧪 **Isolated Testing**
- Testing potentially breaking changes
- Experimenting with new libraries
- Package compatibility testing
- Debugging without affecting main environment

🧪 **Development Experimentation**
- Learning new Django features
- Testing third-party packages
- Code experiments
- Temporary testing

---

## Environment Setup

### Setting Up Primary Environment

```bash
# Create virtual environment (if not exists)
cd c:\00-web-dev
python -m venv django-ykqaenv

# Activate it
cd django-ykqaenv
.\Scripts\activate

# Navigate to project
cd ..\django-ykenv\yk

# Install dependencies
pip install -r requirements.txt

# Verify installation
python --version
pip list
```

### Setting Up Testing Environment

```bash
# Create virtual environment (if not exists)
cd c:\00-web-dev\django-ykenv
python -m venv venvykqa

# Activate it
.\venvykqa\Scripts\activate

# Navigate to project
cd yk

# Install dependencies
pip install -r requirements.txt

# Verify installation
python --version
pip list
```

---

## Verifying Active Environment

### Check Which Environment is Active

```bash
# Windows
where python
# Should show either:
# C:\00-web-dev\django-ykqaenv\Scripts\python.exe  (Primary)
# C:\00-web-dev\django-ykenv\venvykqa\Scripts\python.exe  (Testing)

# Linux/macOS
which python
# Should show either:
# /path/to/django-ykqaenv/bin/python  (Primary)
# /path/to/django-ykenv/venvykqa/bin/python  (Testing)
```

### Check Python Version

```bash
python --version
# Should output: Python 3.12.7
```

### Check Installed Packages

```bash
pip list
# Should show all installed packages in current environment
```

---

## Switching Between Environments

### Switch from Testing to Primary

```bash
# 1. Deactivate current environment
deactivate

# 2. Activate primary environment
cd c:\00-web-dev\django-ykqaenv
.\Scripts\activate
cd ..\django-ykenv\yk

# 3. Verify
where python  # Should point to django-ykqaenv
```

### Switch from Primary to Testing

```bash
# 1. Deactivate current environment
deactivate

# 2. Activate testing environment
cd c:\00-web-dev\django-ykenv
.\venvykqa\Scripts\activate
cd yk

# 3. Verify
where python  # Should point to venvykqa
```

---

## Common Commands

### Installing Packages

```bash
# In PRIMARY environment (for production):
pip install package-name
pip freeze > requirements.txt  # Update requirements

# In TESTING environment (for testing only):
pip install package-name
# Do NOT update requirements.txt unless tested and confirmed
```

### Updating Requirements

```bash
# Only do this in PRIMARY environment after testing!
pip freeze > requirements.txt

# Then sync to testing environment:
# Deactivate, switch to testing, then:
pip install -r requirements.txt
```

### Running Django Commands

```bash
# Both environments (make sure correct one is active first):
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py collectstatic
python manage.py test
```

---

## Best Practices

### ✅ DO:

1. **Always activate environment before running Django commands**
   ```bash
   # WRONG:
   python manage.py runserver  # No environment active!

   # RIGHT:
   .\Scripts\activate  # Activate first
   python manage.py runserver
   ```

2. **Use primary environment for daily work**
   - Regular feature development
   - Bug fixes
   - Commits and deployments

3. **Use testing environment for experiments**
   - New package testing
   - Debugging package conflicts
   - Learning and prototyping

4. **Verify active environment before major operations**
   ```bash
   where python  # Check which environment is active
   ```

5. **Keep both environments in sync**
   ```bash
   # After updating primary, sync to testing:
   pip install -r requirements.txt
   ```

### ❌ DON'T:

1. **Don't mix environments**
   - Install production packages only in primary
   - Test packages only in testing environment first

2. **Don't forget to activate**
   - Always check prompt shows `(environment-name)`
   - Verify with `where python`

3. **Don't update requirements.txt from testing environment**
   - Only update requirements.txt from primary environment
   - After packages are tested and confirmed working

4. **Don't commit without testing in primary**
   - Test in testing environment first
   - Verify in primary environment
   - Then commit and push

---

## Troubleshooting

### Issue: "Python not found" or "pip not found"

**Solution**: Environment not activated

```bash
# Activate environment first:
cd c:\00-web-dev\django-ykqaenv
.\Scripts\activate
```

### Issue: "Module not found" error

**Solution**: Package not installed in current environment

```bash
# Check which environment is active
where python

# Install missing package
pip install package-name

# Or reinstall all requirements
pip install -r requirements.txt
```

### Issue: Wrong environment activated

**Solution**: Deactivate and activate correct one

```bash
deactivate
cd c:\00-web-dev\django-ykqaenv  # For primary
.\Scripts\activate
```

### Issue: Packages out of sync between environments

**Solution**: Sync both environments

```bash
# In primary environment:
pip freeze > requirements.txt

# Switch to testing environment:
deactivate
cd c:\00-web-dev\django-ykenv
.\venvykqa\Scripts\activate
pip install -r requirements.txt
```

### Issue: Can't remember which environment to use

**Quick Decision Tree**:
- Regular development? → **Primary** (`django-ykqaenv`)
- Testing new package? → **Testing** (`venvykqa`)
- Committing code? → **Primary** (`django-ykqaenv`)
- Experimenting? → **Testing** (`venvykqa`)
- Production testing? → **Primary** (`django-ykqaenv`)
- Debugging package issue? → **Testing** (`venvykqa`)

---

## Environment Comparison

| Feature | Primary (django-ykqaenv) | Testing (venvykqa) |
|---------|--------------------------|---------------------|
| **Purpose** | Production/Main development | Testing/Experimentation |
| **Stability** | Stable, production-ready | Experimental |
| **Requirements** | Synced with requirements.txt | May have extra packages |
| **Updates** | Careful, tested updates | Frequent, experimental |
| **Git Commits** | ✅ Yes, from here | ❌ No, test first |
| **New Packages** | After testing only | ✅ Yes, test here first |
| **Daily Work** | ✅ Primary choice | Occasional use |
| **Risk Level** | Low (stable) | Higher (experimental) |

---

## Quick Checklist

Before starting work:

- [ ] Virtual environment activated?
- [ ] Correct environment for task (primary vs testing)?
- [ ] Prompt shows environment name?
- [ ] `where python` points to correct location?
- [ ] In correct project directory (`yk/`)?

Before committing:

- [ ] Working in PRIMARY environment?
- [ ] All packages in requirements.txt?
- [ ] Tests pass?
- [ ] Migrations created and applied?
- [ ] Code works in primary environment?

---

## Summary

**Primary Environment** (`django-ykqaenv`):
- Main development
- Production testing
- Git commits
- Stable operations

**Testing Environment** (`venvykqa`):
- Package testing
- Experiments
- Debugging
- Learning

**Remember**: Always activate the environment before running any Django commands!

---

**Last Updated**: November 15, 2025
**Version**: 1.0

---

**© 2025 Yellowkey Holdings. All Rights Reserved.**
