
from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.home, name='home'),           # Home page
    path('about/', views.about, name='about'),   # About page
    path('services/', views.services, name='services'),  # Services page
    path('contact/', views.contact, name='contact'),      # Contact page
    path('careers/', views.careers, name='careers'),      # Careers page
    path('help/', views.help, name='help'),      # Careers page
    path('learning/', views.learning, name='learning'),      # Learning page
    path('careers/frontend-developer/', views.frontend_developer, name='frontend_developer'), # front end
    path('careers/backend-developer/', views.backend_developer, name='backend_developer'), # back end
    path('careers/ui-ux-designer/', views.ui_ux_designer, name='ui_ux_designer'), # Ui design
    path('careers/project-manager/', views.project_manager, name='project_manager'), # project manager

]
