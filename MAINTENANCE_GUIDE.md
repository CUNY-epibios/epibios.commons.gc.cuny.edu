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

## 2. Adding Student Success & Research Stories

The Student Success & Research section operates on a Custom Post Type, meaning you just create a new post, and it automatically gets added to the Student portfolio landing page.

### How to Create a New Story

1. Go to **Student Success Stories** in the left sidebar dashboard menu, then click the **Add New Student Success Story** button at the top.
2. **Title**: Write a descriptive title (e.g., *"MH Ditmore Publishes Research in JMIR Human Factors"*).
3. **Content**: Write a short blurb about the achievement.
4. **Tag the Achievement (ACF)**: Scroll down to the ACF custom fields block and assign the metadata. This is critical for allowing visitors to filter the portfolio grid!
   - **Achievement Type:** Select one of the available choices: `Publication`, `Conference Presentation`, `Award/Honor`, `Career Achievement`, or `Research Project`.
   - **Degree Program:** Select `MPH`, `PhD`, or `DPH`.
   - **Graduation Year:** Enter their graduation year (if applicable).
5. **Featured Image**: Upload a photo of the student or their work.
6. **Publish**.

### Content Guidelines
*   **Privacy:** Always get a student's explicit permission before posting their photo, name, or career outcomes. If they prefer privacy, you can use "Doctoral Student" instead of their name.
*   **Completeness:** Try to include their Degree Program (MPH, PhD, etc.) and a link to the publication or conference if applicable.

---

## 3. Posting News & Events

### Department News & Faculty Achievements
We use the standard WordPress "Posts" feature (the blog) for time-sensitive, chronological updates. **This is where you should highlight Faculty Awards and Achievements.**

1. Go to **Posts** → **Add New**.
2. Write your news article (e.g., "Dr. Waldron Awarded New NIH Grant").
3. In the right sidebar, assign it to the relevant **Category** (e.g., *Department News*, *Faculty Achievements*, *Research Highlights*).
4. Add a **Featured Image** so it looks good on social media and the blog feed.
5. **Publish**.

*(Note: If a student wins a massive national award, you should create a Student Success Story for their permanent portfolio AND publish a News Post to announce it on the blog!)*

### The Events Calendar (Upcoming Events)
The website uses "The Events Calendar" plugin. This automatically generates a full, interactive calendar view at the `/events/` URL, and **automatically includes "Add to Google Calendar" and "iCal Export" buttons** on every event for visitors.

1. Go to **Events** → **Add New**.
2. Enter the title and description of the event.
3. Scroll down to the **"The Events Calendar"** meta box to set the Date, Time, Location/Venue, and Organizer.
4. **Publish**. It will automatically appear on the public `/events/` calendar page.

---

## 4. Course Evaluations

Course evaluations are displayed using the **TablePress** plugin. 

### To update the evaluations data:
1. Generate the updated evaluations CSV file using the [`teachingevals` R package](https://github.com/CUNY-epibios/teachingevals) (Note: this is a private GitHub repository).
2. In the WordPress dashboard, go to **TablePress** → **Import a Table**.
3. Select your generated CSV file as the Import Source.
4. Under "Import Options", choose to **Replace existing table** and select the Course Evaluations table from the list.
5. Click **Import** to update the data displayed on the site.

---

## 5. Routine Weekly/Monthly Maintenance

### Weekly
*   Check for new student achievements or faculty publications to feature.
*   Add upcoming department seminars to the Events Calendar.

### Monthly
*   Review the Student Handbook & Resources page to ensure handbooks and guidelines are current.
*   Check that no broken links exist on the main menu.

### Every Semester
*   Update the Course Evaluations form with the previous semester's evaluations.
*   Review the Faculty Directory to ensure all information is current (e.g., new hires, adjunct faculty who have not taught in the past year).