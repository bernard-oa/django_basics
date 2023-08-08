from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import News
from .forms import RegistrationForm, RegistrationModel
from .models import Registration, Article
from django.contrib import messages  # import while working on flash messages

# Create your views here.


def newsp(request):
    obj = News.objects.get(id=1)

    context = {"data": obj}
    return render(request, "news.html", context)


def newsDate(request, year):
    article_list = News.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": article_list}

    return render(request, "newsdate.html", context)


def home(request):
    
    article = Article.objects.all()
    context = {"article":article}
    return render(request, "home.html", context)


def contact(request):
    return render(request, "contact.html")


def register(request):
    context = {"form": RegistrationForm}
    return render(request, "signup.html", context)


# adding user function
def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = Registration(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
            email=form.cleaned_data["email"],
            phone=form.cleaned_data["phone"],
        )

        myregister.save()
        messages.add_message(
            request, messages.SUCCESS, "You have signedup successfully"
        )

    return redirect("register")


# interacts with the modelform.html
def modelform(request):
    context = {"modelform": RegistrationModel}
    return render(request, "modelform.html", context)


def addModalForm(request):
    mymodelform = RegistrationModel(request.POST)

    if mymodelform.is_valid():
        mymodelform.save()

    return redirect("form")
