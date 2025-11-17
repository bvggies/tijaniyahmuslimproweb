#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read header and footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header
header_start = index_content.find('<header class="bde-header-builder-25-100')
header_end = index_content.find('</header>', header_start) + len('</header>')
header_content = index_content[header_start:header_end]

# Extract footer
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
    
    # Adjust page links
    html_content = html_content.replace('href="index.html"', 'href="../index.html"')
    html_content = html_content.replace('href="about-us/index.html"', 'href="../about-us/index.html"')
    html_content = html_content.replace('href="contact-us/index.html"', 'href="../contact-us/index.html"')
    html_content = html_content.replace('href="privacy-policy/index.html"', 'href="../privacy-policy/index.html"')
    html_content = html_content.replace('href="terms/index.html"', 'href="../terms/index.html"')
    html_content = html_content.replace('href="features/index.html"', 'href="../features/index.html"')
    html_content = html_content.replace('href="winter-aid/index.html"', 'href="../winter-aid/index.html"')
    
    return html_content

# Modern CSS styles
modern_css = """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        .hero-section {
            background: linear-gradient(135deg, #1a472a 0%, #2d5a3d 50%, #3d6b4d 100%);
            padding: 8rem 2rem 6rem;
            text-align: center;
            color: white;
            position: relative;
            overflow: hidden;
        }
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="100" height="100" patternUnits="userSpaceOnUse"><path d="M 100 0 L 0 0 0 100" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/></pattern></defs><rect width="100%" height="100%" fill="url(%23grid)"/></svg>');
            opacity: 0.3;
        }
        .hero-section h1 {
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 700;
            margin-bottom: 1.5rem;
            position: relative;
            z-index: 1;
        }
        .hero-section p {
            font-size: clamp(1.1rem, 2vw, 1.3rem);
            max-width: 700px;
            margin: 0 auto;
            opacity: 0.95;
            position: relative;
            z-index: 1;
        }
        .content-section {
            padding: 5rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        .card {
            background: white;
            border-radius: 16px;
            padding: 2.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            margin-bottom: 2rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        }
        .card h2 {
            color: #1a472a;
            font-size: 2rem;
            margin-bottom: 1rem;
            font-weight: 600;
        }
        .card h3 {
            color: #1a472a;
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-weight: 600;
        }
        .card p {
            color: #555;
            font-size: 1.05rem;
            line-height: 1.8;
            margin-bottom: 1.5rem;
        }
        .card ul {
            margin-bottom: 1.5rem;
            padding-left: 2rem;
        }
        .card li {
            color: #555;
            margin-bottom: 0.75rem;
            line-height: 1.8;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }
        .feature-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border-radius: 12px;
            padding: 2rem;
            border: 1px solid #e9ecef;
            transition: all 0.3s ease;
        }
        .feature-card:hover {
            border-color: #1a472a;
            box-shadow: 0 4px 15px rgba(26, 71, 42, 0.1);
        }
        .feature-card h3 {
            color: #1a472a;
            font-size: 1.3rem;
            margin-bottom: 0.75rem;
        }
        .feature-card p {
            color: #666;
            font-size: 0.95rem;
            margin: 0;
        }
        .stats-section {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 5rem 2rem;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 3rem;
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }
        .stat-item h3 {
            font-size: 3rem;
            color: #1a472a;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }
        .stat-item p {
            color: #666;
            font-size: 1.1rem;
        }
        .contact-form {
            max-width: 700px;
            margin: 0 auto;
            background: white;
            padding: 3rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #333;
            font-size: 0.95rem;
        }
        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 0.875rem;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1rem;
            font-family: inherit;
            transition: border-color 0.3s ease;
        }
        .form-group input:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            outline: none;
            border-color: #1a472a;
        }
        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }
        .btn-submit {
            background: linear-gradient(135deg, #1a472a 0%, #2d5a3d 100%);
            color: white;
            padding: 1rem 2.5rem;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .btn-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(26, 71, 42, 0.3);
        }
        .contact-info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }
        .contact-card {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border-radius: 12px;
            border: 1px solid #e9ecef;
        }
        .contact-card h3 {
            color: #1a472a;
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }
        .contact-card p {
            color: #666;
            margin: 0;
        }
        .last-updated {
            font-style: italic;
            color: #888;
            margin-bottom: 2rem;
            font-size: 0.95rem;
        }
        @media (max-width: 768px) {
            .hero-section {
                padding: 5rem 1.5rem 4rem;
            }
            .content-section {
                padding: 3rem 1.5rem;
            }
            .card {
                padding: 1.5rem;
            }
            .contact-form {
                padding: 2rem 1.5rem;
            }
        }
    </style>
"""

