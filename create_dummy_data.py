# myapp/management/commands/create_dummy_data.py
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from book_store_app.models import Author, Book, Review
from django.utils import timezone
from random import randint, choice

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating dummy data...')

        # Create authors
        authors = []
        for i in range(100):
            author = Author.objects.create(
                name=f'Author {i + 1}',
                birth_date=timezone.now(),
                biography=f'Biography for Author {i + 1}'
            )
            authors.append(author)

        # Create books
        books = []
        for i in range(1000):
            book = Book.objects.create(
                title=f'Book {i + 1}',
                author=choice(authors),
                publication_date=timezone.now(),
                price=randint(10, 100)
            )
            books.append(book)

        # Create reviews
        for i in range(3000):
            Review.objects.create(
                book=choice(books),
                reviewer_name=f'Reviewer {i + 1}',
                content=f'Dummy review content for Reviewer {i + 1}',
                rating=randint(1, 5)
            )

        self.stdout.write(self.style.SUCCESS('Dummy data created successfully!'))
