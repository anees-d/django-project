from django.contrib import admin
from .models import Recipe, Department, StudentID, Student


# Register your models here.

from.models import Recipe

admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)