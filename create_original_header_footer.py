#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Original Header HTML
original_header = """<header class="site-header">
    <div class="header-container">
        <div class="header-top">
            <a href="{home_link}" class="top-banner">❄️ Send essential comfort today to transform a winter of desperation into one of hope ❄️</a>
        </div>
        <div class="header-main">
            <div class="header-logo">
                <a href="{home_link}">
                    <img src="{logo_path}" alt="Tijaniyah Muslim Pro Logo" width="150" height="150">
                </a>
            </div>
            <nav class="header-nav">
                <button class="mobile-menu-toggle" aria-label="Toggle menu" aria-expanded="false">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <ul class="nav-menu">
                    <li><a href="{about_link}">About Us</a></li>
                    <li class="has-dropdown">
                        <a href="{features_link}">Features <span class="dropdown-arrow">▼</span></a>
                        <ul class="dropdown-menu">
                            <li><a href="{features_link}">Core Features</a></li>
                            <li><a href="{ummah_link}">Ummah Pro</a></li>
                            <li><a href="{academy_link}">Academy</a></li>
                        </ul>
                    </li>
                    <li><a href="{contact_link}">Contact Us</a></li>
                    <li><a href="{privacy_link}">Privacy Policy</a></li>
                    <li><a href="{terms_link}">Terms</a></li>
                </ul>
            </nav>
        </div>
    </div>
</header>"""

# Original Footer HTML
original_footer = """<footer class="site-footer">
    <div class="footer-container">
        <div class="footer-content">
            <div class="footer-column">
                <h3>Who We Are</h3>
                <ul>
                    <li><a href="{about_link}">About Us</a></li>
                    <li><a href="{jobs_link}">Job Openings</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>What We Do</h3>
                <ul>
                    <li><a href="{features_link}">Our Features</a></li>
                    <li><a href="{press_link}">Press Releases</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>For Users</h3>
                <ul>
                    <li><a href="{gift_link}">Gift Premium</a></li>
                    <li><a href="{redeem_link}">Redeem Premium</a></li>
                    <li><a href="{contact_link}">Contact Us</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>For Business</h3>
                <ul>
                    <li><a href="{corporate_link}">Corporate Gifting</a></li>
                    <li><a href="{advertise_link}">Advertise With Us</a></li>
                </ul>
            </div>
            <div class="footer-column footer-brand">
                <img src="{footer_logo_path}" alt="Tijaniyah Muslim Pro" width="837" height="442">
                <p>Tijaniyah Muslim Pro is the essential Islamic app companion for Muslims. Now with Qalbox, we are the digital home for all things Muslim.</p>
            </div>
        </div>
        <div class="footer-social">
            <a href="{facebook_link}" aria-label="Facebook" target="_blank" rel="noopener">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/>
                </svg>
            </a>
            <a href="{twitter_link}" aria-label="Twitter" target="_blank" rel="noopener">
                <svg width="24" height="24" viewBox="0 0 512 512" fill="currentColor">
                    <path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"/>
                </svg>
            </a>
            <a href="{instagram_link}" aria-label="Instagram" target="_blank" rel="noopener">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
            </a>
            <a href="{youtube_link}" aria-label="YouTube" target="_blank" rel="noopener">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/>
                </svg>
            </a>
            <a href="{linkedin_link}" aria-label="LinkedIn" target="_blank" rel="noopener">
                <svg width="24" height="24" viewBox="-4 -2 32 32" fill="currentColor">
                    <path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/>
                </svg>
            </a>
        </div>
        <div class="footer-divider"></div>
        <div class="footer-bottom">
            <div class="footer-links">
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
</footer>"""

