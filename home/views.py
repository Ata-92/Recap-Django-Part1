from home.forms import ContactForm
from django.shortcuts import render

# Create your views here.

def home_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = ContactForm()

    return render(request, "index.html", {"form": form})

def about_view(request):
    return render(request, "about.html")

def teacher_view(request):
    return render(request, "teacher.html")

