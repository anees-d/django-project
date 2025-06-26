from django.shortcuts import redirect
from .models import Students
import time
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse
import os


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


def send_email_with_attachment(subject, message, recipient_list, file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found at: {file_path}")
        return HttpResponse(f"❌ File not found at: {file_path}")

    try:
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=recipient_list
        )
        email.attach_file(file_path)
        email.send()
        print("✅ Email sent successfully with attachment.")
        return HttpResponse("✅ Email sent successfully with attachment.")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return HttpResponse(f"❌ Error sending email: {e}")
    