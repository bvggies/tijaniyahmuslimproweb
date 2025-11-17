#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read header and footer from index.html (homepage)
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header
header_start = index_content.find('<header class="bde-header-builder-25-100')
header_end = index_content.find('</header>', header_start) + len('</header>')
header_content = index_content[header_start:header_end]

# Extract footer
footer_start = index_content.find('<footer class="bde-section-28-100')
footer_end = index_content.find('</footer>', footer_start) + len('</footer>')
footer_content = index_content[footer_start:footer_end]

# Create clean head section template
head_template = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"/>
    <link rel="canonical" href="{canonical}" />
    <link rel="icon" href="{favicon}" sizes="32x32" />
    <link rel="icon" href="{favicon}" sizes="192x192" />
    <link rel="apple-touch-icon" href="{favicon}" />
    <link type="text/css" media="all" href="{styles_muslimpro}" rel="stylesheet" />
    <link rel="stylesheet" href="{styles_css}" />
</head>
"""

# Function to adjust paths for subdirectories
def adjust_paths(html_content, is_subdirectory):
    if not is_subdirectory:
        return html_content
    
    # Adjust asset paths
    html_content = html_content.replace('src="assets/', 'src="../assets/')
    html_content = html_content.replace('href="assets/', 'href="../assets/')
    
    # Adjust page links - be careful with order (longer paths first)
    html_content = html_content.replace('href="winter-aid/index.html"', 'href="../winter-aid/index.html"')
    html_content = html_content.replace('href="about-us/index.html"', 'href="../about-us/index.html"')
    html_content = html_content.replace('href="contact-us/index.html"', 'href="../contact-us/index.html"')
    html_content = html_content.replace('href="privacy-policy/index.html"', 'href="../privacy-policy/index.html"')
    html_content = html_content.replace('href="terms/index.html"', 'href="../terms/index.html"')
    html_content = html_content.replace('href="features/index.html"', 'href="../features/index.html"')
    html_content = html_content.replace('href="ummah-pro/index.html"', 'href="../ummah-pro/index.html"')
    html_content = html_content.replace('href="academy-islamic-courses/index.html"', 'href="../academy-islamic-courses/index.html"')
    html_content = html_content.replace('href="advertise/index.html"', 'href="../advertise/index.html"')
    html_content = html_content.replace('href="cookies-policy/index.html"', 'href="../cookies-policy/index.html"')
    html_content = html_content.replace('href="index.html"', 'href="../index.html"')
    
    return html_content

# Page templates - empty content
pages = [
    {
        'path': 'about-us/index.html',
        'title': 'About Us | Tijaniyah Muslim Pro',
        'description': 'Learn about Tijaniyah Muslim Pro - your trusted Islamic app companion providing prayer times, Quran, and Islamic resources to Muslims worldwide.',
        'is_subdir': True
    },
    {
        'path': 'contact-us/index.html',
        'title': 'Contact Us | Tijaniyah Muslim Pro',
        'description': 'Get in touch with Tijaniyah Muslim Pro. We\'re here to help with any questions or support you need.',
        'is_subdir': True
    },
    {
        'path': 'privacy-policy/index.html',
        'title': 'Privacy Policy | Tijaniyah Muslim Pro',
        'description': 'Read Tijaniyah Muslim Pro\'s Privacy Policy to understand how we collect, use, and protect your personal information.',
        'is_subdir': True
    },
    {
        'path': 'terms/index.html',
        'title': 'Terms of Use | Tijaniyah Muslim Pro',
        'description': 'Read Tijaniyah Muslim Pro\'s Terms of Use to understand the terms and conditions for using our services.',
        'is_subdir': True
    }
]

# Generate empty pages
for page in pages:
    # Build head section
    base_path = '../' if page['is_subdir'] else ''
    canonical = f"{base_path}{page['path']}" if page['is_subdir'] else page['path']
    favicon = f"{base_path}assets/App logo.png"
    styles_muslimpro = f"{base_path}styles-muslimpro.css"
    styles_css = f"{base_path}styles.css"
    
    head_section = head_template.format(
        title=page['title'],
        description=page['description'],
        canonical=canonical,
        favicon=favicon,
        styles_muslimpro=styles_muslimpro,
        styles_css=styles_css
    )
    
    header = adjust_paths(header_content, page['is_subdir'])
    footer = adjust_paths(footer_content, page['is_subdir'])
    
    # Empty content - just header and footer
    html = f"""<!DOCTYPE html>
<html lang="en-US">
{head_section}
<body class="page-template-default page">
    {header}
    
    <!-- Content will be added here -->
    
    {footer}
</body>
</html>
"""
    
    with open(page['path'], 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Cleared {page['path']}")

print("\nAll pages cleared successfully!")

