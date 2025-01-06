# admin.py
from django.contrib import admin
from myapp.models import Contact  # Correct import for admin.py
from .models import SupportTicket
from .models import FAQ, HelpContact, DownloadableGuide
from .models import Service, SuccessStory, Achievement, CallToAction, TeamMember, Testimonial, ClientLogo, AboutService, CaseStudy, JobOpening
from .models import LearningResource



# Register your models here
admin.site.register(Service)
admin.site.register(SuccessStory)
admin.site.register(Achievement)
admin.site.register(CallToAction)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(ClientLogo)
admin.site.register(AboutService)
admin.site.register(CaseStudy)
admin.site.register(Contact)
@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')  # Fields to display in the admin list view
    
admin.site.register(FAQ)
admin.site.register(HelpContact)
admin.site.register(DownloadableGuide)
admin.site.register(SupportTicket)

@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category')
    list_filter = ('category', 'created_at')

