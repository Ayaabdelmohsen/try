"""book_store_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin

#from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from .views import BookViewSet

#router = DefaultRouter()
#router.register(r'books', BookViewSet, basename='book')

#urlpatterns = [
    #path('admin/', admin.site.urls),
 #   path('api/', include('book_store_app.urls')),
#]
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,BookDetailView,AuthorListView, AuthorDetailView
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path('books/', BookViewSet.as_view({'get': 'list'}), name='book-list'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
      path('api/authors/', AuthorListView.as_view(), name='author-list'),
    path('api/authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]