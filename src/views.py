from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .forms import *
from .models import *
import csv



def book_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user,
            book=book
        ).exists()

    return render(request, 'book_detail.html', {
        'book': book,
        'is_favorite': is_favorite
    })

@login_required
@user_passes_test(lambda u: u.is_admin)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_admin)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

@login_required
@user_passes_test(lambda u: u.is_admin)
def export_books_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Название', 'Автор(ы)', 'Жанр(ы)', 'Описание'])
    for book in Book.objects.all():
        authors = ', '.join([str(a) for a in book.authors.all()])
        genres = ', '.join([g.name for g in book.genres.all()])
        writer.writerow([book.title, authors, genres, book.description])
    return response

@login_required
@user_passes_test(lambda u: u.is_admin)
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_add')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_admin)
def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_add')
    else:
        form = GenreForm()
    return render(request, 'genre_form.html', {'form': form})


@login_required
def add_to_favorites(request, pk):
    book = get_object_or_404(Book, pk=pk)

    Favorite.objects.get_or_create(
        user=request.user,
        book=book
    )

    return redirect('book_list')

@login_required
def remove_from_favorites(request, pk):
    book = get_object_or_404(Book, pk=pk)

    Favorite.objects.filter(
        user=request.user,
        book=book
    ).delete()

    return redirect('book_list')

@login_required
def favorite_list(request):
    favorites = Book.objects.filter(
        favorited_by__user=request.user
    )

    return render(request, 'favorite_list.html', {
        'books': favorites
    })