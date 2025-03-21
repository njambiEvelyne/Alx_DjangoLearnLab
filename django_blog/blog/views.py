from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q  # Used for search functionality

from .models import Post, Comment, Tag
from .forms import CommentForm, EditProfileForm, RegisterForm, PostForm


# Home View
def home_view(request):
    return render(request, "blog/home.html")


# Blog Post List
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


# Blog Post Detail
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update an existing post (only the author can edit)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        return self.request.user == self.get_object().author


# Delete a post (only the author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        return self.request.user == self.get_object().author


# User Registration
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


# User Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})


# User Logout
def logout_view(request):
    logout(request)
    return redirect("login")


# User Profile
@login_required
def profile_view(request):
    return render(request, "blog/profile.html", {"user": request.user})


# Edit Profile
@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "blog/edit_profile.html", {"form": form})


# Add a new comment
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, "comments/add_comment.html", {"form": form, "post": post})


# Edit an existing comment
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "comments/edit_comment.html", {"form": form, "comment": comment})


# Delete a comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post_id = comment.post.id
    comment.delete()
    return redirect('post-detail', pk=post_id)


# Class-based comment creation
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/add_comment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


# Class-based comment update
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/edit_comment.html"

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


# Class-based comment deletion
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comments/delete_comment.html"

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


# View for listing posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


# View for displaying a single post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


# View for filtering posts by tag
def posts_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts.all()
    return render(request, "blog/posts_by_tag.html", {"tag": tag, "posts": posts})


# View for searching posts
def search_posts(request):
    query = request.GET.get("q", "")
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, "blog/search_results.html", {"query": query, "posts": posts})
