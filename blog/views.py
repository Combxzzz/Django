from django.shortcuts import render
from blog import data

# Create your views here.

def blog(request):
    
    context = {
        'text' : 'ESTAMOS NO BLOG',
        'title' : 'Blog',
        'posts' : data.posts,
    }
    
    return render(
        request,
        'blog/index.html',
        context=context,
    )
    
def post(request, post_id):
    post_data = None
    for post in data.posts:
        if post['id'] == int(post_id):
            post_data = post
            break
    
    context = {
        'text' : 'ESTAMOS NO POST',
        'title' : f"Post {post_id}",
        'post' : post_data,
    }
    
    return render(
        request,
        'partials/post.html',
        context=context,
    )   
    

def comentarios(request):
    
    context = {
        'text' : 'ESTAMOS NO COMENTARIOS',
        'title' : 'comentarios',
        'coments' : data.coments,
    }
    
    return render(
        request,
        'blog/comentarios.html',
        context=context
    )
