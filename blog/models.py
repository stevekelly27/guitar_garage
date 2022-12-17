from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    catagory = models.CharField(max_length=200, default='all')
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Catagory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


# class Question(models.Model):
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="blog_posts")
#     text = models.TextField(_('question'), help_text=_('Ask a question here!'))
#     slug = models.SlugField(_('slug'), max_length=100)
#     created_on = models.DateTimeField(auto_now_add=True)


# class Message(models.Model):
#     content = models.TextField()
#     email = models.EmailField()
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-created_on"]

#     def __str__(self):
#         return self.title

# class Add_Post(models.Model):
#     title = models.CharField(max_length=250, unique=True)
#     slug = models.SlugField(max_length=250, unique=True)
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="blog_posts")
#     featured_image = CloudinaryField('image', default='placeholder')
#     excerpt = models.TextField(blank=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-created_on"]

#     def __str__(self):
#         return self.title