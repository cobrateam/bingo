from django.utils import unittest

from post.models import Post

class TestPost(unittest.TestCase):
    def test_post_should_have_title_and_content(self):
        post = Post.objects.create(title="test", content="some content to test")
        self.assertTrue(post)

    def test_post_unicode_should_be_the_title(self):
        post = Post.objects.create(title="test", content="some content to test")
        self.assertEqual("test", unicode(post))
