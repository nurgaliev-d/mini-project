from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm 

def post_list(request):
    posts = Post.objects.all()  # Get all posts
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
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
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Create a form instance with submitted data
        if form.is_valid():  # Check if the form is valid
            post = form.save(commit=False)  # Create a post instance but don't save yet
            post.author = request.user  # Assign the current user as the author
            post.save()  # Save the post to the database
            return redirect('post_list')  # Redirect to the post list after saving
    else:
        form = PostForm()  # Create a blank form instance

    return render(request, 'blog/post_form.html', {'form': form})  # Render the form