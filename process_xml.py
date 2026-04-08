import os
import csv
import xml.etree.ElementTree as ET
import datetime

# --- 1. Configuration & Data ---
INPUT_XML = 'site-export.xml'
OUTPUT_XML = 'site-export_processed.xml'
PARENT_PAGE_ID = '267'  # ID for 'Faculty' page

# Names of the 13 full-time faculty already in the XML
FULL_TIME_FACULTY = [
    "Luisa N Borrell", "Ayman El-Mohandes", "Renee Goodwin",
    "Heidi E Jones", "Elizabeth Kelvin", "Denis Nash", "Sehyun Oh",
    "Nash Rochman", "Zach Shahn", "Chloe Teasdale", "Levi Waldron",
    "Katarzyna Wyka", "Constantin T Yiannoutsos", "Luisa N. Borrell", "Heidi E. Jones", "Katarzyna E Wyka"
]

# Affiliated Faculty Data
AFFILIATED_FACULTY = [
    {
        "name": "Theresa Diaz",
        "title": "Unit Chief, Epidemiology, Monitoring and Evaluation (EME) unit within the Maternal, Newborn, Child and Adolescent Health and Ageing (MCA) Department, World Health Organization (WHO)",
        "email": "tdiaz1000@gmail.com",
        "bio_link": "https://cunyisph.org/team/theresa-diaz/",
        "scholar_id": "-b6BASwAAAAJ",
        "contributions": "Co-teaching implementation science course; collaborating on grant proposals with ISPH; hosting student practicums/fieldwork; serving on dissertation committees. Connects the department to global public health practice."
    }
]

# --- 2. Helper Functions ---

def create_username(name):
    # e.g., "Lisa Hitch" -> "lisahitch"
    return name.lower().replace(" ", "").replace(".", "").replace("'", "")

def create_slug(name):
    # e.g., "Lisa Hitch" -> "lisa-hitch"
    return name.lower().replace(" ", "-").replace(".", "").replace("'", "")

def generate_bio_html(faculty_data, faculty_type):
    name = faculty_data.get('name')
    title = faculty_data.get('title', '')
    courses = faculty_data.get('courses', [])
    scholar_id = faculty_data.get('scholar_id')
    bio_link = faculty_data.get('bio_link')
    contributions = faculty_data.get('contributions')
    
    # Check for photo
    photo_path = f"photos/{create_slug(name)}.jpg"
    photo_placeholder = ""
    if os.path.exists(photo_path):
         photo_placeholder = f"\n<!-- IMAGE UPLOAD REQUIRED: {photo_path} -->\n<p><em>[Photo available: Please upload {photo_path} as Featured Image]</em></p>\n"

    html = f"<!-- wp:paragraph -->\n<p class=\"faculty-title\"><strong>{title}</strong></p>\n<!-- /wp:paragraph -->\n"
    html += photo_placeholder
    
    if courses:
        html += "\n<!-- wp:heading -->\n<h3>Courses Taught</h3>\n<!-- /wp:heading -->\n<!-- wp:list -->\n<ul>\n"
        for course in courses:
            html += f"<li>{course}</li>\n"
        html += "</ul>\n<!-- /wp:list -->\n"
        
    if contributions:
        html += f"\n<!-- wp:heading -->\n<h3>Contributions & Collaborations</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>{contributions}</p>\n<!-- /wp:paragraph -->\n"

    if bio_link:
        html += f"\n<!-- wp:paragraph -->\n<p><a href=\"{bio_link}\" target=\"_blank\">View Full Profile</a></p>\n<!-- /wp:paragraph -->\n"

    if scholar_id:
        html += f"\n<!-- wp:heading -->\n<h3>Selected Publications</h3>\n<!-- /wp:heading -->\n<!-- wp:shortcode -->\n[schopufe_publications user_id=\"{scholar_id}\" cache_hours=24]\n<!-- /wp:shortcode -->\n"

    return html

def create_acf_meta(key, value):
    meta = ET.Element('{http://wordpress.org/export/1.2/}postmeta')
    k = ET.SubElement(meta, '{http://wordpress.org/export/1.2/}meta_key')
    k.text = key
    v = ET.SubElement(meta, '{http://wordpress.org/export/1.2/}meta_value')
    v.text = f"__CDATA_START__{value}__CDATA_END__"
    return meta

