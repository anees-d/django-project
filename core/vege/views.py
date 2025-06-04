from django.shortcuts import render
from django.contrib import messages  # ✅ For flash messages
from .models import Recipe  # ✅ Import your model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404



def recipes(request):
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        if recipe_name and recipe_description:
            Recipe.objects.create(
                recipe_name=recipe_name,
                recipe_description=recipe_description,
                recipe_image=recipe_image
            )
            messages.success(request, "Recipe added successfully!")
            return redirect('recipes')  # Optional, for clean redirect
        else:
            messages.error(request, "Please fill all fields")

    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})

# Update Recipe
def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.recipe_description = request.POST.get('recipe_description')
        if request.FILES.get('recipe_image'):
            recipe.recipe_image = request.FILES.get('recipe_image')
        recipe.save()
        messages.success(request, "Recipe updated successfully!")
        return redirect('recipe')

    return render(request, 'update_recipe.html', {'recipe': recipe})


# Delete Recipe
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect('recipe')

    return render(request, 'delete.html', {'recipe': recipe})



# Register View
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    
    return render(request, 'register.html')

# Login View
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Replace 'home' with your actual homepage URL name
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'login.html')

#  Logout View
def logout(request):
    auth_logout(request)
    return redirect('login')

from django.contrib.auth import logout as auth_logout

