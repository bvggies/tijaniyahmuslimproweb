#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read header and footer generation function
import sys
sys.path.append('.')
from create_modern_header_footer import generate_header_footer, modern_css

# Features Page CSS
features_css = """
    <style>
        :root {
            --primary-color: #1a472a;
            --primary-dark: #0f2e1a;
            --primary-light: #2d5a3d;
            --accent-color: #3d6b4d;
            --text-dark: #1a1a1a;
            --text-gray: #555555;
            --text-light: #888888;
            --bg-light: #f8f9fa;
            --bg-white: #ffffff;
            --border-color: #e9ecef;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.12);
            --shadow-lg: 0 8px 32px rgba(0,0,0,0.16);
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.7;
            color: var(--text-dark);
            background: var(--bg-white);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        /* Hero Section */
        .features-hero {
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-light) 50%, var(--accent-color) 100%);
            padding: 160px 20px 120px;
            text-align: center;
            color: white;
            position: relative;
            overflow: hidden;
        }
        
        .features-hero::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: rotate 20s linear infinite;
        }
        
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .features-hero-content {
            position: relative;
            z-index: 1;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        .features-hero h1 {
            font-size: clamp(3rem, 7vw, 5.5rem);
            font-weight: 800;
            margin-bottom: 24px;
            letter-spacing: -0.03em;
            line-height: 1.1;
        }
        
        .features-hero p {
            font-size: clamp(1.125rem, 2.5vw, 1.5rem);
            opacity: 0.95;
            line-height: 1.7;
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* Container */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Section */
        .features-section {
            padding: 100px 0;
        }
        
        .features-section-alt {
            background: var(--bg-light);
        }
        
        /* Feature Showcase */
        .feature-showcase {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
            margin-bottom: 80px;
        }
        
        .feature-showcase.reverse {
            grid-template-columns: 1fr 1fr;
        }
        
        .feature-showcase.reverse .feature-content {
            order: 2;
        }
        
        .feature-showcase.reverse .feature-image {
            order: 1;
        }
        
        .feature-content h2 {
            color: var(--primary-color);
            font-size: clamp(2rem, 4vw, 2.75rem);
            font-weight: 700;
            margin-bottom: 20px;
            line-height: 1.2;
        }
        
        .feature-content p {
            color: var(--text-gray);
            font-size: 1.125rem;
            line-height: 1.8;
            margin-bottom: 24px;
        }
        
        .feature-list {
            list-style: none;
            padding: 0;
            margin: 24px 0;
        }
        
        .feature-list li {
            color: var(--text-gray);
            font-size: 1.0625rem;
            line-height: 1.8;
            margin-bottom: 12px;
            padding-left: 28px;
            position: relative;
        }
        
        .feature-list li::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--primary-color);
            font-weight: 700;
            font-size: 1.2rem;
        }
        
        .feature-image {
            position: relative;
            border-radius: 24px;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            background: white;
            padding: 20px;
        }
        
        .feature-image img {
            width: 100%;
            height: auto;
            display: block;
            border-radius: 16px;
            transition: transform 0.5s ease;
        }
        
        .feature-image:hover img {
            transform: scale(1.05);
        }
        
        /* Feature Grid */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
            margin-top: 60px;
        }
        
        .feature-card {
            background: white;
            border-radius: 24px;
            padding: 40px;
            box-shadow: var(--shadow-md);
            transition: var(--transition);
            border: 1px solid var(--border-color);
            position: relative;
            overflow: hidden;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background: linear-gradient(180deg, var(--primary-color), var(--primary-light));
            transform: scaleY(0);
            transition: transform 0.4s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-8px);
            box-shadow: var(--shadow-lg);
            border-color: var(--primary-color);
        }
        
        .feature-card:hover::before {
            transform: scaleY(1);
        }
        
        .feature-card-icon {
            width: 64px;
            height: 64px;
            background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 24px;
            font-size: 2rem;
        }
        
        .feature-card h3 {
            color: var(--primary-color);
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 12px;
        }
        
        .feature-card p {
            color: var(--text-gray);
            font-size: 1rem;
            line-height: 1.7;
            margin: 0;
        }
        
        .feature-card-image {
            margin-top: 24px;
            border-radius: 16px;
            overflow: hidden;
        }
        
        .feature-card-image img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.5s ease;
        }
        
        .feature-card:hover .feature-card-image img {
            transform: scale(1.1);
        }
        
        /* Stats Section */
        .stats-section {
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-light) 100%);
            padding: 80px 0;
            color: white;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 60px;
            text-align: center;
        }
        
        .stat-item {
            padding: 20px;
        }
        
        .stat-number {
            font-size: clamp(3rem, 6vw, 4.5rem);
            font-weight: 800;
            margin-bottom: 12px;
            display: block;
            color: white;
        }
        
        .stat-label {
            font-size: 1.25rem;
            font-weight: 500;
            opacity: 0.95;
        }
        
        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, var(--bg-light) 0%, white 100%);
            padding: 100px 0;
            text-align: center;
        }
        
        .cta-content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .cta-content h2 {
            color: var(--primary-color);
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 700;
            margin-bottom: 24px;
        }
        
        .cta-content p {
            color: var(--text-gray);
            font-size: 1.25rem;
            line-height: 1.8;
            margin-bottom: 40px;
        }
        
        .cta-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .cta-button {
            display: inline-block;
            padding: 18px 40px;
            background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-weight: 600;
            font-size: 1.125rem;
            transition: var(--transition);
            box-shadow: var(--shadow-md);
        }
        
        .cta-button:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }
        
        .cta-button img {
            height: 50px;
            width: auto;
            display: block;
        }
        
        /* Responsive */
        @media (max-width: 1024px) {
            .feature-showcase {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            
            .feature-showcase.reverse .feature-content,
            .feature-showcase.reverse .feature-image {
                order: initial;
            }
        }
        
        @media (max-width: 768px) {
            .features-hero {
                padding: 120px 20px 80px;
            }
            
            .features-section {
                padding: 60px 0;
            }
            
            .feature-grid {
                grid-template-columns: 1fr;
                gap: 32px;
            }
            
            .feature-card {
                padding: 32px 24px;
            }
            
            .cta-buttons {
                flex-direction: column;
                align-items: center;
            }
            
            .cta-button {
                width: 100%;
                max-width: 300px;
            }
        }
    </style>
"""

