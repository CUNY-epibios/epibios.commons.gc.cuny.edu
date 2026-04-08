# XML Direct Editing Plan for Faculty Setup

This plan details how Gemini will directly manipulate the WordPress XML export file (`cunysphepidemiologyandbiostatistics.WordPress.2026-04-08.xml`) to inject the necessary faculty profiles and structural metadata, bypassing hours of manual data entry in the WordPress dashboard.

## 1. Action Plan

Gemini will execute a Python script to perform the following operations on the XML file, outputting a new file ready for WordPress import:

### A. Inject ACF Metadata for Existing Full-time Faculty
- Locate all 13 existing full-time faculty `<item>` blocks.
- Inject the Advanced Custom Fields (ACF) metadata:
  ```xml
  <wp:postmeta>
    <wp:meta_key>faculty_type</wp:meta_key>
    <wp:meta_value><![CDATA[Full-time]]></wp:meta_value>
  </wp:postmeta>
  ```

### B. Auto-Generate Adjunct Faculty Pages
- Parse the adjunct faculty data (extracted below).
- For each adjunct, synthesize a new `<item>` block containing:
  - `<title>`: Faculty Name
  - `<content:encoded>`: Generated bio listing their title and courses taught.
  - `<wp:post_type>`: `page`
  - `<wp:postmeta>`: Set `faculty_type` to `Adjunct`.
  - `<wp:post_parent>`: The ID of the "Faculty" parent page (determined by parsing the XML).

### C. Auto-Generate Affiliated Faculty Pages
- Once provided (see Missing Data section), synthesize `<item>` blocks for all Affiliated faculty with the `faculty_type` set to `Affiliated`.

### D. Shortcodes and Formatting
- Ensure all faculty types (Full-time, Adjunct, Affiliated) support the `[schopufe_publications user_id="..."]` shortcode.
- Apply this shortcode to any faculty member with a known Google Scholar ID (e.g., Lisa Hitch, Theresa Diaz) so their publications are automatically listed.

### E. Faculty Photos
- A set of raw faculty photos has been processed (cropped to a consistent 1:1 square ratio and resized to 400x400 pixels) and saved in the `photos/` directory.
- Because local files cannot be embedded directly into a WordPress XML import, the generated `<content:encoded>` block for each new faculty member will include a placeholder block (e.g., `<!-- IMAGE UPLOAD REQUIRED: photos/Name.jpg -->`).
- After the XML import, the web assistant will batch-upload the contents of the `photos/` folder to the WordPress Media Library and set them as the "Featured Image" for the respective faculty pages.

---

## 2. Pre-Import WordPress Checklist

Before importing the processed XML file (`site-export_processed.xml`), you **must** complete the following in your WordPress dashboard:

1. **ACF "Faculty Type" Configuration:**
   - Confirm you have an ACF Field Group configured with the Field Name `faculty_type`, Field Type "Radio Button", and Choices: `Full-time`, `Adjunct`, `Affiliated`.
2. **Parent "Faculty" Page:**
   - Confirm the main "Faculty" page exists with the ID `267` (this is the ID the script assigned as the parent for all new pages).
3. **Scholar Plugin:**
   - Confirm the CUNY Commons plugin providing the `[schopufe_publications]` shortcode (e.g., Scholar Publications Fetcher) is activated.
4. **CUNY Commons User Accounts:**
   - **Crucial Note:** CUNY Academic Commons requires users to be invited and register using their official campus email (e.g., `name@brooklyn.cuny.edu`). You *cannot* use their CUNYfirst login (e.g., `name@login.cuny.edu`) as it is not a functional inbox for activation emails.
   - When you import the XML, WordPress will detect the synthesized usernames (e.g., `lisahitch`, `theresadiaz`).
   - During the import prompt, do **not** attempt to create new users directly via the importer if they need edit access later, as you won't be able to enforce the CUNY email requirement correctly through that interface. 
   - **Recommendation:** Assign all imported posts to your own administrative account during the import. Then, manually invite the faculty members via the CUNY Commons "Users -> Add New" interface using their official campus emails. Once they activate their accounts, you can bulk-reassign authorship of their pages to them.

