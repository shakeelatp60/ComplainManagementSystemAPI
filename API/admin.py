from django.contrib import admin
from .models import ComplainRecord
# Register your models here.
@admin.register(ComplainRecord)
class ComplainRecordAdmin(admin.ModelAdmin):
    list_display = ['id','complain_number', 'name', 'location', 'mobile_number', 'Description', 'date_time', 'Resolved']
