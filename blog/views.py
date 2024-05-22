from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm

def is_writer(user):
    return user.groups.filter(name='writers').exists()

@login_required
def home(request): # TODO: check if it's necessary to create a home.html file
    group_name = 'writers'
    return render(request, 'base.html', {'group_name': group_name})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

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

    def get_success_url(self):
        """
        Redirect to the list of posts after creating a new post.
        """
        return reverse_lazy('post_list')

    def form_valid(self, form):
        """
        Validate the form and set the author of the post to the current user.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # TODO: is it a redundant method? (the form_valid method should be enough, the author of a post must be in the writers group)
        """
        Check if the current user is in the writers group.
        """
        return is_writer(self.request.user)

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
