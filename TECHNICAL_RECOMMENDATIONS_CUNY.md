# Technical Implementation Recommendations - CUNY Academic Commons Edition
## CUNY SPH Epidemiology & Biostatistics WordPress Site

**Updated for CUNY Academic Commons Available Plugins**

---

## Executive Summary

This document provides WordPress implementation strategies using **only plugins available in the CUNY Academic Commons** plugin library, plus justifications for critical missing plugins that should be requested.

### Plugin Availability Summary
- **Total Recommended Plugins**: 59
- **Available in CUNY Commons**: 23 (39%)
- **Not Available**: 36 (61%)
- **Critical Missing Plugins Requiring Justification**: 3

---

## 1. Course Evaluations System

### ✅ Available Solution: Gravity Forms

**Primary Plugin**: [Gravity Forms](available) ✅ **AVAILABLE**

**Additional Plugins Available**:
- Gravity Forms + Custom Post Types ✅
- Gravity Forms Advanced Post Creation Add-On ✅
- Gravity PDF ✅

#### Implementation Strategy

1. **Create Evaluation Form**
   - Install **Gravity Forms** from CUNY Commons
   - Build multi-step evaluation form with:
     - Course information (dropdown of current courses)
     - Instructor rating fields
     - Quantitative ratings (1-5 scales)
     - Qualitative feedback (text areas)
     - Anonymous submission option

2. **Submission Storage**
   - Store submissions in WordPress database (built into Gravity Forms)
   - Export to CSV/Excel for analysis
   - Use **Gravity PDF** to generate PDF reports

3. **Access Control**
   - Restrict form access to logged-in users only
   - Use **Password Protected** plugin ✅ (available) for page protection
   - Create dedicated page at `/resources/course-evaluations/`
   - Add login requirement with redirect

4. **Workflow**
   ```
   Student logs in → Accesses evaluation form → Submits feedback →
   Faculty/Admin reviews in backend → Export for analysis
   ```

**Available Plugins to Use**:
- ✅ Gravity Forms (forms)
- ✅ Gravity PDF (PDF reports)
- ✅ Password Protected (access control)

**Cost**: All plugins available in CUNY Commons at no additional cost

---

## 2. Faculty Self-Editing System

### ⚠️ Partial Solution Available

**Available Plugins**:
- ✅ **Team Members** - For displaying faculty
- ✅ **Restrict Media Library Access** - Limits media to authors
- ✅ **Elementor** - Frontend visual editing
- ✅ **Jetpack** - May include user management features

**Missing Critical Plugin**: User role/permission management

#### Implementation Strategy with Available Plugins

##### Step 1: Use WordPress Built-In User Roles
WordPress has built-in user roles. Configure manually:

```php
// Use WordPress native "Author" role for faculty
// Authors can:
- Edit their own posts/pages
- Upload files
- View published content
// Authors CANNOT:
- Edit others' content
- Access site settings
- Install plugins
```

##### Step 2: Assign Faculty to Their Pages
1. Create individual faculty pages (already generated)
2. Assign each faculty member as "Author" of their own page
3. Use WordPress Core author filters:
   - In admin, authors only see their own content by default

##### Step 3: Use Restrict Media Library Access
- Install **Restrict Media Library Access** ✅ (available)
- Faculty can only see/edit their own uploaded images

##### Step 4: Frontend Editing with Elementor
Install **Elementor** ✅ (available) for:
- Visual, frontend page editing
- No need to understand WordPress backend
- Drag-and-drop interface
- Can edit publications section, project descriptions, lab info

##### Step 5: Additional Configuration
Use WordPress `functions.php` or custom plugin to:
- Remove unnecessary admin menu items for Authors
- Redirect non-admin users to their page on login

#### Workflow Example
```
Faculty logs in → Redirected to their page →
Uses Elementor frontend editor → Saves changes →
Changes visible immediately (or pending review)
```

### 🔴 MISSING CRITICAL PLUGIN - JUSTIFICATION REQUIRED

**Plugin Needed**: **PublishPress Capabilities** or **User Role Editor**

**Why It's Critical**:
1. **Granular Permission Control**: WordPress built-in roles are too coarse. We need:
   - Faculty to edit ONLY their specific assigned page (not all pages they author)
   - Ability to hide specific admin menu items per role
   - Custom capabilities beyond WordPress defaults

2. **Risk Mitigation**: Without proper role management:
   - Faculty might accidentally edit wrong pages
   - Can't restrict access to sensitive areas without complex custom code
   - Difficult to audit who can access what

