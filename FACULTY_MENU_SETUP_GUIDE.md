# Faculty Menu Setup Guide
## Creating the Faculty Dropdown Menu in WordPress

---

## Overview

This guide shows you how to create a Faculty menu with a dropdown containing all 14 individual faculty members.

**Result**:
```
Faculty ▼
├── Luisa N. Borrell
├── Ayman El-Mohandes
├── Renee Goodwin
├── Lisa Hitch
├── Heidi E. Jones
├── Elizabeth Kelvin
├── Denis Nash
├── Sehyun Oh
├── Nash Rochman
├── Zach Shahn
├── Chloe Teasdale
├── Levi Waldron
├── Katarzyna E Wyka
└── Constantin Yiannoutsos
```

---

## Method 1: Using Page Hierarchy (RECOMMENDED)

This method automatically creates the dropdown menu structure based on parent-child page relationships.

### Step 1: Create the Faculty Directory (Parent Page)

1. **Log in to WordPress** → Go to **Pages** → **Add New**

2. **Create Parent Page**:
   ```
   Title: Faculty
   Permalink: /faculty/
   Content: (See faculty_directory_page.html below)
   ```

3. **Publish** the page

### Step 2: Import Missing Faculty Pages (Child Pages)

13 of the 14 faculty pages have already been imported. For the remaining faculty member (Lisa Hitch), and any future faculty:

1. **Pages** → **Add New**

2. **Set Title**: Use faculty member's name
   - Example: `Lisa Hitch`

3. **Add Content**: Add their bio, photo, and details.

4. **Set Parent Page**:
   - In the right sidebar, find **"Page Attributes"** panel
   - Under **"Parent"**, select **"Faculty"**
   - This makes it a child of the Faculty page

5. **Set Permalink**:
   - Click "Edit" next to permalink
   - Should be: `/faculty/lisa-hitch/`
   - WordPress automatically adds the parent slug

6. **Set Featured Image** (optional):
   - Click "Set featured image"
   - Upload faculty photo if available

7. **Set Author**:
   - In right sidebar, **"Author"** dropdown
   - Select the faculty member (if account exists)

8. **Publish**

### Step 3: Create the Navigation Menu

1. **Go to**: Appearance → Menus

2. **Create New Menu**:
   - Click "create a new menu"
   - Menu Name: `Main Menu` (or whatever your theme uses)
   - Check "Primary Menu" location
   - Click "Create Menu"

3. **Add Faculty Parent Page**:
   - In left column, expand **"Pages"**
   - Check the box next to **"Faculty"**
   - Click "Add to Menu"

4. **Add Individual Faculty Pages**:
   - Still in **"Pages"** section
   - Check boxes for all 14 individual faculty pages
   - Click "Add to Menu"

5. **Create Hierarchy by Dragging**:
   - In the menu structure (right side)
   - **Drag** each individual faculty page **slightly to the right** under "Faculty"
   - When positioned correctly, you'll see them indented
   - This creates the dropdown

6. **Reorder Faculty Names** (optional):
   - Drag faculty pages up/down to reorder
   - Alphabetical by last name is typical:
     - Borrell, Luisa N.
     - El-Mohandes, Ayman
     - Goodwin, Renee
     - Jones, Heidi E.
     - Kelvin, Elizabeth
     - Nash, Denis
     - Oh, Sehyun
     - Rochman, Nash
     - Shahn, Zach
     - Teasdale, Chloe
     - Waldron, Levi
     - Wyka, Katarzyna E
     - Yiannoutsos, Constantin

7. **Save Menu**

---

## Method 2: Manual Menu Setup (If Page Hierarchy Doesn't Work)

If your theme doesn't automatically show child pages in dropdown:

### Step 1: Same as Method 1 (Create all pages)

### Step 2: Manually Build Menu Hierarchy

1. **Appearance** → **Menus**

2. **Add Faculty to Menu**:
   - Find "Faculty" parent page
   - Add to menu

3. **Add Custom Link** (optional directory page):
   - Click "Custom Links" in left column
   - URL: `/faculty/`
   - Link Text: `Faculty Directory` or `All Faculty`
   - Add to Menu
   - Drag slightly right under "Faculty" (makes it first submenu item)

4. **Add All Faculty Pages**:
   - Select all 14 individual faculty pages
   - Add to Menu
   - Drag each **slightly to the right** under "Faculty"
   - They should indent to show they're sub-items

5. **Reorder**:
   - Drag to alphabetize or order as desired

6. **Save Menu**

---

## Method 3: Using CSS Dropdown (If Theme Doesn't Support)

If your theme doesn't support dropdown menus natively, you may need to add CSS.

Most modern WordPress themes (including those on CUNY Commons) support dropdown menus automatically when you indent menu items.

