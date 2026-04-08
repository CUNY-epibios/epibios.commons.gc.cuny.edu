# Faculty Menu Setup Guide
## Creating the Faculty Dropdown Menu in WordPress

---

## Overview

The bulk of the heavy lifting for the Faculty section has already been completed:
- The main `/faculty/` parent page exists.
- All 13 Full-time faculty, 15 Adjunct faculty, and 1 Affiliated faculty profiles have been imported via XML as child pages.
- The duplicated navigation menu items caused by the XML imports have been cleaned up.

The final steps are to ensure the navigation menu is structured by "Faculty Type" rather than a massive list of names, and to configure Elementor to display the directory and headshots correctly.

**Goal Result for the Menu**:
```
Faculty ▼
├── Full-Time Faculty
├── Adjunct Faculty
└── Affiliated Faculty
```
*(Users click these links to view a filtered directory for that faculty type, and from there can click into individual faculty profiles).*

---

## Step 1: Create Category Pages and the Navigation Menu

Because listing potentially dozens of faculty in a single dropdown is bad for usability, we recommend grouping them by type. 

1. **Go to**: Appearance → Menus

2. **Select the Main Menu**:
   - Ensure you are editing the active primary navigation menu.

3. **Verify the Faculty Parent Page**:
   - Make sure the main **"Faculty"** page is in the menu.

4. **Add Category Pages (or Custom Links) for the Dropdown**:
   - You can create separate pages for "Full-Time Faculty", "Adjunct Faculty", and "Affiliated Faculty" that use Elementor/ACF to filter and display the respective faculty.
   - Add these three pages to the menu.

5. **Create Hierarchy by Dragging**:
   - In the menu structure (right side)
   - **Drag** each category page **slightly to the right** under "Faculty"
   - When positioned correctly, you'll see them indented

6. **Save Menu**

---

## Step 2: Displaying the Faculty Directory & Featured Images

By default, the imported XML sets up the data correctly in the backend, but your WordPress theme may not render it automatically. The assistant must address two critical display issues:

### Issue A: The Faculty Directory Only Shows Full-Time Faculty
**Problem:** The main `/faculty/` page currently consists of static HTML from the legacy site. The old site used to list out every single faculty member by name here.
**Solution:**
1. Edit the "Faculty" page with Elementor.
2. Delete the static legacy HTML grid of names.
3. Drag in a dynamic **"Posts"** or **"Portfolio"** widget.
4. Set the query source to `Pages` and filter by `Parent: Faculty`. This will generate an auto-updating grid of all faculty members (including adjuncts) that will stay current forever.

### Issue B: Featured Images (Headshots) Are Missing from Faculty Pages
**Problem:** The XML import correctly assigns the 400x400 headshots as the "Featured Image" for each faculty member (visible in the right sidebar). However, many CUNY Commons themes do not automatically print the Featured Image at the top of standard "Pages."
**Solution (Elementor Pro Required):**
1. Go to **Templates** → **Theme Builder**.
2. Add a new **Single Page** template.
3. Drag a **Featured Image** widget to the top of the layout, followed by a **Post Content** widget underneath it.
4. Set the Display Conditions to `Include: Child Of: Faculty`.
5. Publish. This instantly forces the theme to render the headshots for all 30+ faculty members without editing their pages one by one!

---

## Faculty Directory Landing Page Content

As noted in Issue A above, the `Faculty` page should **not** contain a static HTML grid of names, because then every new adjunct or affiliated faculty member would need to be typed in by hand.

Instead, the human assistant should use **Elementor Pro's Posts Widget** to create a dynamic directory:

1. Edit the `Faculty` page.
2. Add a text block at the top: *"The Department of Epidemiology and Biostatistics is home to award-winning faculty conducting cutting-edge research in population health, infectious diseases, biostatistics, cancer genomics, and more..."*
3. Drag the **Posts** widget into the page.
4. **Content Tab -> Query:**
   - Source: `Pages`
   - Include By: `Term`
   - Term: `Parent -> Faculty`
