from django.shortcuts import render
from .models import Media
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

#@login_required #make available for everybody
def overview(request):
    
    context = {
    'media_objects': Media.objects.all() # return all media 
    }
    return render(request, 'medialibrary/overview.html', context)


@login_required
def new_media(request):
    # return HttpResponse('<h1> Blog Home </h1>')
    #return render(request, 'blog/home.html')

    context = {
        'media_objects': Media.objects.all()
        #'devices': Media.objects.filter(user=request.user) 
    }
    return render(request, 'medialibrary/new_media.html', context) # lets access this data in the tamplate (post variable is availabe there)

def media_detailed_view(request, primary_key):
    try :
        med = Media.objects.get(primary_key)
    except Media.DoesNotExist:
        raise Http404("Media does not exist")
    return render(request, 'medialibrary/detailed_view.html', context={'media': med})


from django.views import generic

class MediaListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Media
    paginate_by = 10


class MediaDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Media