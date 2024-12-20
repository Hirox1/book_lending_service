from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('GOOD', 'Good'),
        ('USED', 'Used'),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Default set to avoid migration issue for existing data
    image = models.ImageField(upload_to='book_images/', blank=True, null=True, default='default_image.jpg')
    interested_users = models.ManyToManyField(
        User, related_name='interested_books', blank=True
    )

    def __str__(self):
        return self.title
