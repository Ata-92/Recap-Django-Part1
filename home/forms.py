from django.forms import fields, widgets
from home.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Phone Number"}),
            "email": forms.EmailInput(attrs={"placeholder": "Phone Number"}),
            "message": forms.TextInput(attrs={"placeholder": "Message"}),
        }
