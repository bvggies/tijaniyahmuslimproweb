#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modern Header HTML
modern_header = """<header class="modern-header">
    <div class="header-top-bar">
        <div class="container">
            <a href="{home_link}" class="top-banner-link">❄️ Send essential comfort today to transform a winter of desperation into one of hope ❄️</a>
        </div>
    </div>
    <div class="header-main">
        <div class="container">
            <div class="header-content">
                <div class="header-logo">
                    <a href="{home_link}" class="logo-link">
                        <img src="{logo_path}" alt="Tijaniyah Muslim Pro Logo" width="150" height="150">
                    </a>
                </div>
                <nav class="main-nav">
                    <button class="mobile-menu-btn" aria-label="Toggle menu" aria-expanded="false">
                        <span class="hamburger-line"></span>
                        <span class="hamburger-line"></span>
                        <span class="hamburger-line"></span>
                    </button>
                    <ul class="nav-list">
                        <li class="nav-item">
                            <a href="{about_link}" class="nav-link">About Us</a>
                        </li>
                        <li class="nav-item has-submenu">
                            <a href="{features_link}" class="nav-link">
                                Features
                                <svg class="dropdown-icon" width="12" height="12" viewBox="0 0 12 12" fill="none">
                                    <path d="M2 4L6 8L10 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </a>
                            <ul class="submenu">
                                <li><a href="{features_link}">Core Features</a></li>
                                <li><a href="{ummah_link}">Ummah Pro</a></li>
                                <li><a href="{academy_link}">Academy</a></li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <a href="{contact_link}" class="nav-link">Contact Us</a>
                        </li>
                        <li class="nav-item">
                            <a href="{privacy_link}" class="nav-link">Privacy Policy</a>
                        </li>
                        <li class="nav-item">
                            <a href="{terms_link}" class="nav-link">Terms</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
</header>"""

# Modern Footer HTML
modern_footer = """<footer class="modern-footer">
    <div class="footer-main">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-column">
                    <h3 class="footer-title">Who We Are</h3>
                    <ul class="footer-links">
                        <li><a href="{about_link}">About Us</a></li>
                        <li><a href="{jobs_link}">Job Openings</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3 class="footer-title">What We Do</h3>
                    <ul class="footer-links">
                        <li><a href="{features_link}">Our Features</a></li>
                        <li><a href="{press_link}">Press Releases</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3 class="footer-title">For Users</h3>
                    <ul class="footer-links">
                        <li><a href="{gift_link}">Gift Premium</a></li>
                        <li><a href="{redeem_link}">Redeem Premium</a></li>
                        <li><a href="{contact_link}">Contact Us</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3 class="footer-title">For Business</h3>
                    <ul class="footer-links">
                        <li><a href="{corporate_link}">Corporate Gifting</a></li>
                        <li><a href="{advertise_link}">Advertise With Us</a></li>
                    </ul>
                </div>
                <div class="footer-column footer-brand-column">
                    <div class="footer-brand">
                        <img src="{footer_logo_path}" alt="Tijaniyah Muslim Pro" class="footer-brand-img">
                        <p class="footer-brand-text">Tijaniyah Muslim Pro is the essential Islamic app companion for Muslims. Now with Qalbox, we are the digital home for all things Muslim.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="footer-social-section">
        <div class="container">
            <div class="social-icons">
                <a href="{facebook_link}" class="social-icon" aria-label="Facebook" target="_blank" rel="noopener">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/>
                    </svg>
                </a>
                <a href="{twitter_link}" class="social-icon" aria-label="Twitter" target="_blank" rel="noopener">
                    <svg width="24" height="24" viewBox="0 0 512 512" fill="currentColor">
                        <path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"/>
                    </svg>
                </a>
                <a href="{instagram_link}" class="social-icon" aria-label="Instagram" target="_blank" rel="noopener">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                    </svg>
                </a>
                <a href="{youtube_link}" class="social-icon" aria-label="YouTube" target="_blank" rel="noopener">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/>
                    </svg>
                </a>
                <a href="{linkedin_link}" class="social-icon" aria-label="LinkedIn" target="_blank" rel="noopener">
                    <svg width="24" height="24" viewBox="-4 -2 32 32" fill="currentColor">
                        <path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/>
                    </svg>
                </a>
            </div>
        </div>
    </div>
    <div class="footer-divider"></div>
    <div class="footer-bottom">
        <div class="container">
            <div class="footer-bottom-content">
                <div class="footer-legal-links">
                    <a href="{help_link}">Help Center</a>
                    <a href="{press_contact_link}">Contact Press</a>
                    <a href="{cookies_link}">Cookies Policy</a>
                    <a href="{privacy_link}">Privacy Policy</a>
                    <a href="{terms_link}">Terms of Use</a>
                    <a href="{disclaimer_link}">Disclaimer</a>
                </div>
                <div class="footer-copyright">
                    <p>Copyright © 2025 Tijaniyah Muslim Pro. All rights reserved.</p>
                </div>
            </div>
        </div>
    </div>
</footer>"""

