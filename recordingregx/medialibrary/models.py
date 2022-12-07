from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid # Required for unique instance

from taggit.managers import TaggableManager
# Create your models here.

class Media(models.Model):
    # must
    title = models.CharField(max_length=250)
    date_uploaded = models.DateTimeField(default=timezone.now)
    date_recorded = models.DateTimeField(default=timezone.now)
    author  = models.ForeignKey(User, on_delete=models.RESTRICT)
    descripttion = models.TextField(max_length=1000)

    sw_version = models.CharField(max_length = 15)

    id = models.UUIDField(primary_key=True, editable =False, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    
    # https://dev.to/thepylot/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
    # instruction how to create tags
    #tags = TaggableManager(blank=True)
    
    
    path_to_media = models.TextField(editable=True)
    
    # add a line of the change done by user and date
    # format example
    # <10.12.2022> [alexej]     updated Title: "makaka" to "chimpansee"      
    # <10.12.2022> [alexej]     updated SwVersion: "1.0.1" to "2.1.0"        
    # <10.12.2022> [sebastian]  updated Description: "Can't be displayed"    
    history_log = models.TextField()

    
    # additionally fields for metadata can be added lader depended on needs



    class Meta:
        ordering = ['date_recorded']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('media-detail', args=[str(self.id)])
        #pass

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} (sw_version.: {self.sw_version})'