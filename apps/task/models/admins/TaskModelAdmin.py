from django.contrib import admin


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'user', 'start_date', 'end_date', 'price', 'status']
    list_editable = ['category', 'status']
