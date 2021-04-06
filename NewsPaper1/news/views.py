from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter
from .forms import PostForm  # импортируем нашу форму


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'
    ordering = ['-dateCreation']
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'
    ordering = ['-dateCreation']
    paginate_by = 1
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'add.html'
    context_object_name = 'post'
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST


# дженерик для редактирования объекта
class PostEditView(UpdateView):
    template_name = 'edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


# дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'detail.html'
    queryset = Post.objects.all()
