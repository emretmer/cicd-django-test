from django.test import TestCase
from posts.models import Post  # Correct absolute import

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(title="Test Title", content="Test Content")
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.content, "Test Content")
