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

// Start the slideshow and add other functionalities
document.addEventListener('DOMContentLoaded', () => {
    // Initialize slideshow
    showSlides();

    // "Get Started" button functionality
    const ctaButton = document.getElementById('cta-button');
    if (ctaButton) {
        ctaButton.addEventListener('click', () => {
            alert('Thank you for getting started with us!');
        });
    } else {
        console.error('Button with ID "cta-button" not found.');
    }

    // Testimonial Carousel
    const testimonials = document.querySelectorAll('.testimonial');
    let index = 0;

    setInterval(() => {
        testimonials.forEach((testimonial, i) => {
            testimonial.style.display = i === index ? 'block' : 'none';
        });
        index = (index + 1) % testimonials.length;
    }, 5000); // Change every 5 seconds

    // Services page functionality
    const services = document.querySelectorAll('.service');
    services.forEach(service => {
        service.addEventListener('click', () => {
            alert(`You selected: ${service.querySelector('h2').textContent}`);
        });
    });
});

 // case study js
document.addEventListener('DOMContentLoaded', () => {
    const caseStudies = document.querySelectorAll('.case-study');

    caseStudies.forEach(caseStudy => {
        caseStudy.addEventListener('click', () => {
            alert(`Viewing details for: ${caseStudy.querySelector('h3').textContent}`);
        });
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const quoteButtons = document.querySelectorAll('.btn-quote');
    const learnButtons = document.querySelectorAll('.btn-learn');

    // Handle "Request a Quote" button click
    quoteButtons.forEach(button => {
        button.addEventListener('click', () => {
            alert("Redirecting to the Request a Quote form...");
            // Replace with the actual link to the quote form
            window.location.href = "/request-quote/";
        });
    });

    // Handle "Learn More" button click
    learnButtons.forEach(button => {
        button.addEventListener('click', () => {
            alert("Redirecting to more details about this service...");
            // Replace with the actual link to the service details page
            window.location.href = "/service-details/";
        });
    });
});

 // Request a Quote

document.addEventListener('DOMContentLoaded', () => {
    const quoteButtons = document.querySelectorAll('.btn-quote');
    const learnButtons = document.querySelectorAll('.btn-learn');

    // Redirect for "Request a Quote" button
    quoteButtons.forEach(button => {
        button.addEventListener('click', () => {
            window.location.href = "/request-quote/";
        });
    });

    // Redirect for "Learn More" button
    learnButtons.forEach(button => {
        button.addEventListener('click', () => {
            window.location.href = "/learn-more/";
        });
    });
});


// JavaScript for form validation
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        const name = document.getElementById("name");
        const email = document.getElementById("email");
        const phone = document.getElementById("phone");
        const message = document.getElementById("message");

        // Basic validation
        if (!name.value.trim()) {
            alert("Please enter your name.");
            event.preventDefault(); // Prevent form submission
            return;
        }

        if (!email.value.trim() || !validateEmail(email.value)) {
            alert("Please enter a valid email address.");
            event.preventDefault();
            return;
        }

        if (!phone.value.trim() || !validatePhone(phone.value)) {
            alert("Please enter a valid phone number.");
            event.preventDefault();
            return;
        }

        if (!message.value.trim()) {
            alert("Please enter a message.");
            event.preventDefault();
            return;
        }

        // If everything is valid, allow form submission
        alert("Form submitted successfully!");
    });

    // Helper function to validate email
    function validateEmail(email) {
        const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return re.test(String(email).toLowerCase());
    }

    // Helper function to validate phone (simple format: 123-456-7890)
    function validatePhone(phone) {
        const re = /^\d{3}-\d{3}-\d{4}$/;
        return re.test(phone);
    }
});


// JavaScript for form validation
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        const name = document.getElementById("name");
        const email = document.getElementById("email");
        const phone = document.getElementById("phone");
        const message = document.getElementById("message");

        // Basic validation
        if (!name.value.trim()) {
            alert("Please enter your name.");
            event.preventDefault(); // Prevent form submission
            return;
        }

        if (!email.value.trim() || !validateEmail(email.value)) {
            alert("Please enter a valid email address.");
            event.preventDefault();
            return;
        }

        if (!phone.value.trim() || !validatePhone(phone.value)) {
            alert("Please enter a valid phone number.");
            event.preventDefault();
            return;
        }

        if (!message.value.trim()) {
            alert("Please enter a message.");
            event.preventDefault();
            return;
        }

        // If everything is valid, allow form submission
        alert("Form submitted successfully!");
    });

    // Helper function to validate email
    function validateEmail(email) {
        const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return re.test(String(email).toLowerCase());
    }

    // Helper function to validate phone (simple format: 123-456-7890)
    function validatePhone(phone) {
        const re = /^\d{3}-\d{3}-\d{4}$/;
        return re.test(phone);
    }
});



// script.js
document.querySelectorAll('.faq h3').forEach((faqHeader) => {
    faqHeader.addEventListener('click', () => {
        const faq = faqHeader.parentElement;
        faq.classList.toggle('active');
    });
});
