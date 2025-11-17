#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read homepage
with open('index.html', 'r', encoding='utf-8') as f:
    homepage_content = f.read()

# Extract header (from <header to </header>)
header_start = homepage_content.find('<header class="bde-header-builder-25-100')
header_end = homepage_content.find('</header>', header_start) + len('</header>')
homepage_header = homepage_content[header_start:header_end]

# Extract footer (from <footer to </footer>)
footer_start = homepage_content.find('<footer class="bde-section-28-100')
footer_end = homepage_content.find('</footer>', footer_start) + len('</footer>')
homepage_footer = homepage_content[footer_start:footer_end]

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

# Pages to update
pages = [
    'about-us/index.html',
    'contact-us/index.html',
    'privacy-policy/index.html',
    'terms/index.html',
]

for page_path in pages:
    print(f"Updating {page_path}...")
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_subdir = '/' in page_path
    
    # Remove existing header
    header_start_idx = content.find('<header')
    if header_start_idx != -1:
        header_end_idx = content.find('</header>', header_start_idx) + len('</header>')
        content = content[:header_start_idx] + content[header_end_idx:]
        print(f"  ✓ Removed old header")
    
    # Remove existing footer
    footer_start_idx = content.find('<footer')
    if footer_start_idx != -1:
        footer_end_idx = content.find('</footer>', footer_start_idx) + len('</footer>')
        content = content[:footer_start_idx] + content[footer_end_idx:]
        print(f"  ✓ Removed old footer")
    
    # Insert homepage header after <body>
    body_start = content.find('<body')
    if body_start != -1:
        body_tag_end = content.find('>', body_start) + 1
        adjusted_header = adjust_paths(homepage_header, is_subdir)
        content = content[:body_tag_end] + '\n    ' + adjusted_header + '\n' + content[body_tag_end:]
        print(f"  ✓ Added homepage header")
    
    # Insert homepage footer before </body>
    body_end = content.rfind('</body>')
    if body_end != -1:
        adjusted_footer = adjust_paths(homepage_footer, is_subdir)
        content = content[:body_end] + '\n    ' + adjusted_footer + '\n' + content[body_end:]
        print(f"  ✓ Added homepage footer")
    
    # Ensure stylesheets are included
    if 'styles-muslimpro.css' not in content and not is_subdir:
        head_end = content.rfind('</head>')
        if head_end != -1:
            stylesheet = '    <link type="text/css" media="all" href="styles-muslimpro.css" rel="stylesheet" />\n'
            content = content[:head_end] + stylesheet + content[head_end:]
    elif 'styles-muslimpro.css' not in content and is_subdir:
        head_end = content.rfind('</head>')
        if head_end != -1:
            stylesheet = '    <link type="text/css" media="all" href="../styles-muslimpro.css" rel="stylesheet" />\n'
            content = content[:head_end] + stylesheet + content[head_end:]
    
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Updated {page_path}\n")

print("All pages updated with homepage header and footer!")

