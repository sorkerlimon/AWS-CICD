from django.contrib import admin
from .models import ApplyForm

class ApplyFormAdmin(admin.ModelAdmin):
    list_display = ['applicant_id','first_name','last_name', 'interested_for', 'cv','email', 'phonenumber', 'date_of_birth', 'want_to_work', 'highest_education', 'earliest_start_date', 'national_id', 'position']
    list_filter = ['interested_for', 'want_to_work', 'highest_education']

admin.site.register(ApplyForm, ApplyFormAdmin)
