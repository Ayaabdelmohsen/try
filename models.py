# book_store_app/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.reviewer_name} - {self.book.title}"
