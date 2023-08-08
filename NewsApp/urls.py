from django.urls import path
from .views import home, contact, newsp, newsDate, register, addUser, modelform, addModalForm

urlpatterns = [
    path("news/", newsp, name="news"),
    path("home/", home, name="home"),
    path("contact/", contact, name="contact"),
    path("newsdate/<int:year>", newsDate),
    path("signup/", register, name="register"),
    path("addUser/", addUser, name="addUser"),
    path("modelform/", modelform, name="form"),
    path("addmodelfrom/", addModalForm, name="modelform"),
]
