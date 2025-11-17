// Load header and footer into pages
document.addEventListener('DOMContentLoaded', function() {
    // Determine base path based on current page location
    const currentPath = window.location.pathname;
    let basePath = '';
    const isSubdirectory = currentPath.includes('/about-us/') || 
                           currentPath.includes('/contact-us/') || 
                           currentPath.includes('/privacy-policy/') || 
                           currentPath.includes('/terms/');
    
    if (isSubdirectory) {
        basePath = '../';
    }
    
    // Function to fix paths in loaded HTML
    function fixPaths(html, isSubdir) {
        if (!isSubdir) return html;
        
        // Fix asset paths
        html = html.replace(/src="assets\//g, 'src="../assets/');
        // Fix links to root pages
        html = html.replace(/href="index\.html"/g, 'href="../index.html"');
        html = html.replace(/href="about-us\/index\.html"/g, 'href="../about-us/index.html"');
        html = html.replace(/href="contact-us\/index\.html"/g, 'href="../contact-us/index.html"');
        html = html.replace(/href="privacy-policy\/index\.html"/g, 'href="../privacy-policy/index.html"');
        html = html.replace(/href="terms\/index\.html"/g, 'href="../terms/index.html"');
        html = html.replace(/href="features\/index\.html"/g, 'href="../features/index.html"');
        html = html.replace(/href="winter-aid\/index\.html"/g, 'href="../winter-aid/index.html"');
        
        return html;
    }
    
    // Load header
    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder) {
        fetch(basePath + 'header.html')
            .then(response => response.text())
            .then(data => {
                const fixedData = fixPaths(data, isSubdirectory);
                headerPlaceholder.innerHTML = fixedData;
                // Reinitialize any scripts that might be needed
                if (typeof breakdance !== 'undefined') {
                    breakdance.init();
                }
            })
            .catch(error => console.error('Error loading header:', error));
    }
    
    // Load footer
    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
        fetch(basePath + 'footer.html')
            .then(response => response.text())
            .then(data => {
                const fixedData = fixPaths(data, isSubdirectory);
                footerPlaceholder.innerHTML = fixedData;
            })
            .catch(error => console.error('Error loading footer:', error));
    }
});

