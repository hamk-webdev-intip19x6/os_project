from django.db import models

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
    desc = models.CharField(max_length=200)
    pub_date = models.IntegerField()
    def __str__(self):
        return self.title
