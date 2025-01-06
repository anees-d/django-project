from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Service, SuccessStory, Achievement, CallToAction
from .models import TeamMember, Testimonial, ClientLogo, CaseStudy, AboutService
from django.contrib import messages
from .forms import ContactForm 
from .models import JobOpening
from .models import FAQ, HelpContact, DownloadableGuide
from .forms import SupportTicketForm
from .models import LearningResource




# Home page view
def home(request):
    # Fetch all related data
    services = Service.objects.all()
    success_stories = SuccessStory.objects.all()
    achievements = Achievement.objects.all()
    call_to_action = CallToAction.objects.first()
    
    # Fetch about services safely
    about_services = AboutService.objects.all() if AboutService.objects.exists() else None

    # Debugging to confirm data
    print(f"Achievements: {achievements}")
    print(f"About Services: {about_services}")

    # Pass data to the template
    context = {
        'services': services,
        'success_stories': success_stories,
        'achievements': achievements,
        'call_to_action': call_to_action,
        'about_services': about_services,
    }
    return render(request, 'home.html', context)



# About page view
def about(request):
    
    team_members = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()
    client_logos = ClientLogo.objects.all()
    return render(request, 'about.html', {
        'team_members': team_members,
        'testimonials': testimonials,
        'client_logos': client_logos,
    })

# Services page view

def services(request):
    # Fetch services and case studies dynamically from the database
    services = Service.objects.all()
    case_studies = CaseStudy.objects.all()

    return render(request, 'services.html', {
        'services': services,
        'case_studies': case_studies,
    })

# Contact page view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Manually create and save the Contact object
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            return redirect('success_page')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

# careers page

def careers(request):
    job_listings = JobOpening.objects.filter(is_active=True)  # Fetch active jobs only
    return render(request, 'careers.html', {'job_listings': job_listings})

# help page

def help(request):
    
    faqs = FAQ.objects.all()
    contacts = HelpContact.objects.all()
    guides = DownloadableGuide.objects.all()
    
    return render(request, 'help.html', {
        'faqs': faqs,
        'contacts': contacts,
        'guides': guides
    })

# Learning page


def learning(request):
    resources = LearningResource.objects.all().order_by('-created_at')
    return render(request, 'learning.html', {'resources': resources})


# front end
def frontend_developer(request):
    return render(request, 'frontend_developer.html')


#back end

def backend_developer(request):
    return render(request, 'backend_developer.html')

# UI design

def ui_ux_designer(request):
    return render(request, 'ui_ux_designer.html')

# Project manager

def project_manager(request):
    return render(request, 'project_manager.html')

# request quote

def request_quote(request):
    return render(request, 'request-quote.html')

# learn more

def learn_more(request):
    return render(request, 'learn-more.html')

# submit page
def submit_ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket-success')
    else:
        form = SupportTicketForm()
    return render(request, 'submit_ticket.html', {'form': form})

def ticket_success(request):
    return render(request, 'ticket_success.html')


# blog section


def blogs(request):
    return render(request, 'blogs.html')  # File directly in templates

def tutorials(request):
    return render(request, 'tutorials.html')

def webinars(request):
    return render(request, 'webinars.html')

def case_studies(request):
    return render(request, 'case_studies.html')

# Contact form submit

def submit_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send an email, save to database)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # You can save the data to a database or send an email
            # Example: Sending a success message
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact-us')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact_us.html', {'form': form})

