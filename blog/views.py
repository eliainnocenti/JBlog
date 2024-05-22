from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

class AboutView(TemplateView):
    """
    View for displaying the about page.
    """
    template_name = 'blog/about.html'

    # You can add any additional methods here if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any context data here if needed
        return context


class PostListView(ListView):
    """
    View for displaying a list of blog posts.
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    """
    View for displaying a detailed view of a blog post.
    """
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new blog post.
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        """
        Validate the form and set the author of the post to the current user.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for updating an existing blog post.
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        """
        Validate the form and set the author of the post to the current user.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Check if the current user is the author of the post.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting a blog post.
    """
    model = Post
    success_url = '/'

    def test_func(self):
        """
        Check if the current user is the author of the post.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
