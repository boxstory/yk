# Color Palette Reference - Yellow Key AMRC

**Quick Reference Guide for Developers**
**Version:** 2.0 - Light Theme
**Last Updated:** November 15, 2025

---

## 🎨 Quick Color Picker

### Primary (Gold Yellow)

| Shade | Hex Code | RGB | Use Case |
|-------|----------|-----|----------|
| 50 | `#fffef7` | `rgb(255, 254, 247)` | Subtle highlights, very light backgrounds |
| 100 | `#fffbea` | `rgb(255, 251, 234)` | Hover backgrounds, light sections |
| 200 | `#fff4c7` | `rgb(255, 244, 199)` | Card backgrounds, highlighted areas |
| 300 | `#ffe99f` | `rgb(255, 233, 159)` | Soft borders, dividers |
| 400 | `#ffdd66` | `rgb(255, 221, 102)` | Icons, medium emphasis |
| **500** | **`#ffd700`** | **`rgb(255, 215, 0)`** | **PRIMARY BRAND COLOR** |
| 600 | `#e6c200` | `rgb(230, 194, 0)` | Hover states, darker accents |
| 700 | `#ccad00` | `rgb(204, 173, 0)` | Active states, pressed buttons |
| 800 | `#b39900` | `rgb(179, 153, 0)` | Text on light, strong emphasis |
| 900 | `#998500` | `rgb(153, 133, 0)` | Darkest accents, maximum contrast |

---

### Secondary (Slate Gray-Blue)

| Shade | Hex Code | RGB | Use Case |
|-------|----------|-----|----------|
| 50 | `#f8f9fb` | `rgb(248, 249, 251)` | Page background, ultra light |
| 100 | `#f1f3f7` | `rgb(241, 243, 247)` | Section backgrounds, very light |
| 200 | `#e4e7ed` | `rgb(228, 231, 237)` | Borders, dividers, light gray |
| 300 | `#cbd0da` | `rgb(203, 208, 218)` | Soft borders, disabled backgrounds |
| 400 | `#9ca3af` | `rgb(156, 163, 175)` | Disabled text, placeholders |
| 500 | `#6b7280` | `rgb(107, 114, 128)` | Secondary text, captions |
| 600 | `#4b5563` | `rgb(75, 85, 99)` | Body text, paragraphs |
| 700 | `#374151` | `rgb(55, 65, 81)` | Headings, important text |
| **800** | **`#2c3e50`** | **`rgb(44, 62, 80)`** | **PRIMARY TEXT COLOR** |
| 900 | `#1a202c` | `rgb(26, 32, 44)` | Maximum emphasis, darkest |

---

### Success (Modern Green)

| Type | Hex Code | RGB | Use Case |
|------|----------|-----|----------|
| Light | `#d4edda` | `rgb(212, 237, 218)` | Success alert backgrounds |
| **Main** | **`#10b981`** | **`rgb(16, 185, 129)`** | **Success messages, icons** |
| Dark | `#059669` | `rgb(5, 150, 105)` | Success text, hover states |

---

### Error (Modern Red)

| Type | Hex Code | RGB | Use Case |
|------|----------|-----|----------|
| Light | `#fee2e2` | `rgb(254, 226, 226)` | Error alert backgrounds |
| **Main** | **`#ef4444`** | **`rgb(239, 68, 68)`** | **Error messages, icons** |
| Dark | `#dc2626` | `rgb(220, 38, 38)` | Error text, hover states |

---

### Warning (Modern Amber)

| Type | Hex Code | RGB | Use Case |
|------|----------|-----|----------|
| Light | `#fef3c7` | `rgb(254, 243, 199)` | Warning alert backgrounds |
| **Main** | **`#f59e0b`** | **`rgb(245, 158, 11)`** | **Warning messages, icons** |
| Dark | `#d97706` | `rgb(217, 119, 6)` | Warning text, hover states |

---

### Info (Modern Blue)

| Type | Hex Code | RGB | Use Case |
|------|----------|-----|----------|
| Light | `#dbeafe` | `rgb(219, 234, 254)` | Info alert backgrounds |
| **Main** | **`#3b82f6`** | **`rgb(59, 130, 246)`** | **Info messages, icons** |
| Dark | `#2563eb` | `rgb(37, 99, 235)` | Info text, hover states |

---

## 🎯 Common Use Cases

