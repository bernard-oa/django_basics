from django.db import models
from django.utils import timezone


# Create your models here.
class News(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author


class SportNews(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.author


class Registration(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def shortenText(self):
        return self.body[:100]


# inheritance


class ContactInfo(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    address = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Customer(ContactInfo):
    phone = models.CharField(max_length=30)


class Staff(ContactInfo):
    position = models.CharField(max_length=30)


class Place(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Restaurant(Place):
    serves_pizza = models.BooleanField(default=False)
    serves_tuna = models.BooleanField(default=False)