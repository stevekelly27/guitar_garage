from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import slugify
import unittest


class TestViews(TestCase):
    """
    Test blog app views
    """
    def setUp(self):
        """Create test data"""
        self.user = User.objects.create_superuser(username='testname', is_superuser=True, is_staff=True)
        self.user.set_password('1234')
        self.user.save()
        self.c1 = Category.objects.create(name='pedals', description='test description')
        self.c2 = Category.objects.create(name='amps', description='fender-amps')
        self.c3 = Category.objects.create(name='guitar', description='gibson')
        self.p1 = Post.objects.create(title='test', slug=slugify('test'), author=self.user, category=self.c1, featured_image=SimpleUploadedFile(
            name='walrus-audio.jpeg', content=open('media/walrus-audio.jpeg', 'rb').read(), content_type='image/jpeg'), excerpt='test', content='test')
        self.com1 = Comment.objects.create(name='test', post=self.p1, email='test', body='test', approved=True)  

    def test_get_recent_post_list(self):
        """Test home retrieval and correct template used"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_get_post_detail(self):
        """Test post_detail retrieval and correct template used"""
        response = self.client.get(
            reverse('post_details', args=[self.p1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_details.html', 'base.html')

    def test_get_post_add(self):
        """Test post_add retrieval and correct template used"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html', 'base.html')
        response = self.client.post('/add_post', {
            'title': 'test2',
            'category': Category.objects.get(id=1),
            'featured_image': SimpleUploadedFile(
                name='walrus-audio.jpeg', content=open('media/walrus-audio.jpeg', 'rb').read(), content_type='image/jpeg'), 'excerpt':'test',
            'content': 'test2'
            }, follow=True)
        self.assertEqual(response.status_code, 200)
        print(Post.objects.all())

    def test_get_post_edit(self):
        """Test post_edit retrieval and correct template used"""
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('edit_post', args=[self.p1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_edit.html', 'base.html')
        response = self.client.post(reverse('edit_post', args=[self.p1.slug]), {
            'title': 'test',
            'category': Category.objects.get(id=1),
            'featured_image': SimpleUploadedFile(
                name='walrus-audio.jpeg', content=open('media/walrus-audio.jpeg', 'rb').read(), content_type='image/jpeg'), 
            'excerpt': 'test',
            'content': 'test-change'})
        print(response.context)
        print(response.content.decode())
        # self.assertEqual(response.status_code, 200)
        # p = Post.objects.get(id=1)
        # self.assertEqual(p.content, 'change')

    def test_get_post_delete(self):
        """Test post_delete retrieval and correct template used"""
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('delete_post', args=[self.p1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_delete.html', 'base.html')
        print(Post.objects.get(id=1))
        response = self.client.post(reverse('delete_post', args=[self.p1.slug]))
        self.assertEqual(response.status_code, 302)
        p = Post.objects.count()
        print(p)
        self.assertEqual(p, 0)

    def test_post_comment(self):
        """Test post commenting feature"""
        self.client.force_login(self.user)
        response = self.client.post(
                    reverse('post_details',
                            args=[self.com1.id]),
                    data={'body': 'testcomment'})
        self.assertRedirects(
            response, reverse('post_details', args=[self.com1.id]))