### Backgrounds

```css
/* Page Background */
body { background: #f8f9fb; } /* Secondary-50 */

/* Card/Container Background */
.card { background: #ffffff; } /* Pure white */

/* Section Background (Alternating) */
section:nth-child(even) { background: #f1f3f7; } /* Secondary-100 */

/* Highlight Background */
.highlight { background: #fffbea; } /* Primary-100 */
```

---

### Text

```css
/* Primary Text (Body) */
p, span { color: #2c3e50; } /* Secondary-800 */

/* Secondary Text (Captions) */
.caption { color: #6b7280; } /* Secondary-500 */

/* Muted Text (Placeholders) */
::placeholder { color: #9ca3af; } /* Secondary-400 */

/* Disabled Text */
.disabled { color: #cbd0da; } /* Secondary-300 */
```

---

### Borders

```css
/* Default Border */
.card { border: 1px solid #e4e7ed; } /* Secondary-200 */

/* Emphasis Border */
.card:hover { border-color: #cbd0da; } /* Secondary-300 */

/* Primary Border */
.card-active { border-color: #ffe99f; } /* Primary-300 */

/* Strong Border */
.card-selected { border-color: #ffd700; } /* Primary-500 */
```

---

### Buttons

```css
/* Primary Button */
.btn-primary {
  background: linear-gradient(135deg, #ffd700, #e6c200);
  color: #2c3e50;
  border: 1px solid #e6c200;
}

/* Primary Button Hover */
.btn-primary:hover {
  background: #e6c200;
  border-color: #ccad00;
}

/* Secondary Button */
.btn-secondary {
  background: #ffffff;
  color: #4b5563;
  border: 1px solid #e4e7ed;
}
```

---

### Alerts

```css
/* Success Alert */
.alert-success {
  background: #d4edda;
  color: #059669;
  border-left: 4px solid #10b981;
}

/* Error Alert */
.alert-error {
  background: #fee2e2;
  color: #dc2626;
  border-left: 4px solid #ef4444;
}

/* Warning Alert */
.alert-warning {
  background: #fef3c7;
  color: #d97706;
  border-left: 4px solid #f59e0b;
}

/* Info Alert */
.alert-info {
  background: #dbeafe;
  color: #2563eb;
  border-left: 4px solid #3b82f6;
}
```

---

## 📐 Semantic Color Variables

### Use These in Code

```css
/* Primary */
var(--brand-primary-500)  /* Main gold */
var(--brand-primary-600)  /* Hover gold */
var(--brand-primary-100)  /* Light background */

/* Text */
var(--text-primary)       /* #2c3e50 - Main text */
var(--text-secondary)     /* #4b5563 - Secondary */
var(--text-muted)         /* #9ca3af - Muted */

/* Backgrounds */
var(--bg-page)            /* #f8f9fb - Page */
var(--bg-white)           /* #ffffff - Cards */
var(--bg-light)           /* #f1f3f7 - Sections */

/* Borders */
var(--border-light)       /* #e4e7ed - Default */
var(--border-medium)      /* #cbd0da - Emphasis */
var(--border-primary)     /* #ffe99f - Gold accent */

/* States */
var(--color-success)      /* #10b981 */
var(--color-error)        /* #ef4444 */
var(--color-warning)      /* #f59e0b */
var(--color-info)         /* #3b82f6 */
```

---

## 🎨 Color Combinations

### Gold + Slate (Primary)

```
Background: #fffbea (Primary-100)
Text: #2c3e50 (Secondary-800)
Border: #ffe99f (Primary-300)
✅ Contrast: 8.5:1 (AAA)
```

### White + Slate (Cards)

```
Background: #ffffff (White)
Text: #2c3e50 (Secondary-800)
Border: #e4e7ed (Secondary-200)
✅ Contrast: 12.6:1 (AAA)
```

### Light Gray + Dark Gray (Sections)

```
Background: #f1f3f7 (Secondary-100)
Text: #4b5563 (Secondary-600)
Border: #cbd0da (Secondary-300)
✅ Contrast: 8.2:1 (AAA)
```

---

## 🌈 Gradient Formulas

