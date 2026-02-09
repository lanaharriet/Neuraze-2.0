from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import Post, Comment, PostReaction


@login_required
def feed(request):

    # CREATE POST
    if request.method == "POST" and "create_post" in request.POST:
        content = request.POST.get("content")
        if content:
            Post.objects.create(
                author=request.user,
                content=content
            )
        return redirect('community:feed')

    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'community/feed.html', {
        'page_obj': page_obj
    })


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # ADD COMMENT
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(
                user=request.user,
                post=post,
                content=content
            )
        return redirect('community:post_detail', post_id=post.id)

    likes = post.reactions.filter(value=1).count()
    dislikes = post.reactions.filter(value=-1).count()

    return render(request, 'community/post_detail.html', {
        'post': post,
        'likes': likes,
        'dislikes': dislikes
    })


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author == request.user:
        post.delete()

    return redirect('community:feed')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user:
        post_id = comment.post.id
        comment.delete()
        return redirect('community:post_detail', post_id=post_id)

    return redirect('community:feed')


@login_required
def react_post(request, post_id, value):
    post = get_object_or_404(Post, id=post_id)
    value = int(value)

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
        'dislikes': post.reactions.filter(value=-1).count()
    })
