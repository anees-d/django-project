from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    peoples = [
        {'name': 'Anees', 'age': 26},
        {'name': 'Ali', 'age': 17},
        {'name': 'Ahmad', 'age': 29},
        {'name': 'Saboor', 'age': 52},
        {'name': 'Sameen', 'age': 15},
        
    ]
    
    for person in peoples:  # ✅ Use a different variable name
        if person['age']: 
            print("yes")

    vegetables = {'pumpkin', 'tomato', 'potato', 'cocumber'}

    return render(request, "home/index.html", context={'peoples': peoples, 'vegetables': vegetables, 'page' : 'django 2023 tuttorial'})

def about(request):
    
    context = {'page' : 'About'}

  
    return render(request, "about.html", context)

def contact(request):
    
    context = {'page' : 'Contact'}
    
    return render(request, "contact.html", context)
    

def success_page(request):
    print("✅ Success Page Loaded")
    context = {'page' : 'Contact'}

    return HttpResponse("<h1> This is a success page</h1>")
