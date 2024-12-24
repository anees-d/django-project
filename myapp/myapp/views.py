from django.shortcuts import render

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
    return render(request, 'contact.html')

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




