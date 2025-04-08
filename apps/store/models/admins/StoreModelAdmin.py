from django.contrib import admin


class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_editable = ['price']
