# Website Maintenance Guide

This guide is for the department assistant or web administrator. It covers the routine tasks required to keep the CUNY SPH Epidemiology & Biostatistics website up to date now that the initial setup is complete.

---

## 1. Managing the Faculty Directory

Because the Faculty Directory is dynamically driven by Elementor and Advanced Custom Fields (ACF), **you do NOT need to manually edit the navigation menu or the directory grid when someone joins or leaves the department.**

### Adding a New Faculty Member

When a new faculty member joins the department:

1. Go to **Pages** → **Add New** in the WordPress dashboard.
2. **Set Title**: Enter the faculty member's full name (e.g., `John Doe`).
3. **Add Content**: Add their bio, education, and details in the text editor.
4. **Assign Faculty Type**: Scroll down to the ACF "Faculty Settings" box and select their type: `Full-time`, `Adjunct`, or `Affiliated`. *(This is the magic step that automatically places them in the correct directory!)*
5. **Set Parent Page**:
   - In the right sidebar, find the **"Page Attributes"** panel.
   - Under **"Parent"**, select **"Faculty"**.
6. **Set Permalink**:
   - Click "Edit" next to the permalink at the top.
   - Ensure it looks like: `/faculty/john-doe/`
7. **Set Featured Image**:
   - Click "Set featured image" in the right sidebar.
   - Upload their 400x400 square cropped headshot.
8. **Set Author** (Optional):
   - If they have a CUNY Commons account and you want them to be able to edit their own page, select their username from the **"Author"** dropdown.
9. **Publish**.

They will instantly appear in the dropdown menu category and on the main Faculty grid.

### Removing a Faculty Member
If a faculty member leaves:
1. Go to **Pages** → **All Pages**.
2. Hover over their name and click **Trash**. 
3. They will automatically be removed from all directories and menus.

---

## 2. Adding Student Success Stories

The Student Success section operates on a Custom Post Type, meaning you just create a new post, and it automatically gets added to the Student Success landing page.

### How to Create a New Story

1. Go to **Student Success Stories** → **Add New** in the left sidebar.
2. **Title**: Write a descriptive title (e.g., *"MH Ditmore Publishes Research in JMIR Human Factors"*).
3. **Content**: Write a short blurb about the achievement.
4. **Custom Fields**: Fill out the provided fields (Student Name, Degree Program, Graduation Year, Achievement Type).
5. **Featured Image**: Upload a photo of the student or their work.
6. **Publish**.

### Content Guidelines
*   **Privacy:** Always get a student's explicit permission before posting their photo, name, or career outcomes. If they prefer privacy, you can use "Doctoral Student" instead of their name.
*   **Completeness:** Try to include their Degree Program (MPH, PhD, etc.) and a link to the publication or conference if applicable.

---

## 3. Posting News & Events

### Department News
1. Go to **Posts** → **Add New**.
2. Write your news article.
3. In the right sidebar, assign it to the relevant **Category** (e.g., *Department News*, *Faculty Achievements*, *Research Highlights*).
4. Add a **Featured Image** so it looks good on social media and the blog feed.
5. **Publish**.

### The Events Calendar
1. Go to **Events** → **Add New**.
2. Enter the title and description of the event.
3. Scroll down to the **"The Events Calendar"** meta box to set the Date, Time, Location/Venue, and Organizer.
4. **Publish**. It will automatically appear on the `/events/` calendar page.

---

## 4. Course Evaluations

Course evaluations are collected via **Gravity Forms** on a password-protected page. 

### To view or export results:
1. Go to **Forms** → **Entries**.
2. Select the Course Evaluation form from the dropdown at the top.
3. You can view individual responses here, or click **Export** on the left menu to download the data as a CSV for Excel.

---

## 5. Routine Weekly/Monthly Maintenance

### Weekly
*   Check for new student achievements or faculty publications to feature.
*   Add upcoming department seminars to the Events Calendar.

### Monthly
*   Review the "Internal Resources" password-protected page to ensure handbooks and guidelines are current.
*   Check that no broken links exist on the main menu.
