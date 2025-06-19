from django.shortcuts import render
from django.contrib import messages  # ✅ For flash messages
from .models import Recipe  # ✅ Import your model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from vege.models import Student, SubjectMarks
from django.contrib.auth import logout as auth_logout
from django.core.paginator import Paginator








def recipes(request):
    # POST logic for adding a recipe
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
            return redirect('recipes')  # Refresh and show new recipe
        else:
            messages.error(request, "Please fill all fields")

    # GET logic for listing + searching + pagination
    query = request.GET.get('q', '')
    recipe_list = Recipe.objects.all()

    if query:
        recipe_list = recipe_list.filter(recipe_name__icontains=query)

    paginator = Paginator(recipe_list, 5)  # 5 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes.html', {
        'recipes': page_obj,
        'query': query,
    })

# Update Recipe
def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == "POST":
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.recipe_description = request.POST.get('recipe_description')

        if request.FILES.get('recipe_image'):
            recipe.recipe_image = request.FILES.get('recipe_image')

        recipe.save()
        messages.success(request, "Recipe updated successfully!")
        return redirect("recipes")  # or wherever you list recipes

    return render(request, "update_recipe.html", {"recipe": recipe})



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


#students


def get_students(request):
    query = request.GET.get('q', '')
    queryset = Student.objects.all()

    if query:
        queryset = queryset.filter(student_name__icontains=query)

    paginator = Paginator(queryset, 10)  # Show 5 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/students.html', {
        'queryset': page_obj,
        'query': query
    })
    
    
def see_marks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)

    # Add pagination (e.g., 5 marks per page)
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/see_marks.html', {'queryset': queryset})
