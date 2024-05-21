from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class BlogAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post_data = {'title': 'Test Post', 'content': 'This is a test post.'}
        self.post = Post.objects.create(title='Existing Post', content='Existing content.')

    def test_blog_post_creation(self):
        url = reverse('posts')
        response = self.client.post(url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)  # Check if a new post is created

    def test_blog_post_retrieval(self):
        url = reverse('post_update_delete', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    # Add more test methods for other views...

    def test_comment_creation(self):
        url = reverse('comment', args=[self.post.id])
        comment_data = {'post': self.post.id,'content': 'Test comment','author':"testing2", }
        response = self.client.post(url, comment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)  # Check if a new comment is created

# Create your tests here.
