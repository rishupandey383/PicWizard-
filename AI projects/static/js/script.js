document.addEventListener('DOMContentLoaded', function() {
    const promptInput = document.getElementById('prompt-input');
    const generateBtn = document.getElementById('generate-btn');
    const downloadBtn = document.getElementById('download-btn');
    const imageResult = document.getElementById('image-result');
    const loadingSpinner = document.getElementById('loading-spinner');
    
    generateBtn.addEventListener('click', generateImage);
    downloadBtn.addEventListener('click', downloadImage);
    
    async function generateImage() {
        const prompt = promptInput.value.trim();
        
        if (!prompt) {
            alert('Please enter a text prompt');
            return;
        }
        
        // Show loading spinner
        generateBtn.disabled = true;
        loadingSpinner.classList.remove('hidden');
        
        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: prompt })
            });
            
            if (!response.ok) {
                throw new Error('Image generation failed');
            }
            
            const data = await response.json();
            
            // Display the generated image
            imageResult.innerHTML = `<img src="${data.image_url}" alt="Generated image from prompt: ${prompt}">`;
            downloadBtn.classList.remove('hidden');
            downloadBtn.setAttribute('data-image-url', data.image_url);
            
        } catch (error) {
            console.error('Error:', error);
            imageResult.innerHTML = `<p class="error">Error generating image: ${error.message}</p>`;
        } finally {
            generateBtn.disabled = false;
            loadingSpinner.classList.add('hidden');
        }
    }
    
    function downloadImage() {
        const imageUrl = downloadBtn.getAttribute('data-image-url');
        if (!imageUrl) return;
        
        const link = document.createElement('a');
        link.href = imageUrl;
        link.download = `generated-image-${Date.now()}.png`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
});
// Theme Toggle Functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Check for saved theme or use system preference
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark' || (!currentTheme && prefersDarkScheme.matches)) {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
    
    // Toggle theme on button click
    themeToggle.addEventListener('click', function() {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        document.documentElement.setAttribute('data-theme', isDark ? 'light' : 'dark');
        localStorage.setItem('theme', isDark ? 'light' : 'dark');
    });
});