# Modern Header and Footer CSS
modern_css = """
    <style>
        /* Header Styles */
        .modern-header {
            background: #ffffff;
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
            position: sticky;
            top: 0;
            z-index: 1000;
            transition: all 0.3s ease;
        }
        
        .header-top-bar {
            background: linear-gradient(135deg, #1a472a 0%, #2d5a3d 100%);
            padding: 12px 0;
            text-align: center;
        }
        
        .header-top-bar .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .top-banner-link {
            color: #ffffff;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            display: inline-block;
            transition: opacity 0.3s ease;
        }
        
        .top-banner-link:hover {
            opacity: 0.9;
        }
        
        .header-main {
            padding: 20px 0;
        }
        
        .header-main .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .header-logo img {
            display: block;
            height: auto;
            transition: transform 0.3s ease;
        }
        
        .logo-link:hover img {
            transform: scale(1.05);
        }
        
        .main-nav {
            flex: 1;
            display: flex;
            justify-content: flex-end;
        }
        
        .mobile-menu-btn {
            display: none;
            flex-direction: column;
            background: none;
            border: none;
            cursor: pointer;
            padding: 8px;
            gap: 5px;
            z-index: 1001;
        }
        
        .hamburger-line {
            width: 28px;
            height: 3px;
            background: #1a472a;
            border-radius: 2px;
            transition: all 0.3s ease;
        }
        
        .mobile-menu-btn[aria-expanded="true"] .hamburger-line:nth-child(1) {
            transform: rotate(45deg) translate(8px, 8px);
        }
        
        .mobile-menu-btn[aria-expanded="true"] .hamburger-line:nth-child(2) {
            opacity: 0;
        }
        
        .mobile-menu-btn[aria-expanded="true"] .hamburger-line:nth-child(3) {
            transform: rotate(-45deg) translate(7px, -7px);
        }
        
        .nav-list {
            display: flex;
            list-style: none;
            margin: 0;
            padding: 0;
            gap: 40px;
            align-items: center;
        }
        
        .nav-item {
            position: relative;
        }
        
        .nav-link {
            color: #1a1a1a;
            text-decoration: none;
            font-weight: 500;
            font-size: 1rem;
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 0;
            transition: color 0.3s ease;
            position: relative;
        }
        
        .nav-link::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background: #1a472a;
            transition: width 0.3s ease;
        }
        
        .nav-link:hover {
            color: #1a472a;
        }
        
        .nav-link:hover::after {
            width: 100%;
        }
        
        .dropdown-icon {
            transition: transform 0.3s ease;
        }
        
        .has-submenu:hover .dropdown-icon {
            transform: rotate(180deg);
        }
        
        .submenu {
            position: absolute;
            top: 100%;
            left: 0;
            background: #ffffff;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
            border-radius: 12px;
            list-style: none;
            padding: 12px 0;
            margin: 12px 0 0 0;
            min-width: 200px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(-10px);
            transition: all 0.3s ease;
        }
        
        .has-submenu:hover .submenu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }
        
        .submenu li {
            padding: 0;
        }
        
        .submenu a {
            display: block;
            padding: 12px 24px;
            color: #1a1a1a;
            text-decoration: none;
            font-size: 0.95rem;
            transition: all 0.3s ease;
        }
        
        .submenu a:hover {
            background: #f8f9fa;
            color: #1a472a;
            padding-left: 28px;
        }
        
        /* Footer Styles */
        .modern-footer {
            background: #1a1a1a;
            color: #ffffff;
            margin-top: 100px;
        }
        
        .footer-main {
            padding: 80px 0 60px;
        }
        
        .footer-main .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 50px;
        }
        
        .footer-column {
            display: flex;
            flex-direction: column;
        }
        
        .footer-brand-column {
            grid-column: span 2;
        }
        
        .footer-title {
            font-size: 1.125rem;
            font-weight: 600;
            margin-bottom: 24px;
            color: #ffffff;
            position: relative;
            padding-bottom: 12px;
        }
        
        .footer-title::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 40px;
            height: 2px;
            background: linear-gradient(90deg, #1a472a, #2d5a3d);
        }
        
        .footer-links {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        
        .footer-links a {
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            font-size: 0.9375rem;
            transition: all 0.3s ease;
            display: inline-block;
        }
        
        .footer-links a:hover {
            color: #ffffff;
            transform: translateX(5px);
        }
        
        .footer-brand {
            max-width: 500px;
        }
        
        .footer-brand-img {
            max-width: 300px;
            height: auto;
            margin-bottom: 20px;
            opacity: 0.9;
            transition: opacity 0.3s ease;
        }
        
        .footer-brand-img:hover {
            opacity: 1;
        }
        
        .footer-brand-text {
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.9375rem;
            line-height: 1.7;
            margin: 0;
        }
        
        .footer-social-section {
            padding: 40px 0;
            background: rgba(255, 255, 255, 0.05);
        }
        
        .footer-social-section .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .social-icons {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }
        
        .social-icon {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            color: #ffffff;
            text-decoration: none;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .social-icon:hover {
            background: #1a472a;
            transform: translateY(-5px);
            border-color: #2d5a3d;
            box-shadow: 0 8px 20px rgba(26, 71, 42, 0.3);
        }
        
        .footer-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            margin: 0;
        }
        
        .footer-bottom {
            padding: 40px 0;
        }
        
        .footer-bottom .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .footer-bottom-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 24px;
        }
        
        .footer-legal-links {
            display: flex;
            flex-wrap: wrap;
            gap: 28px;
            justify-content: center;
        }
        
        .footer-legal-links a {
            color: rgba(255, 255, 255, 0.7);
            text-decoration: none;
            font-size: 0.875rem;
            transition: color 0.3s ease;
        }
        
        .footer-legal-links a:hover {
            color: #ffffff;
        }
        
        .footer-copyright {
            text-align: center;
        }
        
        .footer-copyright p {
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.875rem;
            margin: 0;
        }
        
        /* Responsive */
        @media (max-width: 1024px) {
            .footer-brand-column {
                grid-column: span 1;
            }
        }
        
        @media (max-width: 768px) {
            .mobile-menu-btn {
                display: flex;
            }
            
            .nav-list {
                position: fixed;
                top: 0;
                right: -100%;
                width: 300px;
                height: 100vh;
                background: #ffffff;
                flex-direction: column;
                align-items: flex-start;
                padding: 100px 30px 30px;
                box-shadow: -4px 0 20px rgba(0, 0, 0, 0.15);
                transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                gap: 0;
                overflow-y: auto;
            }
            
            .nav-list.active {
                right: 0;
            }
            
            .nav-item {
                width: 100%;
                border-bottom: 1px solid #f0f0f0;
            }
            
            .nav-link {
                padding: 18px 0;
                width: 100%;
            }
            
            .nav-link::after {
                display: none;
            }
            
            .submenu {
                position: static;
                opacity: 1;
                visibility: visible;
                transform: none;
                box-shadow: none;
                background: #f8f9fa;
                margin: 0;
                border-radius: 0;
                max-height: 0;
                overflow: hidden;
                transition: max-height 0.3s ease;
            }
            
            .has-submenu:hover .submenu,
            .has-submenu.active .submenu {
                max-height: 300px;
            }
            
            .footer-grid {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            
            .footer-brand-column {
                grid-column: span 1;
            }
            
            .footer-legal-links {
                flex-direction: column;
                gap: 16px;
                text-align: center;
            }
        }
    </style>
    
    <script>
        // Mobile menu functionality
        document.addEventListener('DOMContentLoaded', function() {
            const menuBtn = document.querySelector('.mobile-menu-btn');
            const navList = document.querySelector('.nav-list');
            const navItems = document.querySelectorAll('.has-submenu');
            
            if (menuBtn && navList) {
                menuBtn.addEventListener('click', function() {
                    const isExpanded = navList.classList.contains('active');
                    navList.classList.toggle('active');
                    menuBtn.setAttribute('aria-expanded', !isExpanded);
                });
                
                // Close menu when clicking outside
                document.addEventListener('click', function(e) {
                    if (!menuBtn.contains(e.target) && !navList.contains(e.target)) {
                        navList.classList.remove('active');
                        menuBtn.setAttribute('aria-expanded', 'false');
                    }
                });
                
                // Handle submenu toggle on mobile
                navItems.forEach(item => {
                    const link = item.querySelector('.nav-link');
                    link.addEventListener('click', function(e) {
                        if (window.innerWidth <= 768) {
                            e.preventDefault();
                            item.classList.toggle('active');
                        }
                    });
                });
            }
        });
    </script>
"""