---

## Faculty Directory Landing Page Content

Create this content for the main **Faculty** page:

```html
<!-- wp:heading -->
<h2 class="wp-block-heading">Our Faculty</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The Department of Epidemiology and Biostatistics is home to award-winning faculty conducting cutting-edge research in population health, infectious diseases, biostatistics, cancer genomics, and more. Our faculty are committed to rigorous scientific inquiry, mentoring the next generation of public health leaders, and addressing health inequities.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Faculty Directory</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Click on a faculty member's name to view their profile, including education, research interests, and publications.</p>
<!-- /wp:paragraph -->

<!-- wp:columns {"columns":2} -->
<div class="wp-block-columns">
<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Professors & Distinguished Professors</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul>
<li><a href="/faculty/luisa-n-borrell/">Luisa N. Borrell</a>, Distinguished Professor</li>
<li><a href="/faculty/ayman-el-mohandes/">Ayman El-Mohandes</a>, Professor and Dean</li>
<li><a href="/faculty/renee-goodwin/">Renee Goodwin</a>, Distinguished Professor</li>
<li><a href="/faculty/heidi-e-jones/">Heidi E. Jones</a>, Professor</li>
<li><a href="/faculty/denis-nash/">Denis Nash</a>, Distinguished Professor</li>
<li><a href="/faculty/levi-waldron/">Levi Waldron</a>, Professor and Department Chairperson</li>
<li><a href="/faculty/constantin-yiannoutsos/">Constantin Yiannoutsos</a>, Professor</li>
</ul>
<!-- /wp:list -->

</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Associate & Assistant Professors</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul>
<li><a href="/faculty/elizabeth-kelvin/">Elizabeth Kelvin</a>, Associate Professor</li>
<li><a href="/faculty/chloe-teasdale/">Chloe Teasdale</a>, Associate Professor</li>
<li><a href="/faculty/katarzyna-e-wyka/">Katarzyna E Wyka</a>, Associate Professor</li>
<li><a href="/faculty/sehyun-oh/">Sehyun Oh</a>, Assistant Professor</li>
<li><a href="/faculty/nash-rochman/">Nash Rochman</a>, Assistant Professor</li>
<li><a href="/faculty/zach-shahn/">Zach Shahn</a>, Assistant Professor</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Lecturers</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul>
<li><a href="/faculty/lisa-hitch/">Lisa Hitch</a>, Adjunct Lecturer</li>
</ul>
<!-- /wp:list -->

</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Research Areas</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Our faculty expertise spans:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
<li><strong>Infectious Disease Epidemiology</strong> – HIV/AIDS, COVID-19, emerging pathogens, global health</li>
<li><strong>Social Epidemiology</strong> – Health disparities, structural racism, social determinants of health</li>
<li><strong>Biostatistics & Data Science</strong> – Causal inference, machine learning, bioinformatics, computational biology</li>
<li><strong>Reproductive & Maternal Health</strong> – Pregnancy outcomes, contraception, adolescent health</li>
<li><strong>Mental Health & Substance Use</strong> – Depression, anxiety, tobacco, cannabis, drug policy</li>
<li><strong>Cancer Epidemiology & Genomics</strong> – Cancer prevention, microbiome research, precision medicine</li>
<li><strong>Statistical Methods</strong> – Longitudinal data analysis, survival analysis, clinical trials</li>
</ul>
<!-- /wp:list -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p><strong>Interested in joining our faculty?</strong> View current <a href="https://sph.cuny.edu/about/employment/">job openings at CUNY SPH</a>.</p>
<!-- /wp:paragraph -->
```

---

## Quick Reference: List of All 14 Faculty Members

Ensure all are present and correctly linked:

| # | Faculty Name | File | URL Slug |
|---|--------------|------|----------|
| 1 | Luisa N. Borrell | `luisa-n-borrell.html` | `/faculty/luisa-n-borrell/` |
| 2 | Ayman El-Mohandes | `ayman-el-mohandes.html` | `/faculty/ayman-el-mohandes/` |
| 3 | Renee Goodwin | `renee-goodwin.html` | `/faculty/renee-goodwin/` |
| 4 | Lisa Hitch | `lisa-hitch.html` | `/faculty/lisa-hitch/` |
| 5 | Heidi E. Jones | `heidi-e-jones.html` | `/faculty/heidi-e-jones/` |
| 6 | Elizabeth Kelvin | `elizabeth-kelvin.html` | `/faculty/elizabeth-kelvin/` |
| 7 | Denis Nash | `denis-nash.html` | `/faculty/denis-nash/` |
| 8 | Sehyun Oh | `sehyun-oh.html` | `/faculty/sehyun-oh/` |
| 9 | Nash Rochman | `nash-rochman.html` | `/faculty/nash-rochman/` |
| 10 | Zach Shahn | `zach-shahn.html` | `/faculty/zach-shahn/` |
| 11 | Chloe Teasdale | `chloe-teasdale.html` | `/faculty/chloe-teasdale/` |
| 12 | Levi Waldron | `levi-waldron.html` | `/faculty/levi-waldron/` |
| 13 | Katarzyna E Wyka | `katarzyna-e-wyka.html` | `/faculty/katarzyna-e-wyka/` |
| 14 | Constantin Yiannoutsos | `constantin-yiannoutsos.html` | `/faculty/constantin-yiannoutsos/` |

