from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CommentForm, PostForm
from .models import Category, Comment, Post


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


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        # Não chamar de self.post: esse nome é usado pelo Django para requisições POST.
        self.post_obj = get_object_or_404(Post, pk=kwargs['post_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post_obj
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.post_obj.pk})


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)  # 404 se a categoria não existir
    posts = category.posts.order_by('-posted_at')
    # Reaproveita o template de listagem de posts, que mostra o nome da categoria.
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})
