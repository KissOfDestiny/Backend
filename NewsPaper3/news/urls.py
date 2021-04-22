from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostEditView, PostDeleteView, PostSearch, subscribe_View

urlpatterns = [
    path('', PostList.as_view(), name='all'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),  # Ссылка на детали поста
    path('add/', PostCreateView.as_view(), name='add'),  # Ссылка на создание поста
    path('search/', PostSearch.as_view()),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='edit'),
    path('subscribe/<int:pk>', subscribe_View, name='Subscribe'),
]
