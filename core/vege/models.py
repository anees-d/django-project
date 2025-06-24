from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid





class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

# =====================
# Recipe Model
# =====================

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe')
    recipe_view_count = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.recipe_name)
            unique_slug = base_slug
            num = 1

            # Loop to ensure slug is unique
            while Recipe.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1

            self.slug = unique_slug
        
        super().save(*args, **kwargs)

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
    
# subjects

class Subjects(models.Model):
    subject_name = models.CharField(max_length = 100)
    


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
    is_deleted = models.BooleanField(default=False)

    
    objects = StudentManager()
    admin_objects = models.Manager

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = "student"


# Marks

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'
     
    class Meta:
        unique_together = ['student' , 'subject']
        
# Report Card

class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_card_generation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student_name} - Rank {self.student_rank}"

    class Meta:
        unique_together = ['student_rank', 'date_of_report_card_generation']

    
      
