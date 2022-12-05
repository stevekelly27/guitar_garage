from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse
from .models import Post


def PostList(request):
    if request.method == 'GET':
        post = Post.objects.all().order_by('-created_on')
        context = {'post': post}
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
        context = {'post': post}
        return render(request, 'post_details.html', context)

    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.body = request.POST.get('body')
        task.save()
        return redirect('index.html')
