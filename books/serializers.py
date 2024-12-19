from rest_framework import serializers
from .models import Book, Author, Genre
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        ref_name = 'BooksUserSerializer'  # Add this line to avoid conflict

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    interested_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
