from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import slugify


class TestModels(TestCase):

    def setUp(self):
        """Create test data"""
        self.user = User.objects.create(username='testname')
        self.user.set_password('1234')
        self.user.save()
        self.c1 = Category.objects.create(name='pedals', description='test description')
        self.c2 = Category.objects.create(name='amps', description='fender-amps')
        self.c3 = Category.objects.create(name='guitar', description='gibson')
        self.p1 = Post.objects.create(title='test', slug=slugify('test'), author=self.user, category=self.c1, featured_image=SimpleUploadedFile(
            name='walrus-audio.jpeg', content=open('media/walrus-audio.jpeg', 'rb').read(), content_type='image/jpeg'), excerpt='test', content='test')
        self.com1 = Comment.objects.create( name='test', post=self.p1, email='test', body='test', approved=True)

    def test_post_model_str(self):
        """Test the __str__ method for post"""
        self.assertEqual(self.p1.__str__(), self.p1.title)

    def test_comment_model_str(self):
        """Test the __str__ method for comment"""
        self.assertEqual(
            self.com1.__str__(),
            f'Comment {self.com1.body} by {self.com1.name}'
            )
