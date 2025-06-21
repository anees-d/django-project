from django.contrib import admin
from .models import Recipe, Department, StudentID, Student, Subjects, SubjectMarks


# Register your models here.

from.models import Recipe

admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subjects)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']
admin.site.register(SubjectMarks, SubjectMarkAdmin)

class ReportCardAdmin(admin.ModelAdmin): 
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_report_card_generation']
    
    def total_marks(self, obj):
        return obj.aggregate(Sum())

admin.site.register(ReportCard, ReportCardAdmin)