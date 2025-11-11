# Tijaniyah Muslim Pro - Landing Page

A beautiful, responsive landing page for Tijaniyah Muslim Pro, designed to match the layout and structure of the Muslim Pro website.

## Features

- **Responsive Design**: Fully responsive layout that works on all devices
- **Modern UI**: Clean and modern interface matching the Muslim Pro design
- **Interactive Elements**: Smooth scrolling, mobile menu, and animated sections
- **Complete Sections**: 
  - Header with navigation
  - Hero section with Arabic quote
  - Feature cards
  - Main features showcase
  - Statistics and testimonials
  - Islamic resources/blog section
  - Newsletter subscription
  - Footer with links

## File Structure

```
tijaniyahmuslimpro_web/
├── index.html          # Main HTML file
├── styles.css          # All CSS styles
├── script.js           # JavaScript for interactivity
├── assets/             # Images and media files
│   └── README.md       # Image requirements
└── README.md           # This file
```

## Getting Started

1. **Add Images**: Place all required images in the `assets/` folder (see `assets/README.md` for the list)

2. **Open in Browser**: Simply open `index.html` in your web browser

3. **Customize**: 
   - Update text content in `index.html`
   - Modify colors in `styles.css` (CSS variables in `:root`)
   - Adjust functionality in `script.js`

## Customization

### Colors
Edit the CSS variables in `styles.css`:
```css
:root {
    --primary-color: #1a472a;
    --secondary-color: #2d5a3d;
    --accent-color: #4a7c59;
    /* ... */
}
```

### Content
All content can be edited directly in `index.html`. Search for "Tijaniyah Muslim Pro" to find all instances that need customization.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Notes

- Images are referenced but not included. Please add appropriate images to the `assets/` folder.
- The newsletter form currently shows an alert on submission. Connect it to your backend API.
- Language selector is functional but needs backend integration for actual language switching.

## License

Copyright © 2025 Tijaniyah Muslim Pro. All rights reserved.