5. **Content Tab -> Layout:**
   - Skin: `Cards`
   - Columns: `3` or `4`
   - Show Image: `Yes` (This automatically pulls the 400x400 headshots).
   - Title: `Yes`
   - Excerpt: `No`
   - Read More: `No`

---

## Quick Reference: List of Faculty Members

Ensure all are present, correctly linked, and assigned the proper "Faculty Type":

### Full-time Faculty (13)
| # | Faculty Name | URL Slug |
|---|--------------|----------|
| 1 | Luisa N. Borrell | `/faculty/luisa-n-borrell/` |
| 2 | Ayman El-Mohandes | `/faculty/ayman-el-mohandes/` |
| 3 | Renee Goodwin | `/faculty/renee-goodwin/` |
| 4 | Heidi E. Jones | `/faculty/heidi-e-jones/` |
| 5 | Elizabeth Kelvin | `/faculty/elizabeth-kelvin/` |
| 6 | Denis Nash | `/faculty/denis-nash/` |
| 7 | Sehyun Oh | `/faculty/sehyun-oh/` |
| 8 | Nash Rochman | `/faculty/nash-rochman/` |
| 9 | Zach Shahn | `/faculty/zach-shahn/` |
| 10 | Chloe Teasdale | `/faculty/chloe-teasdale/` |
| 11 | Levi Waldron | `/faculty/levi-waldron/` |
| 12 | Katarzyna E Wyka | `/faculty/katarzyna-e-wyka/` |
| 13 | Constantin Yiannoutsos | `/faculty/constantin-yiannoutsos/` |

### Adjunct Faculty (15)
| # | Faculty Name | URL Slug |
|---|--------------|----------|
| 1 | Fiona Fogarty | `/faculty/fiona-fogarty/` |
| 2 | Amena El Harakeh | `/faculty/amena-el-harakeh/` |
| 3 | Tony DeVito | `/faculty/tony-devito/` |
| 4 | Priscilla Lopez D'Antico | `/faculty/priscilla-lopez-dantico/` |
| 5 | Mukta Mohnani | `/faculty/mukta-mohnani/` |
| 6 | David Goldfarb | `/faculty/david-goldfarb/` |
| 7 | Rehana Rasul | `/faculty/rehana-rasul/` |
| 8 | Jenny Shen | `/faculty/jenny-shen/` |
| 9 | Madelyn Carlson | `/faculty/madelyn-carlson/` |
| 10 | Jose Fernando Florez-Arango | `/faculty/jose-fernando-florez-arango/` |
| 11 | Kimberly Sebek | `/faculty/kimberly-sebek/` |
| 12 | Ludwig Geistlinger | `/faculty/ludwig-geistlinger/` |
| 13 | Haoyan Zhong | `/faculty/haoyan-zhong/` |
| 14 | Chloe Mirzayi | `/faculty/chloe-mirzayi/` |
| 15 | Lisa Hitch | `/faculty/lisa-hitch/` |

### Affiliated Faculty (1)
| # | Faculty Name | URL Slug |
|---|--------------|----------|
| 1 | Theresa Diaz | `/faculty/theresa-diaz/` |

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
   - Full-Time, Adjunct, and Affiliated categories should show

2. ✅ **Click individual category links**
   - Should go to the filtered faculty directory page for that type

3. ✅ **Click "Faculty" parent item**
   - Should go to the main Faculty Directory page
   - Page should list all faculty with links, separated by type

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
1. ✅ Parent page & Faculty Pages imported via XML
2. ✅ Static submenus deleted from main navigation
3. Create Category Pages (Full-Time, Adjunct, Affiliated)
4. Add Category Pages to dropdown menu
5. Update Faculty Directory with Elementor Posts Widget
6. Apply Single Page Theme Builder template for Featured Images
7. Test dropdown!

**Time Required**:
- Directory Updates & Elementor Setup: 30 minutes

---

## Need Help?

- **WordPress Documentation**: https://wordpress.org/support/article/wordpress-menu-user-guide/
- **CUNY Commons Support**: https://commons.gc.cuny.edu/help/
- **Your Theme Documentation**: Check your specific theme's menu setup guide

Good luck! Your faculty dropdown menu will look professional and be easy to navigate. 🎓