# Header and Footer CSS
header_footer_css = """
    <style>
        /* Header Styles */
        .site-header {
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        .header-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .header-top {
            background: linear-gradient(135deg, #1a472a 0%, #2d5a3d 100%);
            padding: 12px 0;
            text-align: center;
        }
        
        .header-top .top-banner {
            color: white;
            text-decoration: none;
            font-size: 0.9rem;
            display: block;
        }
        
        .header-main {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px 0;
        }
        
        .header-logo img {
            display: block;
            height: auto;
        }
        
        .header-nav {
            flex: 1;
            display: flex;
            justify-content: flex-end;
        }
        
        .mobile-menu-toggle {
            display: none;
            flex-direction: column;
            background: none;
            border: none;
            cursor: pointer;
            padding: 8px;
            gap: 4px;
        }
        
        .mobile-menu-toggle span {
            width: 25px;
            height: 3px;
            background: var(--primary-color);
            transition: all 0.3s;
        }
        
        .nav-menu {
            display: flex;
            list-style: none;
            gap: 32px;
            align-items: center;
            margin: 0;
            padding: 0;
        }
        
        .nav-menu li {
            position: relative;
        }
        
        .nav-menu a {
            color: var(--text-dark);
            text-decoration: none;
            font-weight: 500;
            font-size: 1rem;
            transition: color 0.3s;
        }
        
        .nav-menu a:hover {
            color: var(--primary-color);
        }
        
        .has-dropdown .dropdown-arrow {
            font-size: 0.7rem;
            margin-left: 4px;
        }
        
        .dropdown-menu {
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            border-radius: 8px;
            list-style: none;
            padding: 8px 0;
            margin: 8px 0 0 0;
            min-width: 180px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(-10px);
            transition: all 0.3s;
        }
        
        .has-dropdown:hover .dropdown-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }
        
        .dropdown-menu li {
            padding: 0;
        }
        
        .dropdown-menu a {
            display: block;
            padding: 10px 20px;
            color: var(--text-dark);
        }
        
        .dropdown-menu a:hover {
            background: var(--bg-light);
            color: var(--primary-color);
        }
        
        /* Footer Styles */
        .site-footer {
            background: #1a1a1a;
            color: white;
            padding: 60px 0 30px;
            margin-top: 80px;
        }
        
        .footer-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            margin-bottom: 40px;
        }
        
        .footer-column h3 {
            font-size: 1.125rem;
            font-weight: 600;
            margin-bottom: 20px;
            color: white;
        }
        
        .footer-column ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .footer-column ul li {
            margin-bottom: 12px;
        }
        
        .footer-column a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            font-size: 0.9375rem;
            transition: color 0.3s;
        }
        
        .footer-column a:hover {
            color: white;
        }
        
        .footer-brand {
            grid-column: span 2;
        }
        
        .footer-brand img {
            max-width: 300px;
            height: auto;
            margin-bottom: 16px;
        }
        
        .footer-brand p {
            color: rgba(255,255,255,0.8);
            font-size: 0.9375rem;
            line-height: 1.6;
            margin: 0;
        }
        
        .footer-social {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-bottom: 30px;
        }
        
        .footer-social a {
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255,255,255,0.1);
            border-radius: 50%;
            color: white;
            transition: all 0.3s;
        }
        
        .footer-social a:hover {
            background: var(--primary-color);
            transform: translateY(-3px);
        }
        
        .footer-divider {
            height: 1px;
            background: rgba(255,255,255,0.1);
            margin: 30px 0;
        }
        
        .footer-bottom {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }
        
        .footer-links {
            display: flex;
            flex-wrap: wrap;
            gap: 24px;
            justify-content: center;
        }
        
        .footer-links a {
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            font-size: 0.875rem;
            transition: color 0.3s;
        }
        
        .footer-links a:hover {
            color: white;
        }
        
        .footer-copyright {
            text-align: center;
        }
        
        .footer-copyright p {
            color: rgba(255,255,255,0.6);
            font-size: 0.875rem;
            margin: 0;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .mobile-menu-toggle {
                display: flex;
            }
            
            .nav-menu {
                position: fixed;
                top: 0;
                right: -100%;
                width: 280px;
                height: 100vh;
                background: white;
                flex-direction: column;
                align-items: flex-start;
                padding: 80px 30px 30px;
                box-shadow: -2px 0 10px rgba(0,0,0,0.1);
                transition: right 0.3s;
                gap: 0;
            }
            
            .nav-menu.active {
                right: 0;
            }
            
            .nav-menu li {
                width: 100%;
                border-bottom: 1px solid var(--border-color);
            }
            
            .nav-menu a {
                display: block;
                padding: 15px 0;
            }
            
            .dropdown-menu {
                position: static;
                opacity: 1;
                visibility: visible;
                transform: none;
                box-shadow: none;
                background: var(--bg-light);
                margin: 0;
                border-radius: 0;
            }
            
            .footer-brand {
                grid-column: span 1;
            }
            
            .footer-content {
                grid-template-columns: 1fr;
            }
        }
    </style>
    
    <script>
        // Mobile menu toggle
        document.addEventListener('DOMContentLoaded', function() {
            const toggle = document.querySelector('.mobile-menu-toggle');
            const menu = document.querySelector('.nav-menu');
            
            if (toggle && menu) {
                toggle.addEventListener('click', function() {
                    menu.classList.toggle('active');
                    const isExpanded = menu.classList.contains('active');
                    toggle.setAttribute('aria-expanded', isExpanded);
                });
                
                // Close menu when clicking outside
                document.addEventListener('click', function(e) {
                    if (!toggle.contains(e.target) && !menu.contains(e.target)) {
                        menu.classList.remove('active');
                        toggle.setAttribute('aria-expanded', 'false');
                    }
                });
            }
        });
    </script>
"""

# Function to generate header and footer with correct paths
def generate_header_footer(is_subdir=False):
    base = '../' if is_subdir else ''
    
    header = original_header.format(
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
    
    footer = original_footer.format(
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
    
    # Remove old header (from <header to </header>)
    header_start = content.find('<header')
    if header_start != -1:
        header_end = content.find('</header>', header_start) + len('</header>')
        content = content[:header_start] + content[header_end:]
    
    # Remove old footer (from <footer to </footer>)
    footer_start = content.find('<footer')
    if footer_start != -1:
        footer_end = content.find('</footer>', footer_start) + len('</footer>')
        content = content[:footer_start] + content[footer_end:]
    
    # Generate new header and footer
    is_subdir = '/' in page_path
    new_header, new_footer = generate_header_footer(is_subdir)
    
    # Insert header after <body>
    body_start = content.find('<body')
    if body_start != -1:
        body_tag_end = content.find('>', body_start) + 1
        content = content[:body_tag_end] + '\n    ' + new_header + '\n' + content[body_tag_end:]
    
    # Insert footer before </body>
    body_end = content.rfind('</body>')
    if body_end != -1:
        content = content[:body_end] + '\n    ' + new_footer + '\n' + content[body_end:]
    
    # Add header/footer CSS before </head>
    head_end = content.rfind('</head>')
    if head_end != -1:
        content = content[:head_end] + '\n    ' + header_footer_css + '\n' + content[head_end:]
    
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {page_path}")

print("\nAll pages updated with original header and footer!")

