
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters
from .models import Book, Review, Author
from .serializers import BookSerializer, ReviewSerializer, AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name', 'publication_date']
    ordering_fields = ['title', 'author__name', 'publication_date']
    ordering = ['title']  


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        reviews = Review.objects.filter(book=instance)
        reviews_serializer = ReviewSerializer(reviews, many=True)
        return Response({**serializer.data, 'reviews': reviews_serializer.data})
    
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        books = Book.objects.filter(author=instance)
        books_serializer = BookSerializer(books, many=True)
        return Response({**serializer.data, 'books': books_serializer.data})