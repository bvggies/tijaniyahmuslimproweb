#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read footer from index.html (homepage)
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract footer (from <footer class="bde-section-28-100" to </footer>)
footer_start = index_content.find('<footer class="bde-section-28-100')
footer_end = index_content.find('</footer>', footer_start) + len('</footer>')
homepage_footer = index_content[footer_start:footer_end]

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
    print(f"Processing {page_path}...")
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all footer tags
    footer_positions = []
    start_pos = 0
    while True:
        pos = content.find('<footer', start_pos)
        if pos == -1:
            break
        end_pos = content.find('</footer>', pos) + len('</footer>')
        footer_positions.append((pos, end_pos))
        start_pos = end_pos
    
    if len(footer_positions) == 0:
        print(f"  ✗ No footer found")
        continue
    
    # Remove all footers
    for start, end in reversed(footer_positions):
        content = content[:start] + content[end:]
        print(f"  ✓ Removed footer at position {start}-{end}")
    
    # Add homepage footer at the end (before </body>)
    body_end = content.rfind('</body>')
    if body_end == -1:
        print(f"  ✗ </body> tag not found")
        continue
    
    new_footer = adjust_paths(homepage_footer, True)
    content = content[:body_end] + '\n    ' + new_footer + '\n' + content[body_end:]
    print(f"  ✓ Added homepage footer")
    
    # Write back
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Updated {page_path}\n")

print("All pages updated successfully!")

