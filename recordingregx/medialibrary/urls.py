from django.urls import path
from . import views

urlpatterns = [
 
    path('overview/', views.MediaListView.as_view(), name='media_list'), 
    path('new_media/', views.new_media, name='media-new'),  
    #path('media/<int>',views.media_detailed_view,  name='media-detail'), 
    path('media/<int:pk>', views.MediaDetailView.as_view(), name='media-detail'), 
    

]
