from django.contrib import admin
from home.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "email", "message"]

admin.site.register(Contact, ContactAdmin)