def create_faculty_item(faculty_data, type_val, max_post_id):
    name = faculty_data['name']
    username = create_username(name)
    slug = create_slug(name)
    
    item = ET.Element('item')
    
    title = ET.SubElement(item, 'title')
    title.text = name
    
    link = ET.SubElement(item, 'link')
    link.text = f"https://epibios.commons.gc.cuny.edu/faculty/{slug}/"
    
    now = datetime.datetime.now(datetime.timezone.utc)
    pubDate = ET.SubElement(item, 'pubDate')
    pubDate.text = now.strftime("%a, %d %b %Y %H:%M:%S +0000")
    
    creator = ET.SubElement(item, '{http://purl.org/dc/elements/1.1/}creator')
    creator.text = f"__CDATA_START__{username}__CDATA_END__"
    
    guid = ET.SubElement(item, 'guid', {'isPermaLink': 'false'})
    guid.text = f"https://epibios.commons.gc.cuny.edu/?page_id={max_post_id}"
    
    desc = ET.SubElement(item, 'description')
    desc.text = ""
    
    content = ET.SubElement(item, '{http://purl.org/rss/1.0/modules/content/}encoded')
    content_html = generate_bio_html(faculty_data, type_val)
    content.text = f"__CDATA_START__{content_html}__CDATA_END__"
    
    excerpt = ET.SubElement(item, '{http://wordpress.org/export/1.2/excerpt/}encoded')
    excerpt.text = "__CDATA_START____CDATA_END__"
    
    post_id = ET.SubElement(item, '{http://wordpress.org/export/1.2/}post_id')
    post_id.text = str(max_post_id)
    
    post_date = ET.SubElement(item, '{http://wordpress.org/export/1.2/}post_date')
    post_date.text = now.strftime("%Y-%m-%d %H:%M:%S")
    
    post_date_gmt = ET.SubElement(item, '{http://wordpress.org/export/1.2/}post_date_gmt')
    post_date_gmt.text = now.strftime("%Y-%m-%d %H:%M:%S")
    
    post_name = ET.SubElement(item, '{http://wordpress.org/export/1.2/}post_name')
    post_name.text = f"__CDATA_START__{slug}__CDATA_END__"
    
    status = ET.SubElement(item, '{http://wordpress.org/export/1.2/}status')
    status.text = "publish"
    
    post_parent = ET.SubElement(item, '{http://wordpress.org/export/1.2/}post_parent')
    post_parent.text = PARENT_PAGE_ID
    
    menu_order = ET.SubElement(item, '{http://wordpress.org/export/1.2/}menu_order')
    menu_order.text = "0"
    
    post_type = ET.SubElement(item, '{http://wordpress.org/export/1.2/}post_type')
    post_type.text = "page"
    
    post_password = ET.SubElement(item, '{http://wordpress.org/export/1.2/}post_password')
    post_password.text = ""
    
    is_sticky = ET.SubElement(item, '{http://wordpress.org/export/1.2/}is_sticky')
    is_sticky.text = "0"
    
    item.append(create_acf_meta('faculty_type', type_val))
    
    return item

# --- 3. CSV Data as dict since file is missing ---
adjuncts = {
    'Fiona Fogarty': {'name': 'Fiona Fogarty', 'title': 'Adjunct Lecturer', 'courses': ['PUBH 613: Designs, Concepts, and Methods in Public Health Research']},
    'Amena El Harakeh': {'name': 'Amena El Harakeh', 'title': 'Adjunct Lecturer', 'courses': ['PUBH 613: Designs, Concepts, and Methods in Public Health Research']},
    'Tony DeVito': {'name': 'Tony DeVito', 'title': 'Adjunct Lecturer', 'courses': ['PUBH 614: Quantitative and Qualitative Data Analysis Methods in Public Health Research']},
    "Priscilla Lopez D'Antico": {'name': "Priscilla Lopez D'Antico", 'title': 'Adjunct Assistant Professor', 'courses': ['PUBH 614: Quantitative and Qualitative Data Analysis Methods in Public Health Research', 'EPID 622: Applied Research: Data Management and Analysis']},
    'Mukta Mohnani': {'name': 'Mukta Mohnani', 'title': 'Adjunct Lecturer', 'courses': ['PUBH 614: Quantitative and Qualitative Data Analysis Methods in Public Health Research']},
    'David Goldfarb': {'name': 'David Goldfarb', 'title': 'Adjunct Assistant Professor', 'courses': ['EPID 620 / PUBH 801: Epidemiological Methods I']},
    'Rehana Rasul': {'name': 'Rehana Rasul', 'title': 'Adjunct Lecturer', 'courses': ['EPID 621: Epidemiological Methods II']},
    'Jenny Shen': {'name': 'Jenny Shen', 'title': 'Adjunct Lecturer', 'courses': ['BIOS 621: Applied Biostatistics II']},
    'Madelyn Carlson': {'name': 'Madelyn Carlson', 'title': 'Adjunct Lecturer', 'courses': ['EPID 622: Applied Research: Data Management and Analysis']},
    'Jose Fernando Florez-Arango': {'name': 'Jose Fernando Florez-Arango', 'title': 'Adjunct Assistant Professor', 'courses': ['EPID 633: Design and Development of Population Health Information Systems']},
    'Kimberly Sebek': {'name': 'Kimberly Sebek', 'title': 'Adjunct Lecturer', 'courses': ['EPID 695/895: Database Design and Use']},
    'Ludwig Geistlinger': {'name': 'Ludwig Geistlinger', 'title': 'Adjunct Associate Professor', 'courses': ['EPID 695/895: Programming AI for Public Health and Biomedical Sciences']},
    'Haoyan Zhong': {'name': 'Haoyan Zhong', 'title': 'Adjunct Lecturer', 'courses': ['PUBH 696: Supervised Fieldwork']},
    'Chloe Mirzayi': {'name': 'Chloe Mirzayi', 'title': 'Adjunct Assistant Professor', 'courses': ['PUBH 698: Capstone Project']},
    'Lisa Hitch': {'name': 'Lisa Hitch', 'title': 'Adjunct Lecturer', 'courses': ['BIOS 620: Applied Biostatistics I'], 'scholar_id': 'odQAFhcAAAAJ'}
}

