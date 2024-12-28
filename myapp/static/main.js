function toggleMission() {
    const mission = document.getElementById('mission');
    if (mission.style.display === 'none' || mission.style.display === '') {
        mission.style.display = 'block';
    } else {
        mission.style.display = 'none';
    }
}

let slideIndex = 0;

function showSlides() {
    const slides = document.getElementsByClassName('slide');

    // Hide all slides
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }

    // Increment the slide index
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1; // Reset to the first slide
    }

    // Show the current slide
    slides[slideIndex - 1].style.display = 'block';

    // Repeat every 3 seconds
    setTimeout(showSlides, 3000);
}

// Start the slideshow
document.addEventListener('DOMContentLoaded', () => {
    showSlides();


    // get started button

    document.addEventListener('DOMContentLoaded', () => {
        document.addEventListener('DOMContentLoaded', () => {
            const ctaButton = document.getElementById('cta-button');
        
            if (ctaButton) {
                ctaButton.addEventListener('click', () => {
                    alert('Thank you for getting started with us!');
                });
            } else {
                console.error('Button with ID "cta-button" not found.');
            }
        });
        
    });
});