# Features Page Content
features_content = """
    <section class="features-hero">
        <div class="features-hero-content">
            <h1>Complete Islamic Companion</h1>
            <p>Discover all the powerful features that make Tijaniyah Muslim Pro your trusted digital companion for practicing your Deen.</p>
        </div>
    </section>

    <section class="features-section">
        <div class="container">
            <div class="feature-showcase">
                <div class="feature-content">
                    <h2>Prayer Times & Qibla</h2>
                    <p>Never miss a prayer with accurate, location-based prayer times. Our advanced algorithm calculates precise prayer times based on your location, with beautiful prayer cards and clear indicators for current and next prayers.</p>
                    <ul class="feature-list">
                        <li>Accurate location-based prayer times</li>
                        <li>Beautiful prayer cards with animations</li>
                        <li>Current and next prayer indicators</li>
                        <li>Adhan notifications</li>
                        <li>Qibla compass with real-time direction</li>
                        <li>Distance to Kaaba display</li>
                    </ul>
                </div>
                <div class="feature-image">
                    <img src="assets/home screen.PNG" alt="Prayer Times Screen" loading="lazy">
                </div>
            </div>

            <div class="feature-showcase reverse">
                <div class="feature-content">
                    <h2>Read the Holy Quran</h2>
                    <p>Access the complete Holy Quran with multiple translations, beautiful Arabic text, and powerful search capabilities. Bookmark your favorite verses and read with ease.</p>
                    <ul class="feature-list">
                        <li>Complete Quran with Arabic text</li>
                        <li>Multiple translations</li>
                        <li>Verse-by-verse reading</li>
                        <li>Bookmark favorite verses</li>
                        <li>Powerful search functionality</li>
                        <li>Audio recitation</li>
                    </ul>
                </div>
                <div class="feature-image">
                    <img src="assets/quran screen.jpg" alt="Quran Reader Screen" loading="lazy">
                </div>
            </div>

            <div class="feature-showcase">
                <div class="feature-content">
                    <h2>Duas & Supplications</h2>
                    <p>Comprehensive collection of Islamic prayers and supplications for every occasion. Access authentic duas with Arabic text, transliteration, and translations.</p>
                    <ul class="feature-list">
                        <li>Extensive collection of duas</li>
                        <li>Arabic text with transliteration</li>
                        <li>Multiple translations</li>
                        <li>Categorized by occasion</li>
                        <li>Search and favorites</li>
                        <li>Daily dhikr reminders</li>
                    </ul>
                </div>
                <div class="feature-image">
                    <img src="assets/duas screen.jpg" alt="Duas Screen" loading="lazy">
                </div>
            </div>

            <div class="feature-showcase reverse">
                <div class="feature-content">
                    <h2>AI Noor - Your AI-Powered Islamic Assistant</h2>
                    <p>Get instant answers to your Islamic questions with our AI-powered assistant. AI Noor provides authentic, scholar-verified responses to help you on your spiritual journey.</p>
                    <ul class="feature-list">
                        <li>AI-powered Islamic guidance</li>
                        <li>Instant answers to questions</li>
                        <li>Scholar-verified responses</li>
                        <li>Available 24/7</li>
                        <li>Multiple languages support</li>
                        <li>Contextual understanding</li>
                    </ul>
                </div>
                <div class="feature-image">
                    <img src="assets/ai noor screen.jpg" alt="AI Noor Screen" loading="lazy">
                </div>
            </div>
        </div>
    </section>

    <section class="features-section features-section-alt">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary-color); font-size: clamp(2rem, 4vw, 2.75rem); font-weight: 700; margin-bottom: 60px;">All Features</h2>
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-card-icon">🕌</div>
                    <h3>Prayer Times</h3>
                    <p>Accurate location-based prayer times with beautiful cards and current/next prayer indicators.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">🧭</div>
                    <h3>Qibla Compass</h3>
                    <p>Real-time compass with accurate Qibla direction calculation and distance to Kaaba display.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">📿</div>
                    <h3>Digital Tasbih</h3>
                    <p>Interactive counter with animations, multiple targets (33, 99, 100, 1000), and haptic feedback.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">📖</div>
                    <h3>Quran Reader</h3>
                    <p>Complete Quran with Arabic text, translations, bookmarks, and search capabilities.</p>
                    <div class="feature-card-image">
                        <img src="assets/quran screen2.PNG" alt="Quran Reader" loading="lazy">
                    </div>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">🤲</div>
                    <h3>Duas & Supplications</h3>
                    <p>Comprehensive collection with Arabic text, transliteration, translation, search, and favorites.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">📝</div>
                    <h3>Wazifa Tracker</h3>
                    <p>Track daily Islamic practices with progress tracking and filter options.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">📋</div>
                    <h3>Lazim Tracker</h3>
                    <p>Track your daily Islamic commitments and spiritual routines.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">🕌</div>
                    <h3>Zikr Jumma</h3>
                    <p>Special Friday prayers and dhikr for your spiritual practice.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">📔</div>
                    <h3>Islamic Journal</h3>
                    <p>Reflect on your spiritual journey and document your growth.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">👨‍🏫</div>
                    <h3>Scholars</h3>
                    <p>Learn from Islamic scholars and teachers.</p>
                    <div class="feature-card-image">
                        <img src="assets/scholars screen.PNG" alt="Scholars" loading="lazy">
                    </div>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">👥</div>
                    <h3>Community</h3>
                    <p>Connect with fellow Muslims worldwide.</p>
                    <div class="feature-card-image">
                        <img src="assets/community screen.jpg" alt="Community" loading="lazy">
                    </div>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">📍</div>
                    <h3>Mosque Locator</h3>
                    <p>Find nearby mosques and prayer facilities.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">🕋</div>
                    <h3>Makkah Live</h3>
                    <p>Watch live streams from the Holy Kaaba.</p>
                    <div class="feature-card-image">
                        <img src="assets/makkah live screen.PNG" alt="Makkah Live" loading="lazy">
                    </div>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">🤖</div>
                    <h3>AI Noor</h3>
                    <p>AI-powered Islamic assistant for your questions.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">💝</div>
                    <h3>Donate</h3>
                    <p>Support Islamic causes and charitable work.</p>
                    <div class="feature-card-image">
                        <img src="assets/zakat screen.jpg" alt="Donate" loading="lazy">
                    </div>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">🕐</div>
                    <h3>Hajj & Umrah</h3>
                    <p>Complete guide and tools for Hajj and Umrah pilgrimage.</p>
                    <div class="feature-card-image">
                        <img src="assets/hajj screen.jpg" alt="Hajj" loading="lazy">
                    </div>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">📚</div>
                    <h3>Islamic Lessons</h3>
                    <p>Learn from comprehensive Islamic courses and lessons.</p>
                    <div class="feature-card-image">
                        <img src="assets/lessons screen.jpg" alt="Lessons" loading="lazy">
                    </div>
                </div>
                
                <div class="feature-card">
                    <div class="feature-card-icon">⭐</div>
                    <h3>More Features</h3>
                    <p>Discover additional powerful features to enhance your Islamic practice.</p>
                    <div class="feature-card-image">
                        <img src="assets/more features screen.PNG" alt="More Features" loading="lazy">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="stats-section">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number">160+ million</span>
                    <p class="stat-label">Downloads worldwide</p>
                </div>
                <div class="stat-item">
                    <span class="stat-number">9.7M</span>
                    <p class="stat-label">Active users</p>
                </div>
                <div class="stat-item">
                    <span class="stat-number">4.7</span>
                    <p class="stat-label">App Store rating</p>
                </div>
                <div class="stat-item">
                    <span class="stat-number">50+</span>
                    <p class="stat-label">Languages supported</p>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <div class="cta-content">
                <h2>Start Your Spiritual Journey Today</h2>
                <p>Download Tijaniyah Muslim Pro and experience the complete Islamic companion designed to strengthen your connection with Allah.</p>
                <div class="cta-buttons">
                    <a href="https://apps.apple.com/app/muslim-pro-azan-quran-qibla/id388389451" class="cta-button" target="_blank" rel="noopener">
                        <img src="assets/wp-content/uploads/2024/09/appstore-200-69.png" alt="Download on App Store">
                    </a>
                    <a href="https://play.google.com/store/apps/details?id=com.bitsmedia.android.tijaniyahmuslimpro" class="cta-button" target="_blank" rel="noopener">
                        <img src="assets/wp-content/uploads/2024/09/play_store-200.png" alt="Get it on Google Play">
                    </a>
                </div>
            </div>
        </div>
    </section>
"""

# Create features directory if it doesn't exist
import os
os.makedirs('features', exist_ok=True)

# Generate header and footer
header, footer = generate_header_footer(is_subdir=True)

# Build the page
head_section = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Features | Tijaniyah Muslim Pro</title>
    <meta name="description" content="Discover all the powerful features of Tijaniyah Muslim Pro - your complete Islamic companion with prayer times, Quran, duas, AI assistant, and more.">
    <meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large"/>
    <link rel="canonical" href="../features/index.html" />
    <link rel="icon" href="../assets/App logo.png" sizes="32x32" />
    <link rel="icon" href="../assets/App logo.png" sizes="192x192" />
    <link rel="apple-touch-icon" href="../assets/App logo.png" />
    <link rel="stylesheet" href="../styles.css" />
</head>
"""

html = f"""<!DOCTYPE html>
<html lang="en-US">
{head_section}
    {modern_css}
    {features_css}
</head>
<body class="page-template-default page">
    {header}
    {features_content}
    {footer}
</body>
</html>
"""

with open('features/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Created features/index.html")

