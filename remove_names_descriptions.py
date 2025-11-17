#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start and end of the blog posts section
start_marker = '<div class="bde-loop bde-loop-grid ee-posts ee-posts-grid">'
end_marker = '</div></div></div></section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers")
    exit(1)

# Extract the section
section_content = content[start_idx:end_idx]

# Remove all h3 titles and descriptions from each article
import re

# Pattern to match and remove title and description
pattern = r'<div class="bde-loop-item__wrap ee-post-wrap">\s*<h3 class="ee-post-title">.*?</h3>\s*<div class="bde-loop-item__content ee-post-content">.*?</div>\s*</div>'

# Replace with empty wrap div (or remove it entirely)
# Let's remove the wrap div completely
new_section = re.sub(pattern, '', section_content, flags=re.DOTALL)

# Replace the section in the content
content = content[:start_idx] + new_section + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Removed names and descriptions from Complete Islamic Companion section")