# About Us Page Content
about_us_content = """
    <!-- Hero Section -->
    <section class="hero-section">
        <h1>About Tijaniyah Muslim Pro</h1>
        <p>Your trusted Islamic companion, empowering Muslims worldwide with accurate prayer times, comprehensive Quran resources, and meaningful Islamic content.</p>
    </section>

    <!-- Main Content -->
    <section class="content-section">
        <div class="card">
            <h2>Our Mission</h2>
            <p>Tijaniyah Muslim Pro is dedicated to being your digital companion in practicing your Deen. We strive to provide accurate prayer times, comprehensive Quran resources, and meaningful Islamic content that helps Muslims worldwide stay connected to their faith.</p>
            <p>From accurate prayer times and Qibla compass to Quran reading, digital tasbih, duas, Wazifa tracking, Islamic journal, AI-powered guidance, and community features - Tijaniyah Muslim Pro is your complete digital companion for practicing your Deen.</p>
        </div>

        <div class="card">
            <h2>Our Vision</h2>
            <p>We envision a world where every Muslim has easy access to authentic Islamic resources and tools that strengthen their connection with Allah and their community.</p>
            <p>Through technology and innovation, we aim to make Islamic knowledge and practices accessible to Muslims everywhere, anytime, anywhere.</p>
        </div>

        <div class="card">
            <h2>Our Core Values</h2>
            <div class="grid">
                <div class="feature-card">
                    <h3>Authenticity</h3>
                    <p>We ensure all our content and resources are based on authentic Islamic sources and verified by Islamic scholars.</p>
                </div>
                <div class="feature-card">
                    <h3>Accessibility</h3>
                    <p>We believe Islamic knowledge should be accessible to everyone, regardless of location or background.</p>
                </div>
                <div class="feature-card">
                    <h3>Community</h3>
                    <p>We foster a sense of unity and belonging among Muslims worldwide through our platform.</p>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>Our Features</h2>
            <div class="grid">
                <div class="feature-card">
                    <h3>Prayer Times</h3>
                    <p>Accurate location-based prayer times with beautiful cards and current/next prayer indicators.</p>
                </div>
                <div class="feature-card">
                    <h3>Qibla Compass</h3>
                    <p>Real-time compass with accurate Qibla direction calculation and distance to Kaaba display.</p>
                </div>
                <div class="feature-card">
                    <h3>Duas & Supplications</h3>
                    <p>Comprehensive collection with Arabic text, transliteration, translation, search, and favorites.</p>
                </div>
                <div class="feature-card">
                    <h3>Quran Reader</h3>
                    <p>Complete Quran with Arabic text, translations, bookmarks, and search capabilities.</p>
                </div>
                <div class="feature-card">
                    <h3>Digital Tasbih</h3>
                    <p>Interactive counter with animations, multiple targets (33, 99, 100, 1000), and haptic feedback.</p>
                </div>
                <div class="feature-card">
                    <h3>Wazifa Tracker</h3>
                    <p>Track daily Islamic practices with progress tracking and filter options.</p>
                </div>
                <div class="feature-card">
                    <h3>Lazim Tracker</h3>
                    <p>Track your daily Islamic commitments and spiritual routines.</p>
                </div>
                <div class="feature-card">
                    <h3>Zikr Jumma</h3>
                    <p>Special Friday prayers and dhikr for your spiritual practice.</p>
                </div>
                <div class="feature-card">
                    <h3>Islamic Journal</h3>
                    <p>Reflect on your spiritual journey and document your growth.</p>
                </div>
                <div class="feature-card">
                    <h3>Scholars</h3>
                    <p>Learn from Islamic scholars and teachers.</p>
                </div>
                <div class="feature-card">
                    <h3>Community</h3>
                    <p>Connect with fellow Muslims worldwide.</p>
                </div>
                <div class="feature-card">
                    <h3>Mosque Locator</h3>
                    <p>Find nearby mosques and prayer facilities.</p>
                </div>
                <div class="feature-card">
                    <h3>Makkah Live</h3>
                    <p>Watch live streams from the Holy Kaaba.</p>
                </div>
                <div class="feature-card">
                    <h3>AI Noor</h3>
                    <p>AI-powered Islamic assistant for your questions.</p>
                </div>
                <div class="feature-card">
                    <h3>Donate</h3>
                    <p>Support Islamic causes and charitable work.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
        <div class="stats-grid">
            <div class="stat-item">
                <h3>160+ million</h3>
                <p>Downloads worldwide</p>
            </div>
            <div class="stat-item">
                <h3>9.7M</h3>
                <p>Active users</p>
            </div>
            <div class="stat-item">
                <h3>4.7</h3>
                <p>App Store rating</p>
            </div>
        </div>
    </section>
"""

