from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from cloudinary_storage import storage


def PostList(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_on')
        if 'q' in request.GET: 
            q = request.GET.get('q', '')
            posts = Post.objects.filter(category__name=q).order_by('-created_on')
        categories = Category.objects.all()
        context = {'posts': posts, 'categories': categories}
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


def add_post(request):

    if request.method == "GET":
        if not request.user.is_staff:
            return redirect(
                reverse('home')
            )
        post_form = PostForm()
        context = {
            "post_form": post_form
            }
        return render(request, 'add_post.html', context)

    if request.method == "POST":
        if not request.user.is_staff:
            return redirect(
                reverse('home')
            )

        post_form = PostForm(request.POST, request.FILES)
        print('ok')
        if post_form.is_valid():
            print(post_form.__dict__)
            post = post_form.save(commit=False)
            slug2 = slugify(post.title)
            post.slug = slug2
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            post_form = PostForm()

        return render(
            request,
            "post_edit.html",
            {
                "post_form": post_form
            })


def choose_category(request):
    if request.method == "GET":
        if not request.user.is_staff:
            return redirect(
                reverse('home')
            )


def delete_post(request, slug):
    if request.method == "GET":
        context = {
            "slug": slug
            }
        return render(request, 'post_delete.html', context)

    if request.method == "POST":
        if not request.user.is_staff:
            HttpResponseRedirect(reverse('home', args=[slug]))

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        storage.cloudinary.api.delete_resources([post.featured_image])
        post.delete()
        return HttpResponseRedirect(reverse('home'))


def edit_post(request, slug):

    if request.method == 'GET':
        if not request.user.is_staff:
            HttpResponseRedirect(reverse('home', args=[slug]))

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        post_form = PostForm(instance=post)
        print("post_image", post.featured_image.public_id)
        return render(
            request,
            "post_edit.html",
            {
                "post_form": post_form
            })

    if request.method == 'POST':
        if not request.user.is_staff:
            HttpResponseRedirect(reverse('post_detail', args=[slug]))

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        print('ok2', post)
        post_form = PostForm(request.POST, request.FILES, instance=post)
        print(post_form)
        if post_form.is_valid():
            print('ok2')
            post = post_form.save(commit=False)
            slug2 = slugify(post.title)
            post.slug = slug2
            post.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            post_form = PostForm(instance=post)

        return render(
            request,
            "post_edit.html",
            {
                "post_form": post_form
            })
