from django.shortcuts import render

# Create your views here.

def home(request):
    
    context = {
        'text' : 'ESTAMOS NA HOME',
        'title' : 'Home',
    }
    
    return render(
        request,
        'home/index.html',
        context=context
    )
    