3. **User Experience**: Proper role management provides:
   - Clean, simplified admin interface for faculty
   - Reduced confusion and support requests
   - Professional appearance

**Alternatives if Not Approved**:
- Custom development (costly, maintenance burden)
- WordPress Multisite with per-site permissions (complex)
- Accept risks of coarse-grained permissions

**Recommended Action**: Request **Members** plugin features be enhanced OR request installation of **PublishPress Capabilities** ($79/year)

---

## 3. Student Success Showcase

### ✅ Full Solution Available

**Primary Plugins**:
1. ✅ **Custom Post Type UI** (available)
2. ✅ **Advanced Custom Fields** (available)
3. ✅ **NextGEN Gallery** (available) - For photo galleries
4. ✅ **MetaSlider** (available) - For featured content carousels

#### Implementation Strategy

##### Step 1: Create "Student Success" Custom Post Type
Using **Custom Post Type UI** ✅:
- Post Type Name: `student_success`
- Labels: "Student Success Stories"
- Public: Yes
- Show in menu: Yes
- Supports: Title, Editor, Featured Image, Categories, Tags

##### Step 2: Add Custom Fields
Using **Advanced Custom Fields** ✅ (plus Date and Time Picker extension ✅):

```
Field Group: "Student Success Details"
Fields:
- Student Name (text)
- Graduation Year (number)
- Degree Program (select: MPH, PhD, DPH)
- Current Position (text)
- Organization (text)
- Achievement Type (select: Award, Publication, Career, Research)
- Photo (image upload)
- Quote (textarea)
- LinkedIn Profile (URL)
- Achievement Date (date picker)
```

##### Step 3: Display Options

**Option A: Use NextGEN Gallery** ✅
- Create student success gallery
- Display as grid with captions
- Lightbox for detailed view

**Option B: Use WordPress Default Post Archive**
- Display on `/students/success/`
- Filter by category (award, publication, career)
- Standard blog-style layout with featured images

**Option C: Use MetaSlider** ✅ for Featured Students
- Highlight recent achievements on homepage
- Rotating carousel of success stories

##### Step 4: Use Available Block Plugins
- ✅ **Atomic Blocks** (available) - Gutenberg blocks for layouts
- ✅ **Advanced Views Lite** (available) - Display custom fields

**Available Plugins to Use**:
- ✅ Custom Post Type UI
- ✅ Advanced Custom Fields + Date picker extension
- ✅ NextGEN Gallery
- ✅ MetaSlider
- ✅ Atomic Blocks
- ✅ Advanced Views Lite

**Cost**: All plugins available at no additional cost

---

## 4. Internal Resources Hub

### ✅ Full Solution Available

**Primary Plugins**:
1. ✅ **Password Protected** (available)
2. ✅ **WP Document Revisions** (available)
3. ✅ **Media Library Assistant** (available)
4. ✅ **Jetpack** (available) - May include content restriction features

#### Implementation Strategy

##### Step 1: Create Resources Hub Structure
```
/resources/ (Public landing page with descriptions)
├── /resources/student-handbook/ (Public)
├── /resources/course-evaluations/ (Login required)
├── /resources/capstone-guides/ (Public or login required)
└── /resources/internal/ (Password protected - faculty/students only)
```

##### Step 2: Access Control Tiers

**Tier 1: Public Resources**
- Student handbook (general information)
- Public guides and forms
- No protection required

**Tier 2: Student/Faculty Resources** (Login Required)
- Use WordPress native "Private" page visibility
- Only logged-in users can access
- Set during page creation

**Tier 3: Highly Sensitive** (Password Protected)
- Use **Password Protected** plugin ✅
- Set per-page password
- Share password only with authorized users

##### Step 3: File Management
Using **Media Library Assistant** ✅ and **WP Document Revisions** ✅:

1. **Media Library Assistant**:
   - Enhanced media library organization
   - Custom taxonomies for documents
   - Better search and filtering
   - Bulk editing capabilities

2. **WP Document Revisions**:
   - Track document versions
   - Require review/approval for changes
   - View revision history
   - Restore previous versions
   - Perfect for living documents like handbooks

**Example Page Structure**:
```html
<!-- /resources/internal/ page (password protected) -->

<h2>Faculty Resources</h2>
<ul>
  <li><a href="/wp-content/uploads/faculty-handbook-2026.pdf">Faculty Handbook 2026 (PDF)</a></li>
  <li><a href="/wp-content/uploads/evaluation-results.xlsx">Course Evaluation Results (Excel)</a></li>
</ul>

<h2>Student Resources</h2>
<ul>
  <li><a href="/wp-content/uploads/capstone-template.docx">Capstone Template (Word)</a></li>
  <li><a href="/wp-content/uploads/irb-guide.pdf">IRB Application Guide (PDF)</a></li>
</ul>
```

