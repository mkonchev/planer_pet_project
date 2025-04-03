from django.contrib import admin

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', 'balance', 'sub_active', 'sub_due_to_date']
    #list_editable = ['price']