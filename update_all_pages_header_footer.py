#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read header and footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header (from first <header> to </header>)
header_start = content.find('<header class="bde-header-builder-25-100')
header_end = content.find('</header>', header_start) + len('</header>')
header_content = content[header_start:header_end]

# Extract footer (from <footer to </footer>)
footer_start = content.find('<footer class="bde-section-28-100')
footer_end = content.find('</footer>', footer_start) + len('</footer>')
footer_content = content[footer_start:footer_end]

# Remove duplicate second header from index.html
second_header_start = content.find('</header><header class="bde-header-builder-25-172')
if second_header_start != -1:
    second_header_end = content.find('</header>', second_header_start + len('</header>')) + len('</header>')
    content = content[:second_header_start + len('</header>')] + content[second_header_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Removed duplicate header from index.html")

# Function to adjust paths for subdirectories
def adjust_paths(html_content, is_subdirectory):
    if not is_subdirectory:
        return html_content
    
    # Adjust asset paths
    html_content = html_content.replace('src="assets/', 'src="../assets/')
    html_content = html_content.replace('href="assets/', 'href="../assets/')
    
    # Adjust page links
    html_content = html_content.replace('href="index.html"', 'href="../index.html"')
    html_content = html_content.replace('href="about-us/index.html"', 'href="../about-us/index.html"')
    html_content = html_content.replace('href="contact-us/index.html"', 'href="../contact-us/index.html"')
    html_content = html_content.replace('href="privacy-policy/index.html"', 'href="../privacy-policy/index.html"')
    html_content = html_content.replace('href="terms/index.html"', 'href="../terms/index.html"')
    html_content = html_content.replace('href="features/index.html"', 'href="../features/index.html"')
    html_content = html_content.replace('href="winter-aid/index.html"', 'href="../winter-aid/index.html"')
    
    return html_content

# Update all pages
pages = [
    ('index.html', False),
    ('about-us/index.html', True),
    ('contact-us/index.html', True),
    ('privacy-policy/index.html', True),
    ('terms/index.html', True),
]

for page_path, is_subdir in pages:
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            page_content = f.read()
        
        # Replace header placeholder or old header
        if '<div id="header-placeholder"></div>' in page_content:
            page_content = page_content.replace('<div id="header-placeholder"></div>', adjust_paths(header_content, is_subdir))
        elif '<header' in page_content and 'bde-header-builder-25-100' not in page_content:
            # Find and replace old header
            old_header_start = page_content.find('<header')
            if old_header_start != -1:
                old_header_end = page_content.find('</header>', old_header_start) + len('</header>')
                page_content = page_content[:old_header_start] + adjust_paths(header_content, is_subdir) + page_content[old_header_end:]
        
        # Replace footer placeholder or old footer
        if '<div id="footer-placeholder"></div>' in page_content:
            page_content = page_content.replace('<div id="footer-placeholder"></div>', adjust_paths(footer_content, is_subdir))
        elif '<footer' in page_content and 'bde-section-28-100' not in page_content:
            # Find and replace old footer
            old_footer_start = page_content.find('<footer')
            if old_footer_start != -1:
                old_footer_end = page_content.find('</footer>', old_footer_start) + len('</footer>')
                page_content = page_content[:old_footer_start] + adjust_paths(footer_content, is_subdir) + page_content[old_footer_end:]
        
        # Remove JavaScript loader script
        page_content = page_content.replace('<script src="load-header-footer.js" defer></script>', '')
        page_content = page_content.replace('<script src="../load-header-footer.js" defer></script>', '')
        
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        print(f"Updated {page_path}")
    except Exception as e:
        print(f"Error updating {page_path}: {e}")

print("Done updating all pages!")

