from django.db import models
from django import forms

class AboutService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.title

# success story

class SuccessStory(models.Model):
    client_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.client_name

class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/')

    def __str__(self):
        return self.title


# get started

class CallToAction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_text = models.CharField(max_length=50, default="Get Started")
    button_link = models.URLField(max_length=200, default="/contact-us/")  # Default link for the button

    def __str__(self):
        return self.title

# about us

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_members/')
    bio = models.TextField()
    
    def __str__(self):
        return self.name


class Testimonial(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.content


class ClientLogo(models.Model):
    logo = models.ImageField(upload_to='client_logos/')
    alt_text = models.CharField(max_length=100)

    def __str__(self):  # Move it here
        return self.alt_text

# Services

# models.py
# services
class Service(models.Model):
    SERVICE_TYPES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile Development'),
        ('security', 'Cybersecurity'),
        ('consulting', 'Consulting'),
        ('training', 'Training'),
    ]
    title = models.CharField(max_length=255)  # Example field
    description = models.TextField()
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES, default='web')

    def __str__(self):
        return self.title


#  Case study

class CaseStudy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='case_studies/images/', blank=True, null=True)
    video = models.FileField(upload_to='case_studies/videos/', blank=True, null=True)

    def __str__(self):
        return self.title

# Contact form submit
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
# Form Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']  # Update with your model fields
        
# careers

class JobOpening(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    details_url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Help page

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class HelpContact(models.Model):
    category = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.category

class DownloadableGuide(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='docs/')
    
    def __str__(self):
        return self.title

# Support Ticket

class SupportTicket(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Ticket from {self.name} - {self.subject}"


# learning page

class LearningResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    category = models.CharField(max_length=100, choices=[
        ('python', 'Python'),
        ('django', 'Django'),
        ('html_css', 'HTML & CSS'),
        ('javascript', 'JavaScript')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
