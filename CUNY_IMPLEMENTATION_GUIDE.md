# CUNY Academic Commons Implementation Guide
## Quick Reference for Epi & Biostat Site

**Updated**: February 28, 2026 - CUNY Academic Commons Edition

---

## 📚 Document Roadmap

### Start Here
1. **[CUNY_IMPLEMENTATION_GUIDE.md](CUNY_IMPLEMENTATION_GUIDE.md)** ⭐ **YOU ARE HERE** - Quick start for CUNY
2. **[TECHNICAL_RECOMMENDATIONS_CUNY.md](TECHNICAL_RECOMMENDATIONS_CUNY.md)** - Full implementation guide with CUNY plugins
3. **[PLUGIN_REQUISITION_JUSTIFICATIONS.md](PLUGIN_REQUISITION_JUSTIFICATIONS.md)** - Request missing critical plugins

### Content Files
- **[SITE_MAP.md](SITE_MAP.md)** - Proposed site architecture

---

## 🎯 Key Differences: CUNY vs. Original Plan

### What Changed
We analyzed the **612 plugins available in CUNY Academic Commons** and updated all recommendations to use only available plugins where possible.

| Feature | Original Plan | CUNY Commons Plan |
|---------|--------------|------------------|
| **Forms** | Gravity Forms ($59) | ✅ Gravity Forms (available!) |
| **User Roles** | PublishPress ($79) | WordPress native + **request plugin** |
| **Security** | Wordfence (free) | Jetpack (check features) + **request if needed** |
| **Backups** | UpdraftPlus (free) | CUNY IT backups + **request if needed** |
| **Custom Fields** | ACF Pro ($49) | ✅ ACF Free (available!) |
| **Events** | Events Calendar Pro ($99) | ✅ Events Calendar Free (available!) |
| **Frontend Editing** | Elementor Pro ($59) | ✅ Elementor Free (available!) |
| **Portfolio** | Essential Grid ($39) | ✅ NextGEN Gallery (available!) |
| **Total Annual Cost** | $385-700 | **$0** |

### Available vs. Not Available

✅ **Available in CUNY Commons** (23 plugins):
- Gravity Forms + extensions
- Advanced Custom Fields
- Custom Post Type UI
- The Events Calendar + extensions
- Elementor
- Yoast SEO
- NextGEN Gallery, MetaSlider
- Password Protected
- WP Document Revisions
- Relevanssi
- Blog2Social
- Jetpack

❌ **Not Available** (Need workarounds or requests):
- User role management (request User Role Editor - FREE)
- Security plugins (check Jetpack, request Wordfence - FREE)
- Backup plugins (check CUNY IT, request UpdraftPlus - FREE)
- Some portfolio/grid plugins (use available alternatives)

---

## 🚀 Quick Start Implementation

### Phase 0: Pre-Implementation (Do This First!)

#### Contact CUNY IT to Clarify:
```
1. Does CUNY Commons provide automated backups?
   - If yes: What is restore procedure?
   - If no: Request UpdraftPlus plugin

2. Does Jetpack subscription include Security features?
   - If yes: How to enable?
   - If no: Request Wordfence plugin

3. Can we request additional free plugins?
   - User Role Editor (for faculty permissions)
   - Process and timeline?
```

**Template Email**: See [PLUGIN_REQUISITION_JUSTIFICATIONS.md](PLUGIN_REQUISITION_JUSTIFICATIONS.md)

---

### Phase 1: Foundation (Week 1)

#### Install Essential Plugins from CUNY Commons:
1. ✅ **Jetpack** - Swiss army knife (stats, security?)
2. ✅ **Yoast SEO** - Search engine optimization
3. ✅ **Custom Post Type UI** - For student success posts
4. ✅ **Advanced Custom Fields** - Custom data fields
5. ✅ **Gravity Forms** - Course evaluation forms
6. ✅ **The Events Calendar** - Department events
7. ✅ **Elementor** - Faculty page editing
8. ✅ **Password Protected** - Restrict content
9. ✅ **WP Document Revisions** - Document management
10. ✅ **Relevanssi** - Better search

#### Activate All in One Go:
- Log in to CUNY Commons admin
- Navigate to Plugins
- Search and activate each from list above

---

### Phase 2: Faculty Pages (Week 2)

#### Import Missing Faculty Pages:
```bash
13 of the 14 faculty pages have already been imported.
For the remaining faculty member (Lisa Hitch):
1. Create new page: Pages → Add New
2. Set parent page to "Faculty"
3. Add content for the faculty member
4. Add faculty member as Author
5. Set URL slug
6. Publish
```

