from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),  # Include the app URLs
    path('learning/', include('myapp.urls')),  # Add your app’s URLs here

]
