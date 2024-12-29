from django.shortcuts import render
from django.http import JsonResponse


# Home page view
def home(request):
    return render(request, 'home.html')

# About page view
def about(request):
    return render(request, 'about.html')

# Services page view
def services(request):
    return render(request, 'services.html')

# Contact page view
def contact(request):
    return render(request, 'contact-us.html')

# careers page

def careers(request):
    return render(request, 'careers.html')

# help page

def help(request):
    return render(request, 'help.html')

# Learning page

def learning(request):
    return render(request, 'learning.html')

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
        # Extract data from the request (e.g., user email, query)
        ticket_data = {
            'email': request.POST.get('email'),
            'query': request.POST.get('query'),
        }
        # Save the ticket data to the database (assumes a Ticket model exists)
        # Ticket.objects.create(**ticket_data)

        return JsonResponse({'status': 'success', 'message': 'Ticket submitted successfully.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})


# blog section


def blogs(request):
    return render(request, 'blogs.html')  # File directly in templates

def tutorials(request):
    return render(request, 'tutorials.html')

def webinars(request):
    return render(request, 'webinars.html')

def case_studies(request):
    return render(request, 'case_studies.html')



