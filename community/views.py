from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import Post, Comment, PostReaction
from .forms import PostForm, CommentForm


@login_required
def feed(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community:feed')
    else:
        post_form = PostForm()

    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    for post in page_obj:
        post.likes_count = post.reactions.filter(value=1).count()
        post.dislikes_count = post.reactions.filter(value=-1).count()
        reaction = PostReaction.objects.filter(user=request.user, post=post).first()
        post.user_reaction = reaction.value if reaction else 0

    return render(request, 'community/feed.html', {
        'page_obj': page_obj,
        'post_form': post_form,
        'comment_form': CommentForm()
    })


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('community:feed')


@login_required
def react_post(request, post_id, value):
    post = get_object_or_404(Post, id=post_id)

    value = int(value)  # NOW -1 WORKS

    reaction = PostReaction.objects.filter(
        user=request.user,
        post=post
    ).first()

    if reaction:
        if reaction.value == value:
            reaction.delete()
        else:
            reaction.value = value
            reaction.save()
    else:
        PostReaction.objects.create(
            user=request.user,
            post=post,
            value=value
        )

    return JsonResponse({
        'likes': post.reactions.filter(value=1).count(),
        'dislikes': post.reactions.filter(value=-1).count(),
        'user_reaction': (
            PostReaction.objects.filter(user=request.user, post=post).first().value
            if PostReaction.objects.filter(user=request.user, post=post).exists()
            else 0
        )
    })
