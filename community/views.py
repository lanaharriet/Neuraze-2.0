from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like


@login_required
def community_home(request):
    posts = Post.objects.all().order_by("-created")
    return render(request, "community/community_home.html", {"posts": posts})


@login_required
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created")
    liked = Like.objects.filter(post=post, user=request.user).exists()

    return render(request, "community/post_detail.html", {
        "post": post,
        "comments": comments,
        "liked": liked,
    })


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title.strip() and content.strip():
            Post.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            return redirect("community:home")

    return render(request, "community/create_post.html")


@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        text = request.POST.get("comment")
        post = get_object_or_404(Post, id=post_id)

        if text.strip():
            Comment.objects.create(
                post=post,
                user=request.user,
                comment=text
            )

    return redirect("community:view_post", post_id=post_id)


@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(post=post, user=request.user)

    if like.exists():
        like.delete()  # unlike
    else:
        Like.objects.create(post=post, user=request.user)  # like

    return redirect("community:view_post", post_id=post_id)
