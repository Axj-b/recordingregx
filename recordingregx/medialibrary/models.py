from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.


class Media(models.Model):
    # must
    title = models.CharField(max_length=250)
    date_uploaded = models.DateTimeField(default=timezone.now)
    date_recorded = models.DateTimeField(default=timezone.now)
    author  = models.ForeignKey(User, on_delete=models.RESTRICT)
    descripttion = models.TextField()
    
    # https://dev.to/thepylot/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
    # instruction how to create tags
    tags = TaggableManager()
    
    
    path_to_media = models.SlugField(editable=True, unique=True)
    
    # add a line of the change done by user and date
    # format example
    # <10.12.2022> [alexej]     updated Title: "makaka" to "chimpansee"      
    # <10.12.2022> [alexej]     updated SwVersion: "1.0.1" to "2.1.0"        
    # <10.12.2022> [sebastian]  updated Description: "Can't be displayed"    
    history_log = models.TextField()