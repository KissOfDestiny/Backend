from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostEditView, PostDeleteView, PostSearch

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),  # Ссылка на детали товара
    path('add/', PostCreateView.as_view(), name='add'),  # Ссылка на создание товара
    path('search/', PostSearch.as_view()),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='edit'),

]
