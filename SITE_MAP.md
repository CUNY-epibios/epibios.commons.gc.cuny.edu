# Proposed Site Architecture for CUNY SPH Epidemiology & Biostatistics

## Site Map

```
Home (/)
│
├── About
│   ├── Department Overview
│   └── Mission & Vision
│
├── Faculty ▼ (Dropdown Menu)
│   ├── Full-Time Faculty (landing page filtered by type)
│   ├── Adjunct Faculty (landing page filtered by type)
│   ├── Affiliated Faculty (landing page filtered by type)
│   └── Individual Faculty Pages (Examples):
│       ├── /faculty/luisa-n-borrell/ (Full-Time)
│       ├── /faculty/lisa-hitch/ (Adjunct)
│       └── ...
│
├── Students
│   ├── Student Research (consolidated page)
│   ├── Student Success Stories
│   └── Student Resources
│
├── Resources ▼ (Dropdown Menu)
│   ├── Student Handbook
│   ├── Course Evaluations (protected)
│   ├── Capstone Guides
│   └── Internal Documents (protected)
│
├── News & Events
│   ├── Department News (blog format)
│   ├── Upcoming Events
│   └── Achievements & Awards
│
└── Contact
```

## Menu Structure

### Primary Navigation
1. **Home**
2. **About**
3. **Faculty** (dropdown)
   - Full-Time Faculty
   - Adjunct Faculty
   - Affiliated Faculty
4. **Students**
   - Student Research
   - Success Stories
   - Resources
5. **Resources** (dropdown)
   - Student Handbook
   - Course Evaluations
   - Capstone Guides
   - Internal Documents
6. **News & Events**
7. **Contact**

## Page Hierarchy Details

### Faculty Section
- **Parent Page**: `/faculty/` (Faculty Directory)
  - Acts as a container for all faculty.
  - Custom ACF field `Faculty Type` added to all child pages (Full-time, Adjunct, Affiliated).
  - Use Elementor or an archive view to display grid/card layouts filtered by `Faculty Type` and research area.

- **Child Pages**: Individual faculty pages at `/faculty/[slug]/`
  - Each page includes:
    - Name and title
    - Faculty Type metadata
    - Profile links (CUNY SPH, ISPH, Google Scholar, ORCID, personal/lab websites)
    - Bio and research interests
    - Publications section with shortcode: `[schopufe_publications user_id="SCHOLAR_ID" cache_hours=24]`
    - Current projects (editable by faculty)
    - Lab/group information (editable by faculty)

### Student Section
- **Student Research Page**: `/students/research/`
  - Consolidated list of all student publications and presentations
  - Organized chronologically or by year

- **Success Stories**: `/students/success/`
  - Student achievements, awards, and career placements
  - Alumni spotlights

- **Student Resources**: `/students/resources/`
  - Links to handbooks, forms, and guides
  - Academic and career resources

### Resources Section
- **Student Handbook**: `/resources/student-handbook/`
  - Existing handbook content (already in export)

- **Course Evaluations**: `/resources/course-evaluations/`
  - Protected page (login required)
  - Form integration for submission
  - Historical evaluations storage

- **Capstone Guides**: `/resources/capstone-guides/`
  - Templates, examples, and requirements

- **Internal Documents**: `/resources/internal/`
  - Password-protected area for faculty/student resources

### News & Events
- **News**: `/news/` (blog format)
  - Department announcements
  - Faculty achievements
  - Research highlights

- **Events**: `/events/`
  - Calendar view
  - Seminars, workshops, and conferences

## Content Pruning Recommendations

### Content to Remove/Consolidate
Based on the export analysis, the following should be removed as they duplicate the main CUNY SPH departmental pages:

1. **Static Program Information**
   - MPH program requirements (link to main CUNY SPH page instead)
   - PhD/DPH program details (link to main CUNY SPH page)
   - Admissions information (link to main CUNY SPH)
   - Course listings (link to main CUNY SPH)

2. **Administrative Information**
   - General contact info (link to main department page)
   - Staff directory (unless department-specific)
   - Policies and procedures that are university-wide

3. **Redundant Faculty Bios**
   - Basic faculty info that's on the main CUNY SPH site
   - Keep only research-focused content and publications

### Content to Keep & Enhance
1. **Research-focused content**
   - Faculty research areas and projects
   - Publications (via Google Scholar integration)
   - Student research achievements

2. **Internal resources**
   - Student handbook (department-specific)
   - Course evaluations
   - Internal guides and templates

3. **Community & culture**
   - News and achievements
   - Events and seminars
   - Student success stories

## Implementation Notes

- Use WordPress Custom Post Types for Faculty (if needed for advanced functionality)
- Use standard Pages for most content to keep it simple
- Implement parent-child page relationships for clean URLs
- Use WordPress Menus to create dropdown navigation
- Consider using a page builder (Elementor, Beaver Builder) for the Faculty Directory landing page
