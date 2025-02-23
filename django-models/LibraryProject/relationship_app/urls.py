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

