from django.contrib import admin

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'start_date', 'end_date', 'price'] 
    list_editable = ['category']