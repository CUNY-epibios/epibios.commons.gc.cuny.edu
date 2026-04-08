# CUNY SPH Epi & Biostat Website Migration

This folder proposes next steps to continue building the new Department of Epidemiology and Biostatistics site on the CUNY Academic Commons.

## What We Have Completed
The site is now live at [epibios.commons.gc.cuny.edu](https://epibios.commons.gc.cuny.edu/) and the following are fully implemented:
* **Faculty Pages:** All 13 full-time faculty, 15 adjunct faculty, and 1 affiliated faculty member have been imported to the site.
* **Core Pages:** The *Course Evaluations* and *Student Handbook* pages are published and linked in the main menu.
* **Architecture:** A clean site structure mapping out where everything goes [`SITE_MAP.md`](SITE_MAP.md).
* **Tool Selection:** We verified which CUNY Commons plugins are available for free to achieve our exact goals without external costs.

## Ongoing Maintenance

Once the remaining setup tasks above are completed, day-to-day operations (adding new faculty, posting news, adding student success stories, and updating evaluations) are covered in the [`MAINTENANCE_GUIDE.md`](MAINTENANCE_GUIDE.md).

Here are your exact next steps to finish the site:

1. **Complete Faculty Setup (Chair/Assistant)**
   * All 30+ faculty profiles, including their Headshots and "Faculty Type" metadata (Full-time, Adjunct, Affiliated), have been fully imported.
   * Offer faculty access to edit their pages, then manually invite them via the CUNY Commons "Users -> Add New" interface using their official campus emails. Once they activate their accounts, you can bulk-reassign authorship of their pages to them.
   * Review [`FACULTY_MENU_SETUP_GUIDE.md`](FACULTY_MENU_SETUP_GUIDE.md) for Elementor layout instructions for the main Faculty directory page.

2. **Add Student Success & Events (Assistant)**
   * **Student Success & Research:** The old static "Research" page (currently in draft status) is obsolete. Instead, use the Custom Post Type showcase outlined in [`STUDENT_SUCCESS_GUIDE.md`](STUDENT_SUCCESS_GUIDE.md) to set up a dynamic portfolio of student publications, presentations, and career placements. Add it to the navigation menu.
   * **News & Events:** A sample news post ("This is a News Post!") has been created. Set up *The Events Calendar* plugin and configure category-based news feeds. Add these pages to the menu.

3. **Review and Launch**
   * Check that pages look correct and test the Course Evaluations form to ensure it captures data securely. (Note: Security and backups are handled inherently by the CUNY Academic Commons infrastructure, eliminating the need for third-party security plugins). Finalize any styling before officially announcing the new site!