# Function to generate header and footer with correct paths
def generate_header_footer(is_subdir=False):
    base = '../' if is_subdir else ''
    
    header = modern_header.format(
        home_link=f"{base}index.html",
        logo_path=f"{base}assets/App logo.png",
        about_link=f"{base}about-us/index.html",
        features_link=f"{base}features/index.html",
        ummah_link=f"{base}ummah-pro/index.html",
        academy_link=f"{base}academy-islamic-courses/index.html",
        contact_link=f"{base}contact-us/index.html",
        privacy_link=f"{base}privacy-policy/index.html",
        terms_link=f"{base}terms/index.html"
    )
    
    footer = modern_footer.format(
        about_link=f"{base}about-us/index.html",
        jobs_link="#",
        features_link=f"{base}features/index.html",
        press_link="#",
        gift_link="#",
        redeem_link="#",
        contact_link=f"{base}contact-us/index.html",
        corporate_link="#",
        advertise_link=f"{base}advertise/index.html",
        footer_logo_path=f"{base}assets/wp-content/uploads/2024/07/Untitled-design.png",
        facebook_link="https://www.facebook.com/tijaniyahmuslimpro",
        twitter_link="https://twitter.com/tijaniyahmuslimpro",
        instagram_link="https://www.instagram.com/tijaniyahmuslimproofficial/",
        youtube_link="https://www.youtube.com/channel/UCPTHHlJEmpnPlS0kW4eo4XQ",
        linkedin_link="#",
        help_link="#",
        press_contact_link="#",
        cookies_link=f"{base}cookies-policy/index.html",
        privacy_link=f"{base}privacy-policy/index.html",
        terms_link=f"{base}terms/index.html",
        disclaimer_link="#"
    )
    
    return header, footer

