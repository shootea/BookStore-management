from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 100)


    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    




# Create your models here.