##### Step 4: Search Functionality
Install **Relevanssi** ✅ (available) to:
- Make internal documents searchable
- Better search results for PDFs and files
- Helps students find resources quickly

**Available Plugins to Use**:
- ✅ Password Protected
- ✅ WP Document Revisions
- ✅ Media Library Assistant
- ✅ Relevanssi
- ✅ Jetpack (for additional features)

**Cost**: All plugins available at no additional cost

---

## 5. Department Culture & News Showcase

### ✅ Full Solution Available

**Primary Plugins**:
1. ✅ **The Events Calendar** (available) + Category Colors extension
2. ✅ **Events Manager** (available) - Alternative option
3. ✅ **Event Organiser** (available) - Another alternative
4. ✅ **Yoast SEO** (available)
5. ✅ **Blog2Social** (available) - Social media auto-posting

#### Implementation Strategy

##### Step 1: News Section
Use WordPress built-in blog functionality:

**Categories to Create**:
- Department News
- Faculty Achievements
- Student Achievements
- Research Highlights
- Events & Seminars
- Media Coverage

**Featured Content**:
- Use **MetaSlider** ✅ for homepage news carousel
- Latest posts with **Advanced Views Lite** ✅

##### Step 2: Events Calendar
Using **The Events Calendar** ✅ (RECOMMENDED):

**Features**:
- Calendar view
- List view
- Month/Week/Day views
- Recurring events
- Event categories with **Category Colors** extension ✅
- iCal export
- Google Calendar integration

**Alternative**: **Events Manager** ✅ or **Event Organiser** ✅
- Both full-featured
- Different UX/UI
- Choose based on preference

**Create Events**:
- Seminars and journal clubs
- Department meetings (if public)
- Workshops and training sessions
- Conferences (where faculty are presenting)
- Open houses and recruitment events

##### Step 3: Achievement Highlights
Create using **Custom Post Type UI** ✅ and **Advanced Custom Fields** ✅:

Custom post type: "Achievements"
- Faculty highlights
- Student highlights
- Department milestones

Display with **Advanced Views Lite** ✅

##### Step 4: Visual Enhancement
- **NextGEN Gallery** ✅ - Photo galleries from events
- **MetaSlider** ✅ - Featured content carousels
- **Atomic Blocks** ✅ - Gutenberg blocks for layouts

##### Step 5: SEO & Social Sharing
- **Yoast SEO** ✅ - Optimize news for search engines
- **Blog2Social** ✅ - Auto-share to social media

**Available Plugins to Use**:
- ✅ The Events Calendar + Category Colors
- ✅ Events Manager (alternative)
- ✅ Event Organiser (alternative)
- ✅ Yoast SEO
- ✅ Blog2Social
- ✅ Custom Post Type UI
- ✅ Advanced Custom Fields
- ✅ NextGEN Gallery
- ✅ MetaSlider
- ✅ Atomic Blocks

**Cost**: All plugins available at no additional cost

---

## Overall Technical Stack - CUNY Commons Edition

### Essential Plugins (All Available in CUNY Commons ✅)

**Forms & Data Collection**:
- ✅ Gravity Forms
- ✅ Gravity PDF
- ✅ Contact Form 7 (backup option)

**Content Management**:
- ✅ Custom Post Type UI
- ✅ Advanced Custom Fields
- ✅ WP Document Revisions
- ✅ Media Library Assistant

**Access Control**:
- ✅ Password Protected
- ✅ Restrict Media Library Access
- ✅ WordPress Native Roles (Author, Contributor)

**Events & Calendar**:
- ✅ The Events Calendar + Category Colors
- ✅ Events Manager (alternative)
- ✅ Event Organiser (alternative)

**Visual Enhancement**:
- ✅ Elementor (frontend editing)
- ✅ NextGEN Gallery
- ✅ MetaSlider
- ✅ Atomic Blocks

**SEO & Marketing**:
- ✅ Yoast SEO
- ✅ Blog2Social
- ✅ Relevanssi (search)

**Utility**:
- ✅ Jetpack (Swiss army knife)

### Theme Recommendations
Any of these themes should work well with available plugins:
- WordPress default themes (Twenty Twenty-Four, etc.)
- Check CUNY Commons theme library for pre-approved themes

---

## 🔴 Critical Missing Plugins - Justification for Requisition