# Contact Us Page Content
contact_us_content = """
    <!-- Hero Section -->
    <section class="hero-section">
        <h1>Contact Us</h1>
        <p>We'd love to hear from you. Send us a message and we'll respond as soon as possible.</p>
    </section>

    <!-- Main Content -->
    <section class="content-section">
        <div class="contact-form">
            <form id="contactForm" onsubmit="handleSubmit(event)">
                <div class="form-group">
                    <label for="name">Full Name *</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email Address *</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="subject">Subject *</label>
                    <select id="subject" name="subject" required>
                        <option value="">Select a subject</option>
                        <option value="general">General Inquiry</option>
                        <option value="support">Technical Support</option>
                        <option value="premium">Premium Subscription</option>
                        <option value="partnership">Partnership Opportunities</option>
                        <option value="feedback">Feedback</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="message">Message *</label>
                    <textarea id="message" name="message" required></textarea>
                </div>
                <button type="submit" class="btn-submit">Send Message</button>
            </form>
        </div>

        <div class="contact-info">
            <div class="contact-card">
                <h3>Email</h3>
                <p>support@tijaniyahmuslimpro.com</p>
            </div>
            <div class="contact-card">
                <h3>Response Time</h3>
                <p>We typically respond within 24-48 hours</p>
            </div>
            <div class="contact-card">
                <h3>Office Hours</h3>
                <p>Monday - Friday<br>9:00 AM - 6:00 PM GMT</p>
            </div>
        </div>
    </section>

    <script>
        function handleSubmit(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData);
            console.log('Contact form submission:', data);
            alert('Thank you for contacting us! We will get back to you soon.');
            event.target.reset();
        }
    </script>
"""

# Privacy Policy Page Content
privacy_policy_content = """
    <!-- Hero Section -->
    <section class="hero-section">
        <h1>Privacy Policy</h1>
        <p>Your privacy is important to us. Learn how we collect, use, and protect your personal information.</p>
    </section>

    <!-- Main Content -->
    <section class="content-section">
        <div class="card">
            <p class="last-updated">Last Updated: November 2025</p>

            <h2>Introduction</h2>
            <p>At Tijaniyah Muslim Pro, we are committed to protecting your privacy and ensuring the security of your personal information. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our mobile application and website.</p>

            <h2>Information We Collect</h2>
            <h3>Personal Information</h3>
            <p>We may collect personal information that you voluntarily provide to us, including:</p>
            <ul>
                <li>Name and contact information (email address, phone number)</li>
                <li>Location data for prayer times and Qibla direction</li>
                <li>Account credentials if you create an account</li>
                <li>Payment information for premium subscriptions</li>
            </ul>

            <h3>Automatically Collected Information</h3>
            <p>When you use our services, we may automatically collect:</p>
            <ul>
                <li>Device information (device type, operating system, unique device identifiers)</li>
                <li>Usage data (features used, time spent, interactions)</li>
                <li>Location data (with your permission) for accurate prayer times</li>
                <li>Log data (IP address, access times, pages viewed)</li>
            </ul>

            <h2>How We Use Your Information</h2>
            <p>We use the information we collect to:</p>
            <ul>
                <li>Provide and maintain our services</li>
                <li>Calculate accurate prayer times based on your location</li>
                <li>Process transactions and manage premium subscriptions</li>
                <li>Send you important updates and notifications</li>
                <li>Improve our services and develop new features</li>
                <li>Respond to your inquiries and provide customer support</li>
                <li>Comply with legal obligations</li>
            </ul>

            <h2>Data Sharing and Disclosure</h2>
            <p>We do not sell your personal information. We may share your information only in the following circumstances:</p>
            <ul>
                <li>With your explicit consent</li>
                <li>To comply with legal obligations or court orders</li>
                <li>To protect our rights, privacy, safety, or property</li>
                <li>With service providers who assist in operating our services (under strict confidentiality agreements)</li>
                <li>In connection with a business transfer or merger</li>
            </ul>

            <h2>Data Security</h2>
            <p>We implement appropriate technical and organizational security measures to protect your personal information against unauthorized access, alteration, disclosure, or destruction. However, no method of transmission over the internet is 100% secure.</p>

            <h2>Your Rights</h2>
            <p>Depending on your location, you may have the following rights:</p>
            <ul>
                <li>Access your personal information</li>
                <li>Correct inaccurate data</li>
                <li>Request deletion of your data</li>
                <li>Object to processing of your data</li>
                <li>Data portability</li>
                <li>Withdraw consent where processing is based on consent</li>
            </ul>

            <h2>Children's Privacy</h2>
            <p>Our services are not intended for children under 13 years of age. We do not knowingly collect personal information from children. If you believe we have collected information from a child, please contact us immediately.</p>

            <h2>International Data Transfers</h2>
            <p>Your information may be transferred to and processed in countries other than your country of residence. We ensure appropriate safeguards are in place to protect your data in accordance with this Privacy Policy.</p>

            <h2>Changes to This Privacy Policy</h2>
            <p>We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Last Updated" date.</p>

            <h2>Contact Us</h2>
            <p>If you have any questions about this Privacy Policy or our data practices, please contact us at:</p>
            <p><strong>Email:</strong> privacy@tijaniyahmuslimpro.com<br>
            <strong>Address:</strong> Tijaniyah Muslim Pro Privacy Team</p>
        </div>
    </section>
"""

