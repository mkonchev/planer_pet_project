from django.contrib import admin


class MembershipModelAdmin(admin.ModelAdmin):
    list_display = ["group", "user", "inviter", "invite_reason"]
