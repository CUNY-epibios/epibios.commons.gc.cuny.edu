# CUNY SPH Epi & Biostat Website Migration

This folder contains everything needed for you (the Department Chair) and your assistant to continue building the new Department of Epidemiology and Biostatistics site on the CUNY Academic Commons.

*(Note: Old data dumps and Python scripts used to extract the legacy site have been moved to the `archive/` folder to keep your workspace clean).*

## What We Have Completed
The site is now live at [epibios.commons.gc.cuny.edu](https://epibios.commons.gc.cuny.edu/) and the following are fully implemented:
* **Full-time Faculty Pages:** All 14 faculty pages have been imported and the dropdown navigation menu is set up.
* **Core Pages:** The *Course Evaluations* and *Student Handbook* pages are published and linked in the main menu.
* **Architecture:** A clean site structure mapping out where everything goes (`SITE_MAP.md`).
* **Tool Selection:** We verified which CUNY Commons plugins are available for free to achieve our exact goals without external costs (`CUNY_PLUGIN_ANALYSIS.md`).

## Remaining Tasks

Here are your exact next steps to finish the site:

1. **Add Student Research & Events (Assistant)**
   * **Student Research:** Import the student research content (from `student_page.html` or by following `STUDENT_SUCCESS_GUIDE.md` to set up the Custom Post Type showcase). Add it to the navigation menu.
   * **News & Events:** Set up *The Events Calendar* plugin and configure category-based news feeds. Add these pages to the menu.

2. **Configure Faculty Access (Chair/Assistant)**
   * Create WordPress accounts for the faculty. 
   * Assign the standard WordPress **Author** role to each faculty member. By sticking purely to natively available CUNY Commons plugins, the built-in Author role provides a streamlined way for faculty to update their own pages without needing extra user-role plugins.

3. **Review and Launch**
   * Check that pages look correct and test the Course Evaluations form to ensure it captures data securely. (Note: Security and backups are handled inherently by the CUNY Academic Commons infrastructure, eliminating the need for third-party security plugins). Finalize any styling before officially announcing the new site!