# Terms Page Content
terms_content = """
    <!-- Hero Section -->
    <section class="hero-section">
        <h1>Terms of Use</h1>
        <p>Please read these terms carefully before using our services.</p>
    </section>

    <!-- Main Content -->
    <section class="content-section">
        <div class="card">
            <p class="last-updated">Last Updated: November 2025</p>

            <h2>Agreement to Terms</h2>
            <p>By accessing or using Tijaniyah Muslim Pro ("we," "us," or "our"), you agree to be bound by these Terms of Use ("Terms"). If you do not agree to these Terms, please do not use our services.</p>

            <h2>Description of Service</h2>
            <p>Tijaniyah Muslim Pro provides Islamic tools and resources including prayer times, Qibla direction, Quran reading, Islamic content, and related services through our mobile application and website.</p>

            <h2>User Accounts</h2>
            <h3>Account Creation</h3>
            <p>To access certain features, you may need to create an account. You agree to:</p>
            <ul>
                <li>Provide accurate, current, and complete information</li>
                <li>Maintain and update your account information</li>
                <li>Maintain the security of your account credentials</li>
                <li>Accept responsibility for all activities under your account</li>
            </ul>

            <h2>Acceptable Use</h2>
            <p>You agree not to:</p>
            <ul>
                <li>Use the service for any illegal or unauthorized purpose</li>
                <li>Violate any laws in your jurisdiction</li>
                <li>Infringe upon intellectual property rights</li>
                <li>Transmit any harmful code, viruses, or malware</li>
                <li>Interfere with or disrupt the service</li>
                <li>Attempt to gain unauthorized access to our systems</li>
                <li>Use the service to harass, abuse, or harm others</li>
                <li>Misrepresent your identity or affiliation</li>
            </ul>

            <h2>Premium Subscriptions</h2>
            <h3>Subscription Terms</h3>
            <p>Premium subscriptions are available for purchase. By subscribing, you agree to:</p>
            <ul>
                <li>Pay all fees associated with your subscription</li>
                <li>Automatic renewal unless cancelled</li>
                <li>Price changes with advance notice</li>
                <li>No refunds except as required by law</li>
            </ul>

            <h3>Cancellation</h3>
            <p>You may cancel your subscription at any time through your account settings. Cancellation takes effect at the end of your current billing period.</p>

            <h2>Intellectual Property</h2>
            <p>All content, features, and functionality of Tijaniyah Muslim Pro, including but not limited to text, graphics, logos, images, and software, are owned by us or our licensors and are protected by copyright, trademark, and other intellectual property laws.</p>
            <p>You may not reproduce, distribute, modify, create derivative works, publicly display, or otherwise use our content without our express written permission.</p>

            <h2>Third-Party Services</h2>
            <p>Our service may contain links to third-party websites or services. We are not responsible for the content, privacy policies, or practices of third-party services. Your use of third-party services is at your own risk.</p>

            <h2>Disclaimer of Warranties</h2>
            <p>Tijaniyah Muslim Pro is provided "as is" and "as available" without warranties of any kind, either express or implied. We do not guarantee that:</p>
            <ul>
                <li>The service will be uninterrupted or error-free</li>
                <li>Defects will be corrected</li>
                <li>The service is free of viruses or harmful components</li>
                <li>Prayer times or other information are 100% accurate</li>
            </ul>

            <h2>Limitation of Liability</h2>
            <p>To the maximum extent permitted by law, Tijaniyah Muslim Pro shall not be liable for any indirect, incidental, special, consequential, or punitive damages, or any loss of profits or revenues, whether incurred directly or indirectly, or any loss of data, use, goodwill, or other intangible losses resulting from your use of the service.</p>

            <h2>Indemnification</h2>
            <p>You agree to indemnify and hold harmless Tijaniyah Muslim Pro, its officers, directors, employees, and agents from any claims, damages, losses, liabilities, and expenses arising out of your use of the service or violation of these Terms.</p>

            <h2>Termination</h2>
            <p>We may terminate or suspend your account and access to the service immediately, without prior notice, for any reason, including if you breach these Terms. Upon termination, your right to use the service will cease immediately.</p>

            <h2>Governing Law</h2>
            <p>These Terms shall be governed by and construed in accordance with applicable laws, without regard to conflict of law principles.</p>

            <h2>Changes to Terms</h2>
            <p>We reserve the right to modify these Terms at any time. We will notify users of material changes by posting the updated Terms on this page and updating the "Last Updated" date. Your continued use of the service after changes constitutes acceptance of the new Terms.</p>

            <h2>Contact Information</h2>
            <p>If you have any questions about these Terms, please contact us at:</p>
            <p><strong>Email:</strong> legal@tijaniyahmuslimpro.com<br>
            <strong>Address:</strong> Tijaniyah Muslim Pro Legal Team</p>
        </div>
    </section>
"""