#### Set Up Faculty Accounts:
```
For each faculty member:
1. Users → Add New
2. Username: firstlast (e.g., leviwaldron)
3. Email: faculty CUNY email
4. Role: Author (WordPress built-in)
5. Send welcome email
```

#### Configure Elementor:
1. Install Elementor ✅
2. Allow Authors to use Elementor:
   - Elementor → Settings → Advanced
   - Enable for Authors
3. Train faculty on frontend editing

---

### Phase 3: Course Evaluations (Week 2-3)

*(Note: Historical course evaluation data has already been imported using TablePress).*

#### Create Evaluation Form:
```
1. Forms → Add New (Gravity Forms)
2. Add fields:
   - Course dropdown
   - Instructor ratings (1-5)
   - Open feedback
3. Settings → Confirmation:
   - "Thank you for your feedback"
4. Settings → Restrictions:
   - Require login
```

#### Create Evaluations Page:
```
1. Pages → Add New
2. Title: "Course Evaluations"
3. Add Gravity Form
4. Set visibility: Private (login required)
5. Add to Resources menu
```

---

### Phase 4: Student Success (Week 3)

#### Create Custom Post Type:
```
1. CPT UI → Add/Edit Post Types
2. Post Type Slug: student_success
3. Plural Label: Student Success Stories
4. Supports: Title, Editor, Featured Image
5. Save
```

#### Add Custom Fields:
```
1. Custom Fields → Add New (ACF)
2. Field Group: "Student Details"
3. Add fields:
   - Student Name (text)
   - Graduation Year (number)
   - Degree (select)
   - Achievement (textarea)
   - Photo (image)
4. Location: Post Type = student_success
5. Publish
```

#### Configure Student Research Page:
```
1. Find the existing "Research" page (currently in draft status)
2. Rename to "Student Research" if preferred
3. Add content using the Student Success custom post type showcase
4. Publish
5. Add to Students menu
```

---

### Phase 5: Events & News (Week 4)

#### Set Up Events Calendar:
```
1. Install The Events Calendar ✅
2. Events → Settings:
   - Set timezone
   - Choose default view
3. Events → Add New:
   - Create test event
4. Add Events to main navigation
```

#### Create News Categories:
```
1. Posts → Categories
2. Add categories:
   - Department News
   - Faculty Achievements
   - Student Success
   - Research Highlights
   - Events & Seminars
```

#### Configure Social Sharing:
```
1. Install Blog2Social ✅
2. Connect social accounts (optional)
3. Set auto-post rules
```

---

### Phase 6: Resources Hub (Week 4-5)

#### Upload Documents:
```
1. Media → Add New
2. Upload handbooks, guides
3. Note URLs for linking
```

#### Create Protected Pages:
```
1. Pages → Add New
2. Title: "Internal Resources"
3. Add document links
4. Password Protected plugin:
   - Set page password
   - Share with faculty/students only
```

#### Version Control:
```
1. Install WP Document Revisions ✅
2. Upload living documents
3. Enable workflow approval
```

---

## 🔐 Security Checklist

Since security plugins may not be available:

### Manual Security Steps:
```
✓ Use strong passwords (12+ characters)
✓ Enable WordPress auto-updates
✓ Update plugins weekly
✓ Use HTTPS (should be default on CUNY)
✓ Limit login attempts manually (note IPs)
✓ Regular backups (per CUNY IT procedure)
✓ Check Jetpack security features
✓ Restrict file uploads to known types
✓ Remove unused plugins and themes
✓ Use Restrict Media Library Access ✅
```

---

## 📊 5 Strategic Goals - CUNY Implementation

### Goal 1: Course Evaluations ✅ FULLY ACHIEVABLE
**Plugins**: Gravity Forms ✅ + Password Protected ✅
- Create custom evaluation forms
- Restrict to logged-in users
- Export data to Excel/CSV
- Store securely in database

### Goal 2: Faculty Self-Editing ⚠️ PARTIAL
**Plugins**: WordPress Author role + Elementor ✅
- Faculty can edit their pages
- Elementor provides visual editor
- ⚠️ Can't restrict to ONLY their page (need User Role Editor)
- Workaround: Good training and documentation

### Goal 3: Student Success ✅ FULLY ACHIEVABLE
**Plugins**: Custom Post Type UI ✅ + ACF ✅ + NextGEN Gallery ✅
- Create student success posts
- Add custom fields (degree, year, achievement)
- Display as grid/gallery
- Fully functional with available plugins

### Goal 4: Internal Resources ✅ FULLY ACHIEVABLE
**Plugins**: Password Protected ✅ + WP Document Revisions ✅ + Media Library Assistant ✅
- Upload handbooks and guides
- Password protect sensitive pages
- Track document versions
- Organized file management

