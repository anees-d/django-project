from django.contrib import admin
from .models import Recipe, Department, StudentID, Student, Subjects, SubjectMarks
from django.db.models import Sum    
from .models import ReportCard



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
    list_display = ['student', 'student_rank', 'get_total_marks', 'date_of_report_card_generation']
    
    def get_total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student=obj.student)
        marks = subject_marks.aggregate(total=Sum('marks'))
        return marks['total'] or 0  # Ensure it returns 0 if None

    get_total_marks.short_description = 'Total Marks'  # Optional: Rename column header in admin


admin.site.register(ReportCard, ReportCardAdmin)