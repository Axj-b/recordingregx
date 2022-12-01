from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse
'''
posts = [
    {'author': 'Corey Blue',
     'title': 'Blog post 1',
     'content': 'bla bla blub',
     'date_posted': 'August 27, 2020'
     },
    {'author': 'Jane Blue',
     'title': 'Blog post 2',
     'content': 'bla bla second post ever',
     'date_posted': 'August 30, 2020'
     }
]
''' #not used anymore
# Create your views here.


def home(request):
    # return HttpResponse('<h1> Blog Home </h1>')
    #return render(request, 'blog/home.html')
    context ={}
    all_objects =Post.objects.all()
    if len(all_objects) > 0:

        context = {
            'posts': all_objects
        }
    return render(request, 'blog/home.html', context) # lets access this data in the tamplate (post variable is availabe there)


def about(request):
    # return HttpResponse('<h1> About </h1>')
    return render(request, 'blog/about.html', {'title':'about'})
