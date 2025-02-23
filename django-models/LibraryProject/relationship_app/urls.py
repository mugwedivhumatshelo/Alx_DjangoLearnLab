from django.urls import path
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
]

from django.urls import path
from . import views

urlpatterns = [
    # ... existing URL patterns ...
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<pk>/', views.delete_book, name='delete_book'),
]
from django.urls import path
from . import views

urlpatterns = [
    # ... existing URL patterns ...
    path('admin/', views.admin_view, name='admin_view'),
]

