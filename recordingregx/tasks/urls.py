from django.urls import path
# from .views import TasksView
from . import views

# urlpatterns =[
#     path('', TasksView.as_view(http_method_names=['get'])),
#     path('/<int:id>/', TasksView.as_view(http_method_names=['get'])),
#     path('/store', TasksView.as_view(http_method_names=['post'])),
#     path('/update/<int:id>', TasksView.as_view(http_method_names=['put'])),
#     path('/delete/<int:id>', TasksView.as_view(http_method_names=['delete'])),
# ]

# namespace
app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('/store', views.TaskCreateView.as_view(), name='task_create'),
    path('/update/<int:pk>', views.TaskUpdateView.as_view(), name='task_update'),
    path('/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete'),
]