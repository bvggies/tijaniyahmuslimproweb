#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read header and footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header (from first <header> to </header>)
header_start = index_content.find('<header class="bde-header-builder-25-100')
header_end = index_content.find('</header>', header_start) + len('</header>')
header_content = index_content[header_start:header_end]

# Extract footer (from <footer to </footer>)
footer_start = index_content.find('<footer class="bde-section-28-100')
footer_end = index_content.find('</footer>', footer_start) + len('</footer>')
footer_content = index_content[footer_start:footer_end]

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
    print(f"Processing {page_path}...")
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace header
    header_start_idx = content.find('<header class="bde-header-builder-25-100')
    if header_start_idx != -1:
        header_end_idx = content.find('</header>', header_start_idx) + len('</header>')
        new_header = adjust_paths(header_content, True)
        content = content[:header_start_idx] + new_header + content[header_end_idx:]
        print(f"  ✓ Replaced header")
    else:
        print(f"  ✗ Header not found")
    
    # Find and replace footer
    footer_start_idx = content.find('<footer class="bde-section-28-100')
    if footer_start_idx != -1:
        footer_end_idx = content.find('</footer>', footer_start_idx) + len('</footer>')
        new_footer = adjust_paths(footer_content, True)
        content = content[:footer_start_idx] + new_footer + content[footer_end_idx:]
        print(f"  ✓ Replaced footer")
    else:
        print(f"  ✗ Footer not found")
    
    # Write back
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Updated {page_path}\n")

print("All pages updated successfully!")

