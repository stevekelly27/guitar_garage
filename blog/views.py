from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import DetailView, CreateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy


def PostList(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_on')
        context = {'posts': posts}
        return render(request, 'index.html', context)

    if request.method == 'POST':
        post = Post.objects.create(
            body=request.POST.get('body')
        )
        post.save()
        return redirect('index.html')


def PostDetail(request, pk):
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        # comments = Comment.objects.filter(approved=True)
        comments = post.comments.all()
        comment_form = CommentForm()
        context = {
            'post': post, "comments": comments, "comment_form": comment_form
            }
        return render(request, 'post_details.html', context)

    if request.method == 'POST':
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=pk)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(
                reverse("post_details", args=[post.id])
            )

        else:
            comment_form = CommentForm()

            return render(
                    request,
                    "post_details.html",
                    {
                        "post": post,
                        "comments": comments,
                        "commented": True,
                        "comment_form": comment_form,
                    },
                )


def About(request):
    return render(request, 'about.html')


def Home(request):
    return render(request, 'index.html')


def edit_post(request, pk):
    if request.method == "GET":
        if not request.user.is_staff:
            return redirect(
                reverse('home')
            )

    if request.method == "POST":
        if not request.user.is_staff:
            return redirect(
                reverse('home')
            )


def add_post(request):
    if request.method == "GET":
        if not request.user.is_staff:
            return redirect(
                reverse('home')
            )

    if request.method == "POST":
        if not request.user.is_staff:
            return redirect(
                reverse('home')
            )


# def delete_post(request, id=None):

#     delete_post = get_object_or_404(Post, id=id)

#     creator = delete_post.user.username

#     if request.method == "POST" and request.user.is_authenticated and request.user.username == creator:
#         delete_post.delete()
#         messages.success(request, "Post successfully deleted!")
#         return HttpResponseRedirect("/Blog/list/")

#     context = {'delete_post': delete_post, 'creator': creator}

#     return render(request, 'templates/delete_post.html', context)


# def delete_post(request, post_id=None):
#     post_to_delete = Post.objects.get(id=post_id)
#     post_to_delete.delete()
#     return redirect(
#                 reverse('home')
#             )

# def delete_post(DeleteView):
#     if request.method == "POST":
#         return render(request, 'delete_post.html', context)


# def delete_post(DeleteView):

#     if request.method == 'POST':
#         post = Post.objects.create(
#             body=request.POST.get('body')
#         )
#         post.save()
#         return redirect('delete_post.html')

# def message_me(request, pk):
#     if request.method == 'POST':
#         post = get_object_or_404(queryset, id=pk)
#         comments = post.comments.filter(approved=True).order_by("-created_on")

#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect(reverse("home", args=[post.id]))

#         else:
#             comment_form = CommentForm()

#             return render(request, pk)
