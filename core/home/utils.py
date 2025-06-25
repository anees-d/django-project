from django.shortcuts import redirect
from .models import Students
import time
from django.core.mail import send_mail
from django.conf import settings

def run_this_function():
    print("function started ")
    time.sleep(1)
    print("Function executed")
    
    
    
def send_email_to_client(request):
    subject = "This email is from Django server"
    message = "This is a test message from the Django server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["aneesofficial15@gmail.com"]
    
    send_mail(subject, message, from_email, recipient_list)
    
    return redirect('/')  # or render a thank-you page