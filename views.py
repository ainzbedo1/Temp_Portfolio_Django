from django.shortcuts import render
from django.http import HttpResponse
from .models import main
# Create your views here.

def index(request):
    posts = main.objects.all()[:10]
    context = {
        'comment': 'test body block',
        'posts': posts
    }
    #return HttpResponse('Test Main Portfolio_Django')
    return render(request, 'main/index.html', context)

def details(request, id):
    post = main.objects.get(id=id)

    context = {
        'post': post
    }
    
    return render(request, 'main/details.html', context)