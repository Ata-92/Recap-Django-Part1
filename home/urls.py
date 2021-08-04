from home.views import home_view
from django.urls import path

# app_name = "home"

urlpatterns = [
    path("", home_view, name="home")
]
