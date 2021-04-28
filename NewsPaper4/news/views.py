from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.core.paginator import Paginator
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm  # импортируем нашу форму
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


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


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'add.html'
    context_object_name = 'post'
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST
    permission_required = 'news.add_post'


class PostEditView(PermissionRequiredMixin, UpdateView):
    template_name = 'edit.html'
    form_class = PostForm
    permission_required = 'news.change_post'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = 'news.delete_post'


class PostDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'detail.html'
    queryset = Post.objects.all()
    permission_required = 'news.view_post'
    success_url = 'news/<int:pk>'


@login_required
def subscribe_View(request, pk):
    category = get_object_or_404(Category, id=request.POST.get('post.id'))
    sub = False
    if category.subscribers.filter(id=request.user.id).exists():
        sub = True
        category.subscribers.remove(request.user)
    else:
        category.subscribers.add(request.user)
        sub = False
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))
