
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views  # Import views from the same app

urlpatterns = [
    path('', views.home, name='home'),           # Home page
    path('about/', views.about, name='about'),   # About page
    path('services/', views.services, name='services'),  # Services page
    path('contact-us/', views.contact, name='contact'),      # Contact page

    path('careers/', views.careers, name='careers'),      # Careers page
    path('help/', views.help, name='help'),      # Careers page
    path('learning/', views.learning, name='learning'),      # Learning page
    path('careers/frontend-developer/', views.frontend_developer, name='frontend_developer'), # front end
    path('careers/backend-developer/', views.backend_developer, name='backend_developer'), # back end
    path('careers/ui-ux-designer/', views.ui_ux_designer, name='ui_ux_designer'), # Ui design
    path('careers/project-manager/', views.project_manager, name='project_manager'), # project manager
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

