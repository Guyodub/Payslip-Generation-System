from django.contrib import admin

# Register your models here.
#payslips/admin.pay

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "jobNumber", "jobTitle", "basicPay", "allowances", "deductions")

admin.site.register(UserProfile, UserProfileAdmin)