from django.shortcuts import render

# Create your views here.

def blog(request):
    
    context = {
        'text' : 'ESTAMOS NO BLOG',
        'title' : 'Blog',
    }
    
    return render(
        request,
        'blog/index.html',
        context=context,
    )

def comentarios(request):
    
    context = {
        'text' : 'ESTAMOS NO COMENTARIOS'
    }
    
    return render(
        request,
        'blog/comentarios.html',
        context=context
    )
