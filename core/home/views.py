from django.shortcuts import render, redirect
from django.core.mail import send_mail

from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client

def send_email(request):
    send_email_to_client
    return redirect('/')

def home(request):
    
    seed_db(100)
    
    peoples = [
        {'name': 'Anees', 'age': 26},
        {'name': 'Ali', 'age': 17},
        {'name': 'Ahmad', 'age': 29},
        {'name': 'Saboor', 'age': 52},
        {'name': 'Sameen', 'age': 15},
        
    ]
    
    for person in peoples:  # ✅ Use a different variable name
        if person['age']: 
            print("yes")

    vegetables = {'pumpkin', 'tomato', 'potato', 'cocumber'}

    return render(request, "home/index.html", context={'peoples': peoples, 'vegetables': vegetables, 'page' : 'django 2023 tuttorial'})

def about(request):
    
    context = {'page' : 'About'}

  
    return render(request, "about.html", context)

def contact(request):
    
    context = {'page' : 'Contact'}
    
    return render(request, "contact.html", context)
    

def success_page(request):
    print("✅ Success Page Loaded")
    context = {'page' : 'Contact'}

    return HttpResponse("<h1> This is a success page</h1>")