---

## Troubleshooting

### Problem: Dropdown Menu Not Showing

**Solution 1**: Check theme supports dropdown menus
- Most modern themes do
- Try a different theme (Twenty Twenty-Four, Kadence, Astra)

**Solution 2**: Check menu location
- Appearance → Menus
- Make sure menu is assigned to "Primary Menu" location

**Solution 3**: Check indentation
- In menu editor, sub-items must be indented (dragged slightly right)
- You should see visual indentation

### Problem: Child Pages Not Under Parent URL

**Solution**: Check page parent setting
- Edit individual faculty page
- Right sidebar → Page Attributes → Parent → Select "Faculty"
- Update page
- Permalink should automatically change to `/faculty/name/`

### Problem: Menu Items in Wrong Order

**Solution**: Drag to reorder
- In Appearance → Menus
- Simply drag menu items up or down
- Save Menu

### Problem: Too Many Menu Items (Dropdown Too Long)

**Solution 1**: Don't add all faculty to main menu
- Only show parent "Faculty" page in main menu
- Create Faculty Directory page with links to all faculty
- Individual pages accessible via directory or search

**Solution 2**: Use mega menu plugin (if available in CUNY Commons)
- Allows multi-column dropdowns
- Check if available in plugin library

---

## Alternative: Faculty Widget in Sidebar

If dropdown menu gets too crowded, you could also add a Faculty widget to sidebar:

1. **Appearance** → **Widgets**
2. **Add "Pages" widget** to sidebar
3. **Configure**:
   - Title: "Faculty Directory"
   - Select "Faculty" as parent page
   - Check "Show child pages"
   - Sort by: Title (alphabetical)

This shows faculty list in sidebar on any page.

---

## Testing Your Menu

### After Setup, Test:

1. ✅ **Hover over "Faculty"** in main menu
   - Dropdown should appear
   - All 14 names should show

2. ✅ **Click individual faculty names**
   - Should go to correct faculty page
   - URL should be `/faculty/name/`

3. ✅ **Click "Faculty" parent item**
   - Should go to Faculty Directory page
   - Page should list all faculty with links

4. ✅ **Check mobile view**
   - Menu should collapse to hamburger
   - Dropdown should still work (tap to expand)

5. ✅ **Check all faculty pages**
   - Verify content imported correctly
   - Check Google Scholar shortcode works
   - Verify all links are clickable

---

## Tips for Success

✅ **Use Consistent Naming**:
- Page title: "Levi Waldron" (first name first)
- URL slug: "levi-waldron" (all lowercase, hyphens)

✅ **Set Featured Images**:
- Upload faculty photos
- Makes directory page look professional
- Helps with social media sharing

✅ **Test Permissions**:
- Log in as faculty member
- Can they edit only their page?
- See TECHNICAL_RECOMMENDATIONS_CUNY.md for user role setup

✅ **Mobile Friendly**:
- Test menu on phone/tablet
- Most CUNY Commons themes are responsive

✅ **SEO Friendly**:
- Each faculty page should have unique title
- Use Yoast SEO plugin (available in CUNY Commons)
- Set focus keyword (faculty name)

---

## Summary

### Quick Steps:
1. ✅ Create "Faculty" parent page
2. ✅ Import missing faculty pages as children
3. ✅ Go to Appearance → Menus
4. ✅ Add Faculty + all child pages to menu
5. ✅ Indent child pages under Faculty
6. ✅ Save menu
7. ✅ Test dropdown!

**Time Required**:
- Parent page: 15 minutes
- Missing faculty pages: 5-10 minutes per page
- Menu setup: 15 minutes
- **Total: ~30-45 minutes**

---

## Need Help?

- **WordPress Documentation**: https://wordpress.org/support/article/wordpress-menu-user-guide/
- **CUNY Commons Support**: https://commons.gc.cuny.edu/help/
- **Your Theme Documentation**: Check your specific theme's menu setup guide

Good luck! Your faculty dropdown menu will look professional and be easy to navigate. 🎓