---

## 3. Extracted Adjunct Faculty Data

Based on `adjunctfaculty.csv`, the following adjunct faculty profiles will be generated. They will be formatted with a brief bio stating their title and the courses they teach.

1. **Fiona Fogarty** (Adjunct Lecturer) - *PUBH 613: Designs, Concepts, and Methods in Public Health Research*
2. **Amena El Harakeh** (Adjunct Lecturer) - *PUBH 613: Designs, Concepts, and Methods in Public Health Research*
3. **Tony DeVito** (Adjunct Lecturer) - *PUBH 614: Quantitative and Qualitative Data Analysis Methods in Public Health Research*
4. **Priscilla Lopez D'Antico** (Adjunct Assistant Professor) - *PUBH 614: Quantitative and Qualitative Data Analysis Methods in Public Health Research* & *EPID 622: Applied Research: Data Management and Analysis*
5. **Mukta Mohnani** (Adjunct Lecturer) - *PUBH 614: Quantitative and Qualitative Data Analysis Methods in Public Health Research*
6. **David Goldfarb** (Adjunct Assistant Professor) - *EPID 620 / PUBH 801: Epidemiological Methods I*
7. **Rehana Rasul** (Adjunct Lecturer) - *EPID 621: Epidemiological Methods II*
8. **Jenny Shen** (Adjunct Lecturer) - *BIOS 621: Applied Biostatistics II*
9. **Madelyn Carlson** (Adjunct Lecturer) - *EPID 622: Applied Research: Data Management and Analysis*
10. **Jose Fernando Florez-Arango** (Adjunct Assistant Professor) - *EPID 633: Design and Development of Population Health Information Systems*
11. **Kimberly Sebek** (Adjunct Lecturer) - *EPID 695/895: Database Design and Use*
12. **Ludwig Geistlinger** (Adjunct Associate Professor) - *EPID 695/895: Programming AI for Public Health and Biomedical Sciences*
13. **Haoyan Zhong** (Adjunct Lecturer) - *PUBH 696: Supervised Fieldwork*
14. **Chloe Mirzayi** (Adjunct Assistant Professor) - *PUBH 698: Capstone Project*
15. **Lisa Hitch** (Adjunct Lecturer) - *BIOS 620: Applied Biostatistics I*

*(Details to be extracted from previous XML presence: CUNY SPH Profile & Google Scholar links)*

---

## 4. Extracted Affiliated Faculty Data

1. **Theresa Diaz, MD, MPH**
   - **Title & Affiliation:** Unit Chief, Epidemiology, Monitoring and Evaluation (EME) unit within the Maternal, Newborn, Child and Adolescent Health and Ageing (MCA) Department, World Health Organization (WHO)
   - **Contact:** tdiaz1000@gmail.com
   - **Bio Link:** [CUNY ISPH Profile](https://cunyisph.org/team/theresa-diaz/)
   - **Google Scholar:** `-b6BASwAAAAJ`
   - **Contributions & Collaborations:** Co-teaching implementation science course; collaborating on grant proposals with ISPH; hosting student practicums/fieldwork; serving on dissertation committees. Connects the department to global public health practice.

---

## 5. Missing Data Required to Proceed

Before Gemini can execute the XML manipulation script, please provide the following details (if applicable, otherwise we can proceed with basic generation):

1. **Adjunct Bios (Optional)**: For the adjuncts listed above, I will generate a minimal bio stating their title and the courses they teach. If you have full bios or Scholar IDs for the rest of them, please provide them.
2. **Faculty Usernames (Optional)**: If you want these pages mapped directly to their CUNY Commons accounts upon import, please provide their CUNY email addresses or usernames. Otherwise, they will be assigned to your default admin account and can be reassigned later.