# --- 4. Process XML ---
print("Parsing XML...")
ET.register_namespace('excerpt', "http://wordpress.org/export/1.2/excerpt/")
ET.register_namespace('content', "http://purl.org/rss/1.0/modules/content/")
ET.register_namespace('wfw', "http://wellformedweb.org/CommentAPI/")
ET.register_namespace('dc', "http://purl.org/dc/elements/1.1/")
ET.register_namespace('wp', "http://wordpress.org/export/1.2/")

tree = ET.parse(INPUT_XML)
root = tree.getroot()
channel = root.find('channel')

max_id = 0
for item in channel.findall('item'):
    post_id_elem = item.find('{http://wordpress.org/export/1.2/}post_id')
    if post_id_elem is not None and post_id_elem.text.isdigit():
        max_id = max(max_id, int(post_id_elem.text))

ft_count = 0
for item in channel.findall('item'):
    title_elem = item.find('title')
    post_type_elem = item.find('{http://wordpress.org/export/1.2/}post_type')
    
    if title_elem is not None and post_type_elem is not None and post_type_elem.text == 'page':
        if title_elem.text in FULL_TIME_FACULTY:
            has_type = False
            for meta in item.findall('{http://wordpress.org/export/1.2/}postmeta'):
                key = meta.find('{http://wordpress.org/export/1.2/}meta_key')
                if key is not None and key.text == 'faculty_type':
                    has_type = True
                    break
            
            if not has_type:
                item.append(create_acf_meta('faculty_type', 'Full-time'))
                ft_count += 1

print(f"Injected 'Full-time' ACF metadata into {ft_count} existing faculty pages.")

adj_count = 0
for name, data in adjuncts.items():
    max_id += 1
    new_item = create_faculty_item(data, 'Adjunct', max_id)
    channel.append(new_item)
    adj_count += 1
print(f"Generated {adj_count} new Adjunct faculty pages.")

aff_count = 0
for data in AFFILIATED_FACULTY:
    max_id += 1
    new_item = create_faculty_item(data, 'Affiliated', max_id)
    channel.append(new_item)
    aff_count += 1
print(f"Generated {aff_count} new Affiliated faculty pages.")

print("Saving modified XML...")
tree.write(OUTPUT_XML, encoding='utf-8', xml_declaration=True)

with open(OUTPUT_XML, 'r', encoding='utf-8') as f:
    xml_str = f.read()

xml_str = xml_str.replace('__CDATA_START__', '<![CDATA[')
xml_str = xml_str.replace('__CDATA_END__', ']]>')

# Handle ElementTree namespace mangling on new elements
xml_str = xml_str.replace('<ns0:', '<wp:')
xml_str = xml_str.replace('</ns0:', '</wp:')
xml_str = xml_str.replace('<ns1:', '<dc:')
xml_str = xml_str.replace('</ns1:', '</dc:')
xml_str = xml_str.replace('<ns2:', '<content:')
xml_str = xml_str.replace('</ns2:', '</content:')
xml_str = xml_str.replace('<ns3:', '<excerpt:')
xml_str = xml_str.replace('</ns3:', '</excerpt:')

with open(OUTPUT_XML, 'w', encoding='utf-8') as f:
    f.write(xml_str)

print(f"Done! New XML saved to: {OUTPUT_XML}")
