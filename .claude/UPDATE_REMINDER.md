# Auto-Update SEO Documentation Reminder

## How to Keep SEO Documentation Updated

Whenever you make changes to your codebase, simply ask Claude:

```
"Update .claude/SEO_OPTIMIZATION_GUIDE.md with today's changes"
```

Claude will:
1. Check what files you modified
2. Review if any changes impact SEO
3. Update the documentation with:
   - New "Last Updated" date
   - Any new keywords added
   - Schema changes
   - File modifications
   - Version history

## Quick Commands for Claude

### After Making Changes:
```
"Review my recent changes and update the SEO guide if needed"
```

### Monthly Review:
```
"Review .claude/SEO_OPTIMIZATION_GUIDE.md and update it with current state"
```

### Before Deployment:
```
"Check if SEO guide needs updates before I deploy"
```

### Add New Section:
```
"Add [new feature] documentation to SEO guide"
```

## Why This Works Better Than Automation

✅ **Smart Updates**: Claude only documents relevant changes
✅ **Context Aware**: Understands what actually impacts SEO
✅ **No False Alarms**: Doesn't trigger on non-SEO changes
✅ **Better Documentation**: Writes meaningful explanations, not just logs
✅ **Flexible**: Can update in different styles based on your needs

## Set a Reminder

- **Weekly**: Ask Claude to review and update SEO docs
- **Before Git Commits**: Quick check before committing
- **After Major Features**: Document SEO impact of new features
- **Monthly Audit**: Full review and update

---

**Pro Tip**: Add this to your workflow:
1. Make code changes
2. Before committing, chat with Claude: "Update SEO docs"
3. Commit both code + updated documentation together
