
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import learning



from . import views  # Import views from the same app

urlpatterns = [
    
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.home, name='home'),           # Home page
    path('about/', views.about, name='about'),   # About page
    path('services/', views.services, name='services'),  # Services page
    path('contact-us/', views.contact, name='contact-us'),      # Contact page
    path('submit-contact-form/', views.submit_contact_form, name='submit-contact-form'),


    path('careers/', views.careers, name='careers'),      # Careers page
    path('help/', views.help, name='help'),      # Careers page
    path('submit-ticket/', views.submit_ticket, name='submit_ticket'),  # Matches the template
    path('ticket-success/', views.ticket_success, name='ticket-success'),

    path('learning/', views.learning, name='learning_page'),      # Learning page
    path('careers/frontend-developer/', views.frontend_developer, name='frontend_developer'), # front end
    path('careers/backend-developer/', views.backend_developer, name='backend_developer'), # back end
    path('careers/ui-ux-designer/', views.ui_ux_designer, name='ui_ux_designer'), # Ui design
    path('careers/project-manager/', views.project_manager, name='project_manager'), # project manager
    path('request-quote/', views.request_quote, name='request_quote'),
    path('learn-more/', views.learn_more, name='learn_more'),
    path('blogs/', views.blogs, name='blogs'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('webinars/', views.webinars, name='webinars'),
    path('case-studies/', views.case_studies, name='case-studies'),
    
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

