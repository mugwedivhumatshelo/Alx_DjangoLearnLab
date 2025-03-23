from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
path('posts/<int:post_id>/comments/', views.CommentListView.as_view(), name='comment_list'),
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('posts/<int:post_id>/comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('posts/<int:post_id>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete')
]

