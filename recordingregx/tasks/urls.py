from django.urls import path
from .views import TasksView

urlpatterns =[
    path('', TasksView.as_view(http_method_names=['get'])),
    path('/<int:id>/', TasksView.as_view(http_method_names=['get'])),
    path('/store', TasksView.as_view(http_method_names=['post'])),
    path('/update/<int:id>', TasksView.as_view(http_method_names=['put'])),
    path('/delete/<int:id>', TasksView.as_view(http_method_names=['delete'])),
]
