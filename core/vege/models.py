from django.db import models

# =====================
# Recipe Model
# =====================
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe')
    recipe_view_count = models.IntegerField(default=1)

    def __str__(self):
        return self.recipe_name


# =====================
# Department Model
# =====================

class Department(models.Model):
    department = models.CharField(max_length=100)
    date_of_established = models.DateField(default='2000-01-01')  # Set your desired default

    def __str__(self):
        return self.department

    class Meta:
        ordering = ['department']



# =====================
# StudentID Model
# =====================
class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id


# =====================
# Student Model
# =====================
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField(default = 100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = "student"


# aggregate

for queryset in queryset:
    
