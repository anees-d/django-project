from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings
import os
from home.models import Car
import random  # ✅ Make sure random is imported

def send_email_view(request):
    subject = "Email with Attachment"
    message = "Please find the attached Excel file."
    recipient_list = ["aneesofficial15@gmail.com"]

    file_path = r"D:\django-project\core\home\test.txt"
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')

def home(request):
    # ✅ Create Car object on every page reload
    Car.objects.create(car_name=f"Nexon-{random.randint(0, 100)}", speed=120)

    # ✅ Your existing data
    peoples = [
        {'name': 'Anees', 'age': 26},
        {'name': 'Ali', 'age': 17},
        {'name': 'Ahmad', 'age': 29},
        {'name': 'Saboor', 'age': 52},
        {'name': 'Sameen', 'age': 15},
    ]

    vegetables = {'pumpkin', 'tomato', 'potato', 'cocumber'}

    # ✅ Return the home.html template with context
    return render(request, "home.html", context={
        'peoples': peoples,
        'vegetables': vegetables,
        'page': 'django 2023 tutorial'
    })

def about(request):
    context = {'page': 'About'}
    return render(request, "about.html", context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "contact.html", context)

def success_page(request):
    print("✅ Success Page Loaded")
    return HttpResponse("<h1>This is a success page</h1>")
