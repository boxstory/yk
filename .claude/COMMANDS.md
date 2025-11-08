# Claude Code Quick Commands for Yellowkey Project

## Project Architecture Commands

### Review Project Structure
```
Review .claude/PROJECT_ARCHITECTURE.md
```

### Understand App Workflow
```
Explain the [property listing/tenant management/lead generation] workflow from PROJECT_ARCHITECTURE.md
```

### Check Database Schema
```
Show me the database schema for [property/accounts/webpages] from PROJECT_ARCHITECTURE.md
```

### Understand User Roles
```
Explain user roles and permissions from PROJECT_ARCHITECTURE.md
```

### Find Feature Implementation
```
How is [feature name] implemented? Check PROJECT_ARCHITECTURE.md
```

---

## SEO Documentation Commands

### Update SEO Guide
```
Update .claude/SEO_OPTIMIZATION_GUIDE.md with today's changes
```

### Review Current SEO Status
```
Review our SEO implementation from .claude/SEO_OPTIMIZATION_GUIDE.md
```

### Check What Changed
```
What files have changed since last commit? Do any impact SEO?
```

### Quick Audit
```
Audit our SEO setup and tell me what needs updating
```

### Add New Keywords
```
Add these keywords to our SEO: [list keywords]
Then update the guide
```

### Test Schemas
```
Check if our structured data schemas are still valid
```

---

## Development Workflow with SEO Updates

### 1. After Making Template Changes
```bash
# In Claude Code chat:
"I updated [template files]. Update SEO docs with changes"
```

### 2. Before Committing Code
```bash
# In Claude Code chat:
"Check if .claude/SEO_OPTIMIZATION_GUIDE.md needs updates before I commit"
```

### 3. After Deployment
```bash
# In Claude Code chat:
"Mark deployment date in SEO guide and update version"
```

### 4. Weekly Review
```bash
# In Claude Code chat:
"It's Monday - do a full SEO docs review and update"
```

---

## Common Update Scenarios

### Scenario 1: Added New Service Page
```
I added a new service page at [path].
1. Add appropriate meta tags
2. Add FAQ schema
3. Update SEO guide with this new page
```

### Scenario 2: Changed Keywords
```
I want to target these new keywords: [list]
1. Add them to head.html
2. Update all relevant pages
3. Document in SEO guide
```

### Scenario 3: Modified Structured Data
```
I changed the LocalBusiness schema in head.html
Update the SEO guide to reflect these changes
```

### Scenario 4: New Area Coverage
```
We now serve [new area in Qatar]
1. Add to areaServed in schema
2. Add location keywords
3. Update SEO guide
```

---

## Automation Tips

### VS Code Settings (Optional)
You can set up VS Code to remind you. Add to `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Remind: Update SEO Docs",
      "type": "shell",
      "command": "echo",
      "args": ["⚠️  Remember to ask Claude: 'Update SEO docs'"],
      "presentation": {
        "echo": true,
        "reveal": "always",
        "panel": "new"
      }
    }
  ]
}
```

### Git Commit Template (Optional)
Create `.gitmessage` in project root:

```
# Commit message
#
# Before committing, did you:
# [ ] Ask Claude to update SEO docs if needed?
# [ ] Test structured data if meta tags changed?
# [ ] Update dateModified in Article schema?
```

Then run:
```bash
git config commit.template .gitmessage
```

---

## Monthly Checklist

Copy this to chat with Claude on the 1st of each month:

```
Monthly SEO Documentation Review:

1. Check .claude/SEO_OPTIMIZATION_GUIDE.md is up to date
2. Verify all keywords are still relevant
3. Test structured data at https://search.google.com/test/rich-results
4. Update dateModified in Article schemas
5. Review "Last Updated" dates
6. Check if new competitors have emerged
7. Update future enhancements roadmap
8. Version the documentation (add Month/Year entry)

Please review and update accordingly.
```

---

## Quick Reference

| When | Command |
|------|---------|
| After any template change | "Update SEO docs with template changes" |
| Before git commit | "Check if SEO docs need updating" |
| Added new page | "Document new page in SEO guide" |
| Changed keywords | "Update keyword documentation" |
| Modified schema | "Document schema changes" |
| Weekly | "Review and update SEO guide" |
| Monthly | "Full SEO audit and guide update" |
| Before deployment | "Final SEO docs check before deploy" |

---

**Remember**: The more you update the documentation, the better Claude can help you maintain and improve your SEO over time!