# Update all pages
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
    
    # Remove old header/footer CSS if exists
    css_start = content.find('/* Header Styles */')
    if css_start != -1:
        css_end = content.find('</script>', css_start) + len('</script>')
        if css_end > css_start:
            content = content[:css_start] + content[css_end:]
            print(f"  ✓ Removed old header/footer CSS")
    
    # Insert modern header after <body>
    body_start = content.find('<body')
    if body_start != -1:
        body_tag_end = content.find('>', body_start) + 1
        new_header, _ = generate_header_footer(is_subdir)
        content = content[:body_tag_end] + '\n    ' + new_header + '\n' + content[body_tag_end:]
        print(f"  ✓ Added modern header")
    
    # Insert modern footer before </body>
    body_end = content.rfind('</body>')
    if body_end != -1:
        _, new_footer = generate_header_footer(is_subdir)
        content = content[:body_end] + '\n    ' + new_footer + '\n' + content[body_end:]
        print(f"  ✓ Added modern footer")
    
    # Add modern CSS before </head>
    head_end = content.rfind('</head>')
    if head_end != -1:
        content = content[:head_end] + '\n    ' + modern_css + '\n' + content[head_end:]
        print(f"  ✓ Added modern CSS")
    
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Updated {page_path}\n")

print("All pages updated with modern header and footer!")

