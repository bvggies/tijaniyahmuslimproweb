#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find line numbers
start_line = None
end_line = None
button_start = None
button_end = None

for i, line in enumerate(lines):
    if '<div class="bde-loop bde-loop-grid ee-posts ee-posts-grid">' in line:
        start_line = i
    if '</div>' in line and i > start_line and start_line is not None:
        # Check if this is the closing div for the loop
        if i > start_line + 10:  # Make sure we're past the articles
            # Check next few lines for the section closing
            if i + 2 < len(lines) and '</section>' in lines[i+2]:
                end_line = i + 2
                break
    if '<section class="bde-section-38-410' in line:
        button_start = i
    if button_start and '</section>' in line and i > button_start:
        button_end = i
        break

print(f"Start: {start_line}, End: {end_line}, Button start: {button_start}, Button end: {button_end}")

if start_line is None or end_line is None:
    print("Could not find markers")
    exit(1)

# New content
new_articles = '''    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/home screen.PNG" class="attachment-full size-full wp-post-image" alt="Home Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Home & Dashboard</h3>
            <div class="bde-loop-item__content ee-post-content">
                Your personalized Islamic dashboard with prayer times, Qibla direction, and quick access to all features.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/quran screen.jpg" class="attachment-full size-full wp-post-image" alt="Quran Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Holy Quran</h3>
            <div class="bde-loop-item__content ee-post-content">
                Read and listen to the complete Holy Quran with translations, tafsir, and recitations from renowned Qaris.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/duas screen.jpg" class="attachment-full size-full wp-post-image" alt="Duas Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Duas & Supplications</h3>
            <div class="bde-loop-item__content ee-post-content">
                Access a comprehensive collection of authentic duas for daily life, special occasions, and spiritual moments.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/hajj screen.jpg" class="attachment-full size-full wp-post-image" alt="Hajj Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Hajj & Umrah Guide</h3>
            <div class="bde-loop-item__content ee-post-content">
                Complete guide for performing Hajj and Umrah with step-by-step instructions, maps, and supplications.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/lessons screen.jpg" class="attachment-full size-full wp-post-image" alt="Lessons Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Islamic Lessons</h3>
            <div class="bde-loop-item__content ee-post-content">
                Learn from authentic Islamic courses, lectures, and educational content to deepen your understanding of Islam.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/community screen.jpg" class="attachment-full size-full wp-post-image" alt="Community Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Community</h3>
            <div class="bde-loop-item__content ee-post-content">
                Connect with fellow Muslims, share experiences, and participate in community activities and discussions.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/scholars screen.PNG" class="attachment-full size-full wp-post-image" alt="Scholars Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Scholars & Guidance</h3>
            <div class="bde-loop-item__content ee-post-content">
                Access guidance from renowned Islamic scholars and get answers to your religious questions.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/ai noor screen.jpg" class="attachment-full size-full wp-post-image" alt="AI Noor Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">AI Noor</h3>
            <div class="bde-loop-item__content ee-post-content">
                Your intelligent Islamic companion powered by AI, ready to answer questions about Islam based on authentic sources.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/makkah live screen.PNG" class="attachment-full size-full wp-post-image" alt="Makkah Live Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Makkah Live</h3>
            <div class="bde-loop-item__content ee-post-content">
                Watch live streams from the Holy Kaaba in Makkah and feel connected to the sacred city anytime, anywhere.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/zakat screen.jpg" class="attachment-full size-full wp-post-image" alt="Zakat Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Zakat Calculator</h3>
            <div class="bde-loop-item__content ee-post-content">
                Calculate your Zakat accurately and make donations to support those in need through verified channels.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/tijaniyah features screen.PNG" class="attachment-full size-full wp-post-image" alt="Tijaniyah Features Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">Tijaniyah Features</h3>
            <div class="bde-loop-item__content ee-post-content">
                Explore unique Tijaniyah-specific features and spiritual tools designed for your journey.
            </div>
        </div>
    </article>
    <article class="bde-loop-item ee-post">
        <div class="bde-loop-item__image ee-post-image">
            <img src="assets/more features screen.PNG" class="attachment-full size-full wp-post-image" alt="More Features Screen" decoding="async" loading="lazy" style="width: 100%; height: auto; object-fit: cover;">
        </div>
        <div class="bde-loop-item__wrap ee-post-wrap">
            <h3 class="ee-post-title">More Features</h3>
            <div class="bde-loop-item__content ee-post-content">
                Discover additional tools including digital tasbih, Islamic calendar, mosque locator, and more.
            </div>
        </div>
    </article>
'''

# Replace articles (from start_line+1 to end_line-1)
new_lines = lines[:start_line+1] + [new_articles + '\n'] + lines[end_line:]

# Remove button section if found
if button_start and button_end:
    new_lines = new_lines[:button_start] + new_lines[button_end+1:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done!")

