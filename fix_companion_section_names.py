#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Updated names and descriptions
updates = [
    {
        'old_title': 'Home & Dashboard',
        'new_title': 'Prayer Times & Qibla',
        'old_desc': 'Your personalized Islamic dashboard with prayer times, Qibla direction, and quick access to all features.',
        'new_desc': 'Never miss a prayer with accurate, location-based prayer times. Find the Qibla direction and stay connected to your faith.'
    },
    {
        'old_title': 'Holy Quran',
        'new_title': 'Read the Holy Quran',
        'old_desc': 'Read and listen to the complete Holy Quran with translations, tafsir, and recitations from renowned Qaris.',
        'new_desc': 'Access the complete Holy Quran with multiple translations, beautiful Arabic text, and powerful search capabilities. Bookmark your favorite verses.'
    },
    {
        'old_title': 'Duas & Supplications',
        'new_title': 'Duas & Supplications',
        'old_desc': 'Access a comprehensive collection of authentic duas for daily life, special occasions, and spiritual moments.',
        'new_desc': 'Comprehensive collection of Islamic prayers and supplications for every occasion. Access authentic duas with Arabic text, transliteration, and translations.'
    },
    {
        'old_title': 'AI Noor',
        'new_title': 'AI Noor - Your AI-Powered Islamic Assistant',
        'old_desc': 'Your intelligent Islamic companion powered by AI, ready to answer questions about Islam based on authentic sources.',
        'new_desc': 'Get instant answers to your Islamic questions with our AI-powered assistant. AI Noor provides authentic, scholar-verified responses to help you on your spiritual journey.'
    },
    {
        'old_title': 'Hajj & Umrah Guide',
        'new_title': 'Hajj & Umrah Guide',
        'old_desc': 'Complete guide for performing Hajj and Umrah with step-by-step instructions, maps, and supplications.',
        'new_desc': 'Complete guide for performing Hajj and Umrah with step-by-step instructions, maps, supplications, and essential information for your pilgrimage.'
    },
    {
        'old_title': 'Islamic Lessons',
        'new_title': 'Islamic Lessons & Courses',
        'old_desc': 'Learn from authentic Islamic courses, lectures, and educational content to deepen your understanding of Islam.',
        'new_desc': 'Learn from comprehensive Islamic courses, lectures, and educational content to deepen your understanding of Islam and strengthen your faith.'
    },
    {
        'old_title': 'Community',
        'new_title': 'Community & Social',
        'old_desc': 'Connect with fellow Muslims, share experiences, and participate in community activities and discussions.',
        'new_desc': 'Connect with fellow Muslims worldwide, share experiences, participate in community activities, and build meaningful connections with the Ummah.'
    },
    {
        'old_title': 'Scholars & Guidance',
        'new_title': 'Scholars & Islamic Guidance',
        'old_desc': 'Access guidance from renowned Islamic scholars and get answers to your religious questions.',
        'new_desc': 'Access guidance from renowned Islamic scholars and teachers. Learn from authentic sources and get answers to your religious questions.'
    },
    {
        'old_title': 'Makkah Live',
        'new_title': 'Makkah Live Stream',
        'old_desc': 'Watch live streams from the Holy Kaaba in Makkah and feel connected to the sacred city anytime, anywhere.',
        'new_desc': 'Watch live streams from the Holy Kaaba in Makkah. Feel connected to the sacred city anytime, anywhere, and witness the beauty of the Haram.'
    },
    {
        'old_title': 'Zakat Calculator',
        'new_title': 'Zakat Calculator & Donations',
        'old_desc': 'Calculate your Zakat accurately and make donations to support those in need through verified channels.',
        'new_desc': 'Calculate your Zakat accurately and make donations to support those in need through verified and trusted channels. Fulfill your Islamic obligations with ease.'
    },
    {
        'old_title': 'Tijaniyah Features',
        'new_title': 'Tijaniyah Spiritual Features',
        'old_desc': 'Explore unique Tijaniyah-specific features and spiritual tools designed for your journey.',
        'new_desc': 'Explore unique Tijaniyah-specific features and spiritual tools designed to enhance your spiritual journey and strengthen your connection with Allah.'
    },
    {
        'old_title': 'More Features',
        'new_title': 'Additional Features',
        'old_desc': 'Discover additional tools including digital tasbih, Islamic calendar, mosque locator, and more.',
        'new_desc': 'Discover additional powerful tools including digital tasbih, Islamic calendar, mosque locator, Wazifa tracker, Islamic journal, and much more.'
    }
]

# Apply updates
for update in updates:
    # Replace title
    old_title_tag = f'<h3 class="ee-post-title">{update["old_title"]}</h3>'
    new_title_tag = f'<h3 class="ee-post-title">{update["new_title"]}</h3>'
    content = content.replace(old_title_tag, new_title_tag)
    
    # Replace description
    old_desc_tag = f'<div class="bde-loop-item__content ee-post-content">\n                {update["old_desc"]}\n            </div>'
    new_desc_tag = f'<div class="bde-loop-item__content ee-post-content">\n                {update["new_desc"]}\n            </div>'
    content = content.replace(old_desc_tag, new_desc_tag)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated names and descriptions in Complete Islamic Companion section")

