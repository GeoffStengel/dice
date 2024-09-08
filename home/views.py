from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Jerry Garcia',
        'title': 'Blog Post',
        'content': 'Long Strange Trip',
        'date_posted': 'July 3, 1978'
    },
        {
        'author': 'Bobby Weir',
        'title': 'Blog Post 2',
        'content': 'Long Strange Trip',
        'date_posted': 'May 20, 1995'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/index.html', context)
 
def contact(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/contact.html', context)

def example(request):
    return HttpResponse('<h1>Example Page<h1/>')