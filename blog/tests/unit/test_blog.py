from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test author')
        
        self.assertEqual('Test', b.title)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([], b.posts)
        
    def test_repr(self):
        b = Blog('Test', 'Test author')
        expected = "Test by Test author (0 posts)"
        
        b2 = Blog('My Day', 'Dave')
        expected2 = "My Day by Dave (0 posts)"
        
        self.assertEqual(expected, b.__repr__())
        self.assertEqual(expected2, b2.__repr__())
        
    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test author')
        b.posts = ['Test post']
        expected = "Test by Test author (1 post)"
        
        b2 = Blog('Test 2', 'Test author 2')
        b2.posts = ['Test post', 'Another test post']
        expected2 = "Test 2 by Test author 2 (2 posts)"
        
        self.assertEqual(expected, b.__repr__())
        self.assertEqual(expected2, b2.__repr__())