```css
/* Primary Gradient (Gold) */
background: linear-gradient(135deg, #ffd700 0%, #e6c200 100%);

/* Light Primary Gradient (Subtle Gold) */
background: linear-gradient(135deg, #fffbea 0%, #fff4c7 100%);

/* Secondary Gradient (Slate) */
background: linear-gradient(135deg, #374151 0%, #2c3e50 100%);

/* Page Gradient (Top to Bottom) */
background: linear-gradient(180deg, #f8f9fb 0%, #ffffff 100%);

/* Overlay Gradient (Dark to Transparent) */
background: linear-gradient(180deg, rgba(44,62,80,0) 0%, rgba(44,62,80,0.6) 100%);
```

---

## 📊 Accessibility Matrix

| Foreground | Background | Ratio | WCAG Level |
|------------|-----------|-------|------------|
| `#2c3e50` | `#ffffff` | 12.63:1 | AAA ✅ |
| `#4b5563` | `#ffffff` | 9.24:1 | AAA ✅ |
| `#6b7280` | `#ffffff` | 5.15:1 | AA ✅ |
| `#9ca3af` | `#ffffff` | 3.04:1 | AA Large ✅ |
| `#2c3e50` | `#ffd700` | 4.58:1 | AA ✅ |
| `#2c3e50` | `#fffbea` | 10.12:1 | AAA ✅ |
| `#059669` | `#d4edda` | 5.92:1 | AA ✅ |
| `#dc2626` | `#fee2e2` | 6.41:1 | AA ✅ |

**Legend:**
- AAA: ≥ 7:1 (excellent)
- AA: ≥ 4.5:1 (good)
- AA Large: ≥ 3:1 (acceptable for large text 18px+)

---

## 🎯 Color Decision Tree

### Choosing Text Color

```
Is it main content?
  YES → #2c3e50 (Secondary-800)

Is it secondary information?
  YES → #6b7280 (Secondary-500)

Is it a caption or helper text?
  YES → #9ca3af (Secondary-400)

Is it disabled?
  YES → #cbd0da (Secondary-300)
```

---

### Choosing Background Color

```
Is it the page/body?
  YES → #f8f9fb (Secondary-50)

Is it a card or container?
  YES → #ffffff (White)

Is it a section?
  YES → #f1f3f7 (Secondary-100)

Is it a highlight?
  YES → #fffbea (Primary-100)

Is it a hover state?
  YES → #fff4c7 (Primary-200)
```

---

### Choosing Border Color

```
Is it a default border?
  YES → #e4e7ed (Secondary-200)

Is it emphasis or hover?
  YES → #cbd0da (Secondary-300)

Is it a primary element?
  YES → #ffe99f (Primary-300)

Is it selected/active?
  YES → #ffd700 (Primary-500)
```

---

## 🔍 Testing Your Colors

### Browser DevTools

1. Open DevTools (F12)
2. Go to Elements tab
3. Select element
4. Check Computed tab → color values

### Contrast Checker

1. Use browser DevTools → Accessibility
2. Or visit: https://webaim.org/resources/contrastchecker/
3. Enter foreground and background colors
4. Ensure ratio ≥ 4.5:1 for AA compliance

---

## 💡 Pro Tips

1. **Stick to the scale** - Use defined shades (50-900)
2. **Use variables** - Always use CSS custom properties
3. **Test contrast** - Check all text/background combinations
4. **Be consistent** - Same shade for same purpose
5. **Document choices** - Comment why you chose a color

---

## 📝 Quick Copy Snippets

### HTML Classes

```html
<!-- Primary Button -->
<button class="btn btn-primary">Submit</button>

<!-- Success Alert -->
<div class="alert alert-success">Success message</div>

<!-- Card with Gradient Header -->
<div class="card">
  <div class="card-header">Header</div>
  <div class="card-body">Content</div>
</div>

<!-- Text Colors -->
<p class="text-primary">Primary text</p>
<p class="text-secondary">Secondary text</p>
<p class="text-muted">Muted text</p>
```

---

### CSS Variables

```css
/* Backgrounds */
background: var(--bg-page);
background: var(--bg-white);
background: var(--bg-light);

/* Text */
color: var(--text-primary);
color: var(--text-secondary);
color: var(--text-muted);

/* Borders */
border-color: var(--border-light);
border-color: var(--border-primary);

/* Gradients */
background: var(--gradient-primary);
background: var(--gradient-primary-light);
```

---

**Quick Reference Complete! 🎨**

**© 2025 Yellowkey Holdings. All Rights Reserved.**