### Goal 5: Department Culture ✅ FULLY ACHIEVABLE
**Plugins**: The Events Calendar ✅ + Yoast SEO ✅ + Blog2Social ✅
- Events calendar with multiple views
- News blog with categories
- SEO optimization
- Social media integration

---

## 🔴 Critical Plugins to Request

### Priority 1: User Role Editor (FREE)
**Why**: Faculty need to edit ONLY their specific page
**Impact**: Without it, faculty can edit ALL their authored pages
**Status**: Request from CUNY IT
**Cost**: $0 (free plugin)
**Justification**: See PLUGIN_REQUISITION_JUSTIFICATIONS.md Section 1

### Priority 2: Wordfence or Security Plugin (FREE)
**Why**: Protect course evaluation data (FERPA compliance)
**Impact**: Without it, vulnerable to attacks
**Status**: First check Jetpack features, then request if needed
**Cost**: $0 (free plugin)
**Justification**: See PLUGIN_REQUISITION_JUSTIFICATIONS.md Section 2

### Priority 3: UpdraftPlus Backup (FREE)
**Why**: Disaster recovery capability
**Impact**: Without it, data loss is permanent
**Status**: First check CUNY IT backup procedure
**Cost**: $0 (free plugin)
**Justification**: See PLUGIN_REQUISITION_JUSTIFICATIONS.md Section 3

---

## 📝 Pre-Launch Checklist

### Before Going Live:
```
□ 13 faculty pages imported (Lisa Hitch pending)
□ Faculty user accounts created
□ Elementor frontend editing tested
□ Course evaluation form tested
□ Password protected pages working
□ Events calendar configured
□ News categories created
□ Student research page published
□ All navigation menus built
□ Mobile responsiveness checked
□ Backup procedure documented (from CUNY IT)
□ Security features enabled (Jetpack or requested plugin)
□ Faculty trained on editing their pages
□ Admin documentation completed
□ Contact CUNY IT questions answered
```

---

## 🆘 Troubleshooting

### Can't Find a Plugin?
- Check [available_plugins.csv](available_plugins.csv) for full list
- Search CUNY Commons plugin library
- Contact CUNY Commons support

### Faculty Can't Edit Pages?
- Confirm they are set as "Author" role
- Confirm they are the Author of their specific page
- Check Elementor is enabled for Authors

### Form Submissions Not Working?
- Verify Gravity Forms is activated
- Check form notification settings
- Ensure email server is configured

### Course Evaluations Not Secure?
- Verify page is set to "Private" visibility
- Check Password Protected plugin is active
- Test with logged-out user

### No Backup Available?
- Contact CUNY IT immediately
- Request UpdraftPlus installation
- Do NOT launch without backup solution

---

## 📞 Support Contacts

### CUNY Academic Commons Support
- Website: https://commons.gc.cuny.edu/help/
- Email: commons@gc.cuny.edu
- Documentation: https://commonsinabox.org/documentation/

### Plugin-Specific Help
- **Gravity Forms**: https://www.gravityhelp.com/
- **Elementor**: https://elementor.com/help/
- **Advanced Custom Fields**: https://www.advancedcustomfields.com/resources/
- **The Events Calendar**: https://evnt.is/support

---

## 💡 Next Steps

1. ✅ Read this guide
2. ✅ Contact CUNY IT with questions (use templates in PLUGIN_REQUISITION_JUSTIFICATIONS.md)
3. ✅ Install available plugins (list above)
4. ✅ Request critical missing plugins if needed
5. ✅ Follow Phase 1-6 implementation timeline
6. ✅ Test thoroughly before launch
7. ✅ Train faculty and admins
8. ✅ Launch! 🚀

---

## 📈 Success Metrics

After launch, measure:
- Number of faculty actively updating their pages
- Course evaluation submission rates
- Website traffic and engagement
- Faculty satisfaction with editing experience
- Time to publish new content
- Security incidents (should be zero)

---

## Conclusion

The CUNY Academic Commons provides **23 of the plugins we need** at no additional cost. This includes all the major functionality:

✅ Forms & evaluations (Gravity Forms)
✅ Custom content (ACF + CPT UI)
✅ Events calendar (The Events Calendar)
✅ Visual editing (Elementor)
✅ Document management (WP Document Revisions)

With 3 free plugins requested (User Role Editor, Wordfence, UpdraftPlus), we'll have a complete, professional solution for **$0 total cost**.

**Total Implementation Time**: 5-6 weeks
**Total Additional Cost**: $0
**Ready to launch**: Yes, after CUNY IT clarifications

Good luck with your implementation! 🎓
