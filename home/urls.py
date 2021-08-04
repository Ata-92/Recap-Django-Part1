from home.views import about_view, home_view, teacher_view
from django.urls import path

# app_name = "home"

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("teacher/", teacher_view, name="teacher")
]
