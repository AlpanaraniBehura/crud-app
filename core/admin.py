from django.contrib import admin
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']  # Fields to show in list view
    list_display_links = ['name']        # Makes 'name' clickable for edit
