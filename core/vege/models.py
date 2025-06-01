from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe')
    recipe_view_count =models.IntegerField(default=1)
    
    

class Department(models.Model):
    
    department = models.CharField(max_length=100)
    # Fields
   # name = models.CharField(max_length=100, unique=True)
    #description = models.TextField(blank=True, null=True)
    #created_at = models.DateTimeField(auto_now_add=True)  # Set only once
    #updated_at = models.DateTimeField(auto_now=True)      # Auto update
    
    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']
        
       # db_table = 'department'  # Custom database table name
       # ordering = ['name']      # Default ordering by name (A-Z)
       # verbose_name = 'Department'          # Singular name in admin
       # verbose_name_plural = 'Departments'  # Plural name in admin

    def __str__(self):
        return self.name
    
    class StudentID(models.Model):
            student_id = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.student_id
    
    class Student(models.Model):
        student_name = models.CharField(max_length=100)
        student_id = models.OneToOneField(StudentID, relate_name ="studentid", on_delete-models)
        student_email = models.EmailField(unique=True)
        department = models.ForeignKey('Department', on_delete=models.CASCADE)
        student_age = models.IntegerField(default=18)
        is_active = models.BooleanField(default=True)
        
        def __str__(self) -> str:
            return self.student_name


    class Meta:
        ordering = ['student_name']
        verbose_name = "student"
