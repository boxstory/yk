# CSS Loading Order - Critical Documentation

**Yellow Key AMRC Real Estate Platform**
**Last Updated:** November 15, 2025

---

## 🎨 CSS Cascade Strategy

The Yellow Key platform uses a **three-layer CSS architecture** to ensure brand consistency while leveraging Bootstrap's utility framework:

```
Layer 1: brandkit.css (CSS Variables & Design Tokens)
   ↓
Layer 2: Bootstrap 5 (Third-party Framework)
   ↓
Layer 3: brandkit-overrides.css (Force Brand Styles)
```

---

## 📋 Critical Load Order

### ⚠️ IMPORTANT: Load Order Cannot Be Changed

The CSS files **MUST** load in this exact order in `templates/includes/head.html`:

```html
<!-- 1. BRANDKIT.CSS - Must be loaded FIRST -->
<link rel="stylesheet" href="{% static 'assets/css/brandkit.css' %}">

<!-- 2. Bootstrap 5 - Base framework -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
      rel="stylesheet">

<!-- 2b. BRANDKIT OVERRIDES - Force brandkit styles over Bootstrap (CRITICAL!) -->
<link rel="stylesheet" href="{% static 'assets/css/brandkit-overrides.css' %}">

<!-- 3. Font Awesome, Bootstrap Icons, etc. -->
<!-- 4. Application-specific CSS (webpages/css/main.css, etc.) -->
```

---

## 🔍 Why This Order Matters

### Layer 1: brandkit.css (Foundation)
**Purpose:** Define CSS custom properties (variables) that other files can reference

**Contains:**
- CSS Custom Properties (`--brand-primary`, `--space-4`, etc.)
- Design tokens (colors, spacing, typography)
- No actual styling rules (just variables)

**Why First:** Other CSS files reference these variables, so they must be defined first

**Example:**
```css
:root {
  --brand-primary: #ebcb1b;
  --brand-secondary: #232c3d;
  --space-4: 1rem;
  --border-radius-md: 8px;
}
```

---

### Layer 2: Bootstrap 5 (Framework)
**Purpose:** Provide base CSS framework and utility classes

**Contains:**
- Grid system, flexbox utilities
- Component styles (buttons, cards, modals)
- Typography, spacing utilities
- Bootstrap's own CSS variables

**Why Second:** Needs to load after brandkit.css variables are defined

**Problem:** Bootstrap's styles will override our brand colors because they have higher specificity

**Example Bootstrap Override:**
```css
/* Bootstrap defines its own primary color */
.btn-primary {
  background-color: #0d6efd; /* Bootstrap blue - NOT our yellow! */
}
```

---

### Layer 3: brandkit-overrides.css (Enforcement)
**Purpose:** Force brandkit styles over Bootstrap using `!important` and higher specificity

**Contains:**
- Overrides for all Bootstrap components
- Uses `!important` to win CSS specificity battles
- Ensures brand consistency across all elements

**Why Third:** Must load AFTER Bootstrap to override its styles

**How It Works:**
```css
/* Override Bootstrap's primary color with our brand yellow */
.btn-primary {
  background-color: var(--brand-primary) !important; /* #ebcb1b - our yellow! */
  border-color: var(--brand-primary) !important;
  color: var(--brand-secondary) !important;
}

.btn-primary:hover {
  background-color: var(--brand-primary-dark) !important;
}
```

---

## 🎯 What Gets Overridden

The `brandkit-overrides.css` file forces brand consistency on:

