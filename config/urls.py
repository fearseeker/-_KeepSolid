
from django.contrib import admin
from django.urls import path, include
from src.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('books/', include('src.urls')),
    path('', book_list, name='home'),
]
