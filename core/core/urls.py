"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import*
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include



urlpatterns = [
    path('', home, name="home"), 
    path('recipes/', recipes, name="recipes"),
    path('contact/', contact,  name="contact"), 
    path('about/', about,  name="about"), 

    path('recipe/update/<int:id>/', update_recipe, name='update_recipe'),
    path('recipe/delete/<int:id>/', delete_recipe, name='delete_recipe'),

    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('success-page/', success_page, name="success_page"),
    path('students/', get_students, name="get_students"),
    path('see_marks/<int:student_id>/', see_marks, name='see_marks'),
    
    path('send-email/', send_email_to_client, name='send_email'),


    path('admin/', admin.site.urls),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)