from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit.'
POST_TEMPLATE = '''
          --- {} ---
          
          {}
          
          '''
blogs = dict() # blog_name : Blog object

def menu():
    # Show the user the availible blogs
    # Let the user make a choice
    # Do something with that choice
    # Exit the program
    
    print_blogs()
    selection = input(MENU_PROMPT)
    
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)
    
def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")

def ask_create_blog():
    blog_title = input('Title of the blog? ')
    blog_author = input('whats your name? ')
    
    blogs[blog_title] = Blog(blog_title, blog_author)

def ask_read_blog():
    title = input('enter the blog title')
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_posts(post)
        
def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    pass

        
if __name__ == "__main__":
    print_blogs()