from django.contrib import admin
from home.models import Contact, Teacher

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "email", "message"]

class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "speciality"]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Teacher, TeacherAdmin)
