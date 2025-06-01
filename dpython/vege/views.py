from django.shortcuts import render
from django.contrib import messages  # ✅ For flash messages
from .models import Recipe  # ✅ Import your model

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        # ✅ Input validation (optional but good practice)
        if recipe_name and recipe_description:
            Recipe.objects.create(
                recipe_name=recipe_name,
                recipe_description=recipe_description,
                recipe_image=recipe_image,
            )
            messages.success(request, "Recipe added successfully!")
        else:
            messages.error(request, "Please fill in all required fields.")

    all_recipes = Recipe.objects.all()  # ✅ Fetch all recipes
    return render(request, 'recipes.html', {'recipes': all_recipes})
