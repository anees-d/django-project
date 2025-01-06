document.addEventListener('DOMContentLoaded', () => {
    // Toggle Mission Section
    const mission = document.getElementById('mission');
    const toggleMission = () => {
        if (mission) {
            mission.style.display = (mission.style.display === 'none' || mission.style.display === '') ? 'block' : 'none';
        }
    };

    // Slideshow
    let slideIndex = 0;
    const showSlides = () => {
        const slides = document.getElementsByClassName('slide');
        if (slides.length > 0) {
            for (let i = 0; i < slides.length; i++) {
                slides[i].style.display = 'none'; // Hide all slides
            }
            slideIndex = (slideIndex % slides.length) + 1; // Increment and wrap around
            slides[slideIndex - 1].style.display = 'block'; // Show current slide
            setTimeout(showSlides, 3000); // Repeat
        }
    };
    showSlides();

    // CTA Button Click
    const ctaButton = document.getElementById('cta-button');
    if (ctaButton) {
        ctaButton.addEventListener('click', () => {
            alert('Thank you for getting started with us!');
        });
    }

    // Testimonial Carousel
    const testimonials = document.querySelectorAll('.testimonial');
    if (testimonials.length > 0) {
        let index = 0;
        setInterval(() => {
            testimonials.forEach((testimonial, i) => {
                testimonial.style.display = i === index ? 'block' : 'none';
            });
            index = (index + 1) % testimonials.length;
        }, 5000);
    }

    // Resource Hub Toggle
    const resourceHub = document.getElementById('resource-hub');
    if (resourceHub) {
        const toggleButton = document.createElement('button');
        toggleButton.textContent = 'Toggle Resource Hub';
        toggleButton.style.cssText = `
            margin-bottom: 10px;
            padding: 8px 15px;
            border: none;
            background-color: #007BFF;
            color: #fff;
            border-radius: 5px;
            cursor: pointer;
        `;
        toggleButton.addEventListener('click', () => {
            resourceHub.style.display = (resourceHub.style.display === 'none' || resourceHub.style.display === '') ? 'block' : 'none';
        });
        resourceHub.parentNode.insertBefore(toggleButton, resourceHub);
    }

    // Support Ticket Button
    const supportTicketBtn = document.getElementById('support-ticket-btn');
    if (supportTicketBtn) {
        supportTicketBtn.addEventListener('click', () => {
            window.location.href = '/submit-ticket/';
        });
    }

    // Chatbot Button
    const chatbotBtn = document.getElementById('chatbot-btn');
    const chatbotContainer = document.getElementById('chatbot-container');
    if (chatbotBtn && chatbotContainer) {
        chatbotBtn.addEventListener('click', () => {
            chatbotContainer.style.display = 'block';
        });
    }

    // Form Validation
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (event) => {
            const name = document.getElementById('name');
            const email = document.getElementById('email');
            const phone = document.getElementById('phone');
            const message = document.getElementById('message');

            const validateEmail = (email) => /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email);
            const validatePhone = (phone) => /^\d{3}-\d{3}-\d{4}$/.test(phone);

            if (!name?.value.trim() || !email?.value.trim() || !validateEmail(email.value) || !phone?.value.trim() || !validatePhone(phone.value) || !message?.value.trim()) {
                alert('Please fill out all fields correctly.');
                event.preventDefault();
            }
        });
    }
});