### 1. User Role & Permission Management

**Recommended Plugin**: **PublishPress Capabilities** ($79/year) or **User Role Editor** (Free)

**Why Critical**:
- Current solution relies on WordPress built-in roles which are insufficient for faculty self-editing
- Faculty need to edit ONLY their assigned page, not all pages they author
- Need to hide specific admin menu items to reduce confusion
- WordPress core doesn't provide granular enough control

**Use Case**:
- 14 faculty members each need to edit their own profile page
- Must prevent accidental edits to other faculty pages
- Must simplify admin interface to only show relevant options
- Must maintain audit trail of who edited what

**Impact if Not Available**:
- Increased risk of faculty editing wrong content
- Higher support burden from confused faculty
- Need for expensive custom development
- Reduced user experience quality

**Alternatives Considered**:
- WordPress Multisite: Too complex for this use case
- Custom development: Costly ($2,000-5,000) and maintenance burden
- Manual management: Not scalable with 14+ faculty

**Budget**: $79/year (PublishPress) or FREE (User Role Editor)

**Recommended Action**: Request installation of **User Role Editor** (free) as starting point

---

### 2. Security Plugin

**Recommended Plugin**: **Wordfence Security** (Free version) or **Jetpack Security** (if included)

**Why Critical**:
- Site will host sensitive course evaluations
- Faculty login credentials need protection
- FERPA compliance considerations for student data
- Increasing WordPress site attacks

**Features Needed**:
- Login attempt limiting
- Firewall
- Malware scanning
- Two-factor authentication support
- Security event logging

**Current Status**:
- ✅ **Jetpack** is available - CHECK if security features included
- May provide some security features
- If insufficient, need dedicated security plugin

**Impact if Not Available**:
- Increased risk of unauthorized access to evaluations
- Potential FERPA compliance issues
- No protection against brute-force attacks
- No visibility into security threats

**Budget**: FREE (Wordfence basic) or included with Jetpack

**Recommended Action**:
1. First, check Jetpack's security features
2. If insufficient, request **Wordfence Security** (free version)

---

### 3. Backup Plugin

**Recommended Plugin**: **UpdraftPlus** (Free version)

**Why Critical**:
- Site will contain unique faculty research content
- Course evaluation data must not be lost
- No way to recover from data loss without backups
- CUNY Commons may provide network-level backups, but site-level control is important

**Features Needed**:
- Automated daily/weekly backups
- Offsite backup storage (Google Drive, Dropbox)
- One-click restore capability
- Database + file backups

**Current Status**:
- NOT available in CUNY Commons plugin library
- Unknown if CUNY provides network-level backups
- Need clarification from CUNY IT

**Impact if Not Available**:
- Risk of permanent data loss
- No disaster recovery capability
- Complete site rebuild needed if corruption occurs
- Lost course evaluations cannot be recovered

**Budget**: FREE (UpdraftPlus basic)

**Recommended Action**:
1. **FIRST**: Contact CUNY IT to confirm backup capabilities
2. If CUNY provides adequate backups, document procedure
3. If NOT, request **UpdraftPlus** (free version) or **BackWPup** (free)

---

## Security Considerations (with CUNY Plugins)

### User Access Security

1. **Password Requirements**
   - Use WordPress native password strength meter
   - Manually enforce strong passwords
   - Check if **Jetpack** ✅ includes password policies

2. **Two-Factor Authentication**
   - Check if **Jetpack** ✅ includes 2FA
   - If not, may need to request dedicated plugin

3. **Login Security**
   - Use **Jetpack** ✅ for brute force protection (if available)
   - Manually block IPs if needed
   - Check CUNY Commons network-level protections

### Content Security

1. **Regular Backups**
   - **CONFIRM WITH CUNY IT**: Does CUNY Commons provide automated backups?
   - If yes: Document restore procedure
   - If no: Request backup plugin installation

2. **SSL/HTTPS**
   - Enforce HTTPS (should be default on CUNY Commons)
   - Especially critical for login and forms

3. **File Upload Restrictions**
   - Use **Restrict Media Library Access** ✅
   - WordPress native file type restrictions
   - Limit faculty upload permissions

---

## Implementation Timeline (CUNY Commons Edition)

### Phase 1: Foundation (Week 1-2)
- Confirm CUNY Commons capabilities (backups, security, themes)
- Choose and activate theme
- Install essential plugins from CUNY library:
  - Jetpack ✅
  - Yoast SEO ✅
  - Custom Post Type UI ✅
  - Advanced Custom Fields ✅
- Create user roles and test permissions
- Build site navigation and menu structure

