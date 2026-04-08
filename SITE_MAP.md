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
│   ├── Student Success & Research
│   └── Student Handbook & Resources (protected)
│
├── Course Evaluations
│
├── News & Events
│   ├── Department News (blog format)
│   └── Upcoming Events
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
   - Student Success & Research
   - Student Handbook & Resources
5. **Course Evaluations**
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
- **Student Success & Research**: `/students/success/`
  - A dynamic portfolio grid of student achievements
  - Includes publications, conference presentations, awards, and career placements
  - Filterable by achievement type and degree program

- **Student Handbook & Resources**: `/students/handbook/`
  - Acts as an index page linking to all critical student materials
  - Existing handbook content (already in export)
  - Capstone templates, examples, and requirements
  - General academic and career resources

### Course Evaluations Section
- **Course Evaluations**: `/course-evaluations/`
  - Form integration for submission
  - Historical evaluations storage (publicly viewable)

### News & Events
- **News**: `/news/` (blog format)
  - Department announcements
  - Faculty achievements and awards
  - Research highlights
  - Major student awards (cross-posted from Success Stories)

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
   - Student Success & Research portfolio

## Implementation Notes

- Use WordPress Custom Post Types for Faculty (if needed for advanced functionality)
- Use standard Pages for most content to keep it simple
- Implement parent-child page relationships for clean URLs
- Use WordPress Menus to create dropdown navigation
- Consider using a page builder (Elementor, Beaver Builder) for the Faculty Directory landing page
