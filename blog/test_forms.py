from django.test import TestCase
from .forms import CommentForm, PostForm
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category


class TestForms(TestCase):
    """
    Test fields on post form
    """
    def setUp(self):
        c1 = Category(name='pedals', description='test description')
        c1.save()
        c2 = Category(name='amps', description='fender-amps')
        c2.save()
        c3 = Category(name='guitar', description='gibson')
        c3.save()

    def test_post_title_is_required(self):
        """Test that title field is required"""
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_form_valid(self):
        """Test that content field is required"""
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
        form = PostForm({'title': 'test', 'category': Category.objects.get(id=1), 'featured_image': SimpleUploadedFile(
            name='walrus-audio.jpeg', content=open('media/walrus-audio.jpeg', 'rb').read(), content_type='image/jpeg'), 'excerpt':'test', 'content':'test'})
        self.assertTrue(form.is_valid())
        
    def test_comment_form(self):
        form = CommentForm({'body': 'text'})
        self.assertTrue(form.is_valid())
