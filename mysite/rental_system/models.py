from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.

# Writer, Director and so on
class Creator(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Type(models.Model):
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.type

class Genre(models.Model):
    genre = models.CharField(max_length=200)
    def __str__(self):
        return self.genre

class Publisher(models.Model):
    publisher = models.CharField(max_length=50)
    def __str__(self):
        return self.publisher

#Movie, Book, Comic and so on
class Work(models.Model):
    creators = models.ManyToManyField(Creator)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    publishers = models.ManyToManyField(Publisher)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    pub_date = models.IntegerField(
        default=2020,
        validators=[
            MaxValueValidator(datetime.date.today().year),
            MinValueValidator(1800)
        ]
    )
    def __str__(self):
        return self.title
        
class RentedWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rented_work = models.ForeignKey(Work, on_delete=models.CASCADE)
    rent_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    returned = models.BooleanField(default=False)
    date_returned = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username + " " + self.rented_work.title