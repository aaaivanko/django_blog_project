from django.urls import path

from .views import (PostListView,
                    contact,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)


app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('home/', PostListView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete')
]