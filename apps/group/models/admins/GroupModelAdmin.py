from django.contrib import admin


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
