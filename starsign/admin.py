from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("birth_date", "get_zodiac_sign", "mobile_number")
    search_fields = ("birth_date", "mobile_number")

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ["get_zodiac_sign"]
        return []


admin.site.register(User, UserAdmin)
