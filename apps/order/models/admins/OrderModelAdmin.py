from django.contrib import admin

class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['cost', 'payment_type', 'payment_external_id', 'status', 'created_at', 'pay_at']
    list_editable = ['payment_type', 'status']