### Phase 2: Faculty Section (Week 2-3)
- Import faculty pages from generated HTML files
- Set up faculty user accounts (WordPress "Author" role)
- Install and configure Elementor ✅ for frontend editing
- Install Google Scholar shortcode plugin (check availability)
- Create Faculty Directory landing page using Atomic Blocks ✅
- Train faculty on Elementor editing

### Phase 3: Student & Resources (Week 3-4)
- Import student research page
- Set up student success custom post type
- Configure **Password Protected** ✅ for sensitive resources
- Set up **WP Document Revisions** ✅ for handbooks
- Configure **Media Library Assistant** ✅
- Upload internal documents

### Phase 4: Dynamic Features (Week 4-5)
- Implement course evaluation system with **Gravity Forms** ✅
- Set up **The Events Calendar** ✅
- Create news blog categories and test workflow
- Configure **Blog2Social** ✅ for social sharing
- Set up **Relevanssi** ✅ for better search

### Phase 5: Testing & Launch (Week 5-6)
- Test all user roles and permissions
- Verify Google Scholar shortcode for all faculty
- Update **Ayman El-Mohandes** page with correct Google Scholar ID
- Verify all profile links work
- Test course evaluation submission and data export
- Security audit using available tools
- Train content managers and faculty
- Document backup/restore procedure
- Launch!

---

## Training & Documentation

### For Faculty
Create video tutorials covering:
1. How to log in to WordPress
2. How to use Elementor to edit your page
3. How to add/update research projects
4. How to upload photos (Media Library)
5. Troubleshooting common issues

### For Administrators
Document procedures for:
1. Adding new faculty members and pages
2. Managing user accounts (WordPress native)
3. Publishing news posts and events
4. Managing course evaluations in Gravity Forms
5. Exporting course evaluation data
6. Updating plugins via CUNY Commons
7. Backup and restore procedure (per CUNY IT)

### For Students
Provide guides on:
1. Logging in to CUNY Commons
2. Accessing protected resources
3. Submitting course evaluations
4. Finding handbook and capstone guides

---

## Ongoing Maintenance

### Weekly Tasks
- Review new user registrations
- Review and publish pending content
- Check Gravity Forms submissions

### Monthly Tasks
- Check for plugin updates (via CUNY Commons)
- Review site analytics (Jetpack Stats ✅)
- Check for broken links (Broken Link Checker - check if available ✅)
- Update outdated content

### Quarterly Tasks
- Review user access permissions
- Archive old events
- Update privacy policy

### Annual Tasks
- Review and update faculty information
- User survey for feedback
- Refresh student success stories

---

## Questions to Ask CUNY IT

Before full implementation, clarify:

1. **Backups**:
   - Does CUNY Commons provide automated backups?
   - How do we restore from backup?
   - How far back are backups retained?

2. **Security**:
   - What network-level security is provided?
   - Is Jetpack Security included?
   - Can we request additional security plugins?

3. **Plugin Requests**:
   - Process for requesting new plugins?
   - Timeline for approval?
   - Can we request free plugins easily?

4. **User Management**:
   - Limits on number of user accounts?
   - Can external (non-CUNY) users access?
   - 2FA requirements or availability?

5. **Hosting Resources**:
   - Storage limits?
   - Bandwidth limits?
   - PHP memory limits?

6. **Custom Development**:
   - Can we add custom code (functions.php)?
   - Can we upload custom plugins (if unavailable in library)?
   - Theme customization limitations?

---

## Conclusion

This implementation plan uses **only plugins available in the CUNY Academic Commons** plugin library wherever possible. The approach provides:

- ✅ Course evaluations hosting (Gravity Forms)
- ⚠️ Faculty self-editing (WordPress native + Elementor, limited granularity)
- ✅ Student success showcase (Custom Post Type + ACF + Gallery)
- ✅ Internal resources hub (Password Protected + Document Revisions)
- ✅ Department culture & news (The Events Calendar + WordPress blog)

**Critical Gaps**:
1. User permission management (request User Role Editor - FREE)
2. Security (verify Jetpack features, possibly request Wordfence - FREE)
3. Backups (clarify CUNY IT capabilities, possibly request UpdraftPlus - FREE)

**Total Additional Cost**: Potentially $0 if using free versions and CUNY provides backups/security

**Implementation Time**: 5-6 weeks (part-time, 48-60 hours total)

All three critical missing plugins have FREE versions available, making this a cost-effective solution.

For questions about CUNY Commons capabilities or plugin availability, contact CUNY Academic Commons support.