# Page templates
pages = [
    {
        'path': 'about-us/index.html',
        'title': 'About Us | Tijaniyah Muslim Pro',
        'description': 'Learn about Tijaniyah Muslim Pro - your trusted Islamic app companion providing prayer times, Quran, and Islamic resources to Muslims worldwide.',
        'content': about_us_content,
        'is_subdir': True
    },
    {
        'path': 'contact-us/index.html',
        'title': 'Contact Us | Tijaniyah Muslim Pro',
        'description': 'Get in touch with Tijaniyah Muslim Pro. We\'re here to help with any questions or support you need.',
        'content': contact_us_content,
        'is_subdir': True
    },
    {
        'path': 'privacy-policy/index.html',
        'title': 'Privacy Policy | Tijaniyah Muslim Pro',
        'description': 'Read Tijaniyah Muslim Pro\'s Privacy Policy to understand how we collect, use, and protect your personal information.',
        'content': privacy_policy_content,
        'is_subdir': True
    },
    {
        'path': 'terms/index.html',
        'title': 'Terms of Use | Tijaniyah Muslim Pro',
        'description': 'Read Tijaniyah Muslim Pro\'s Terms of Use to understand the terms and conditions for using our services.',
        'content': terms_content,
        'is_subdir': True
    }
]

# Generate pages
for page in pages:
    header = adjust_paths(header_content, page['is_subdir'])
    footer = adjust_paths(footer_content, page['is_subdir'])
    
    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page['title']}</title>
    <meta name="description" content="{page['description']}">
    <link type="text/css" media="all" href="{'../' if page['is_subdir'] else ''}styles-muslimpro.css" rel="stylesheet" />
    <link rel="stylesheet" href="{'../' if page['is_subdir'] else ''}styles.css" />
    {modern_css}
</head>
<body class="page-template-default page">
    {header}
    {page['content']}
    {footer}
</body>
</html>
"""
    
    with open(page['path'], 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Created {page['path']}")

print("All pages redesigned successfully!")