### Colors
- ✅ Primary (yellow: #ebcb1b)
- ✅ Secondary (navy: #232c3d)
- ✅ Success, Warning, Danger, Info
- ✅ Text colors
- ✅ Background colors

### Typography
- ✅ Font family (Poppins everywhere)
- ✅ Heading styles (h1-h6)
- ✅ Font weights
- ✅ Text colors

### Components
- ✅ Buttons (all variants)
- ✅ Forms (inputs, selects, labels)
- ✅ Cards
- ✅ Modals
- ✅ Alerts
- ✅ Navbar
- ✅ Dropdowns
- ✅ Tables
- ✅ Badges
- ✅ Pagination
- ✅ Breadcrumbs
- ✅ Progress bars
- ✅ Tooltips & Popovers

### Layout
- ✅ Border radius (consistent rounded corners)
- ✅ Shadows (elevation system)
- ✅ Spacing (using our 8px grid)
- ✅ Transitions (smooth animations)

---

## 🚫 Common Mistakes to Avoid

### ❌ WRONG: Loading brandkit-overrides before Bootstrap
```html
<!-- WRONG ORDER! -->
<link rel="stylesheet" href="brandkit.css">
<link rel="stylesheet" href="brandkit-overrides.css"> <!-- Too early! -->
<link rel="stylesheet" href="bootstrap.min.css">
```
**Result:** Bootstrap will override our brand styles

---

### ❌ WRONG: Not loading brandkit-overrides at all
```html
<!-- MISSING OVERRIDES! -->
<link rel="stylesheet" href="brandkit.css">
<link rel="stylesheet" href="bootstrap.min.css">
<!-- Missing: brandkit-overrides.css -->
```
**Result:** Bootstrap blue buttons instead of yellow

---

### ❌ WRONG: Loading app CSS before overrides
```html
<!-- WRONG ORDER! -->
<link rel="stylesheet" href="brandkit.css">
<link rel="stylesheet" href="bootstrap.min.css">
<link rel="stylesheet" href="main.css"> <!-- App CSS too early! -->
<link rel="stylesheet" href="brandkit-overrides.css">
```
**Result:** App CSS might be overridden by brandkit-overrides

---

### ✅ CORRECT: Proper load order
```html
<!-- CORRECT ORDER! -->
<link rel="stylesheet" href="brandkit.css">           <!-- 1. Variables -->
<link rel="stylesheet" href="bootstrap.min.css">      <!-- 2. Framework -->
<link rel="stylesheet" href="brandkit-overrides.css"> <!-- 3. Overrides -->
<link rel="stylesheet" href="main.css">               <!-- 4. App CSS -->
```

---

## 📊 CSS Specificity Rules

### Understanding CSS Specificity
CSS applies styles based on specificity. Higher specificity wins:

1. **Inline styles:** `<div style="color: red">` (Highest)
2. **IDs:** `#header { }` (1-0-0)
3. **Classes, attributes, pseudo-classes:** `.btn { }` (0-1-0)
4. **Elements, pseudo-elements:** `div { }` (0-0-1)
5. **!important:** Overrides everything (Use sparingly!)

### Why We Use !important
```css
/* Without !important - Bootstrap might win */
.btn-primary {
  background-color: var(--brand-primary); /* Might be overridden */
}

/* With !important - We always win */
.btn-primary {
  background-color: var(--brand-primary) !important; /* Always applied */
}
```

**Trade-off:** `!important` is generally discouraged, but necessary when:
- Overriding third-party frameworks (like Bootstrap)
- Ensuring brand consistency across entire platform
- No control over third-party CSS specificity

---

## 🧪 Testing CSS Load Order

### Visual Test Checklist

1. **Primary Button Color**
   ```html
   <button class="btn btn-primary">Click Me</button>
   ```
   ✅ Should be yellow (#ebcb1b), NOT Bootstrap blue (#0d6efd)

2. **Typography**
   ```html
   <h1>Heading</h1>
   <p>Paragraph text</p>
   ```
   ✅ Should use Poppins font, NOT system default

3. **Form Controls**
   ```html
   <input class="form-control" type="text">
   ```
   ✅ Should have yellow focus border, NOT Bootstrap blue

4. **Cards**
   ```html
   <div class="card">...</div>
   ```
   ✅ Should have brandkit shadows and border radius

### Browser DevTools Test

1. Open Chrome/Firefox DevTools (F12)
2. Go to "Network" tab
3. Refresh page
4. Check CSS load order:
   - `brandkit.css` (loads first)
   - `bootstrap.min.css` (loads second)
   - `brandkit-overrides.css` (loads third)
   - Other CSS files (load after)

5. Go to "Elements" tab
6. Inspect a `.btn-primary` button
7. Check "Computed" styles:
   - `background-color` should be `rgb(235, 203, 27)` (yellow)
   - NOT `rgb(13, 110, 253)` (Bootstrap blue)

---

## 🔧 Troubleshooting

### Problem: Buttons are blue instead of yellow

**Cause:** brandkit-overrides.css not loading or loading before Bootstrap

**Fix:**
1. Check `head.html` load order
2. Verify `brandkit-overrides.css` exists in `static/assets/css/`
3. Clear browser cache (Ctrl+Shift+R)
4. Run `python manage.py collectstatic` if in production

---

### Problem: Custom CSS variables not working

**Cause:** brandkit.css not loading first

**Fix:**
1. Ensure brandkit.css loads before ALL other CSS
2. Check browser console for 404 errors
3. Verify path: `{% static 'assets/css/brandkit.css' %}`

---

### Problem: Fonts not applying

**Cause:** Google Fonts loading before brandkit-overrides.css

**Fix:**
1. Google Fonts can load anywhere (only provides font files)
2. brandkit-overrides.css applies font-family with !important
3. Check browser DevTools → Computed → font-family

---

## 📁 File Locations

```
static/
└── assets/
    └── css/
        ├── brandkit.css              (700+ lines - CSS variables)
        └── brandkit-overrides.css    (600+ lines - Bootstrap overrides)

templates/
└── includes/
    └── head.html                     (Critical CSS load order)
```

---

## 🎨 Color Reference

### Primary Colors (Always Use These!)

```css
--brand-primary: #ebcb1b;           /* Yellow Key Gold */
--brand-primary-dark: #e4ac14;      /* Darker Yellow (hover) */
--brand-primary-light: #f5e07e;     /* Light Yellow (backgrounds) */
--brand-primary-pale: #fef9e7;      /* Pale Yellow (subtle) */

--brand-secondary: #232c3d;         /* Dark Navy */
--brand-secondary-light: #727982;   /* Medium Gray */
--brand-secondary-pale: #e8eaed;    /* Light Gray */
```

### Bootstrap Color Mapping

```css
/* Bootstrap's primary → Our yellow */
.btn-primary       → background: #ebcb1b (yellow)
.bg-primary        → background: #ebcb1b (yellow)
.text-primary      → color: #ebcb1b (yellow)
.border-primary    → border-color: #ebcb1b (yellow)

/* Bootstrap's secondary → Our navy */
.btn-secondary     → background: #232c3d (navy)
.bg-secondary      → background: #232c3d (navy)
.text-secondary    → color: #232c3d (navy)
```

---

## 📝 Developer Guidelines

### When Adding New CSS

1. **Never modify Bootstrap directly** (use CDN version)
2. **Add overrides to brandkit-overrides.css**
3. **Use CSS variables from brandkit.css**
4. **Test on all browsers** (Chrome, Firefox, Safari, Edge)
5. **Check mobile responsiveness**

### Example: Adding a New Button Style

```css
/* ❌ WRONG: Don't create a new file */
/* custom-buttons.css */
.my-button {
  background: #ebcb1b;
}

/* ✅ CORRECT: Add to brandkit-overrides.css */
/* brandkit-overrides.css */
.btn-custom {
  background-color: var(--brand-primary) !important;
  color: var(--brand-secondary) !important;
  border-radius: var(--border-radius-md) !important;
}
```

---

## 🚀 Performance Considerations

### Load Order Impact on Performance

1. **brandkit.css (1-2KB)** - Fast, small file
2. **Bootstrap (25KB gzipped)** - CDN cached, fast
3. **brandkit-overrides.css (5-8KB)** - Reasonable size

**Total:** ~30-35KB CSS (acceptable for modern websites)

### Optimization Tips

- ✅ Use CDN for Bootstrap (cached by many sites)
- ✅ Minify brandkit files in production
- ✅ Enable gzip compression on server
- ✅ Use HTTP/2 for parallel loading
- ✅ Consider critical CSS for above-the-fold content

---

## 📚 Additional Resources

- [CSS Specificity Calculator](https://specificity.keegan.st/)
- [MDN: CSS Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)
- [CSS Variables Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

---

## ✅ Checklist for New Developers

Before deploying CSS changes:

- [ ] Verified CSS load order in `head.html`
- [ ] Tested primary button color (should be yellow)
- [ ] Tested font family (should be Poppins)
- [ ] Tested form focus states (should be yellow border)
- [ ] Tested on Chrome, Firefox, Safari
- [ ] Tested on mobile (responsive design)
- [ ] Cleared browser cache
- [ ] Ran `collectstatic` if production
- [ ] Checked browser console for errors
- [ ] Verified all overrides apply with `!important`

---

**© 2025 Yellowkey Holdings. All Rights Reserved.**
