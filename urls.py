from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the app URLs
    path('learning/', include('myapp.urls')),  # Add your app’s URLs here
    path('myapp/', include(('myapp.urls', 'myapp'), namespace='myapp')),


]
