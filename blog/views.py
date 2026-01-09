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

def comentarios(request):
    
    context = {
        'text' : 'ESTAMOS NO COMENTARIOS',
        'title' : 'comentarios'
    }
    
    return render(
        request,
        'blog/comentarios.html',
        context=context
    )
