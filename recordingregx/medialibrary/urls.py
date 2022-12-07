from django.urls import path
from . import views

urlpatterns = [
 
    path('overview/', views.overview, name='medialibrary-overview'), 
    path('new_media/', views.new_media, name='media-new'), 
    

]
