from django.shortcuts import render
from .models import Media
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required #make available for everybody
def overview(request):

    context = {
    'devices': Media.objects.all() # return all media 
    }
    return render(request, 'medialibrary/overview.html', context)


@login_required
def new_device(request):
    # return HttpResponse('<h1> Blog Home </h1>')
    #return render(request, 'blog/home.html')

    context = {
        'media_objects': Media.objects.all()
        #'devices': Media.objects.filter(user=request.user) 
    }
    return render(request, 'medialibrary/new_media.html', context) # lets access this data in the tamplate (post variable is availabe there)