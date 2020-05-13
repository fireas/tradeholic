from django.urls import path
from .views import (checkout_view, HomeView, BookDetailView, addBook_view, livre_view)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout', checkout_view, name='checkout'),
    path('addbook', addBook_view, name='addbook'),
    path('l1', livre_view, name='l1'),
    path('book/<pk>/', BookDetailView.as_view(), name='book')
]