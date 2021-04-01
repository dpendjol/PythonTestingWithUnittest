from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test content', p.content)

    def test_repr(self):
        p = Post('Test', 'Test content')
        expected = "<POST title='Test' content='Test content'>"
        
        self.assertEqual(expected, p.__repr__())
    
    def test_json(self):
        p = Post('Test', 'Test content')
        expected = {'title': 'Test', 'content': 'Test content'}
        
        self.assertDictEqual(expected, p.json())
        
if __name__ == "__main__":
    unittest.main()