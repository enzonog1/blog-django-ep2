from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Post


# Versão 3: classes genéricas (ListView, DetailView, CreateView, UpdateView, DeleteView).

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-posted_at']


class PostDetailView(DetailView):  # 404 automático se o post não existir
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):  # depois de salvar, vai para Post.get_absolute_url()
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


class PostDeleteView(DeleteView):  # GET mostra a confirmação, POST remove
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
