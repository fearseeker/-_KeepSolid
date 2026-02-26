from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/add/', views.book_create, name='book_add'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('books/export/csv/', views.export_books_csv, name='export_books_csv'),
    path('author/add/', views.author_create, name='author_add'),
    path('genre/add/', views.genre_create, name='genre_add'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('book/<int:pk>/favorite/', views.add_to_favorites, name='add_to_favorites'),
    path('book/<int:pk>/unfavorite/', views.remove_from_favorites, name='remove_from_favorites'),

]