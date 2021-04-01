# System tests affect the whole system
from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class AppTests(TestCase):

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test title', 'Test author', 'q')
            app.menu()
            
            self.assertIsNotNone(app.blogs['Test title'])
    
    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:    
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                
                mocked_input.assert_called()

    def test_menu_calls_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        
        with patch('builtins.input') as mocked_input:
            with patch('app.print_posts') as mocked_print_posts:
                mocked_input.side_effect = ('r', 'Test', 'q')
                app.menu()
                
                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_menu_calls_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'Test', 'Test title', 'Test content', 'q')
            app.menu()
            
            self.assertIsNotNone(app.blogs['Test'].posts[0])
            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test content')
            
            
            
    def test_menu_print_prompts(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_call_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q') as mocked_input:
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        b = Blog('Test', 'Test author')
        b2 = Blog('Test 2', 'Test author')
        b3 = Blog('Test 3', 'Test author')
        app.blogs = {'Test': b}
        
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)
    
    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test post', 'Test content')
        app.blogs = {'Test': blog}
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])
            
    def test_print_posts(self):
        post = Post('Post title', 'Post content')
        expected = '''
          --- Post title ---
          
          Post content
          
          '''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            
            mocked_print.assert_called_with(expected)
    
    def test_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test title', 'Test content')
            app.ask_create_post()
            
            self.assertEqual(blog.posts[0].title, 'Test title')
            self.assertEqual(blog.posts[0].content, 'Test content')
            