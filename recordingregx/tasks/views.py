from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import TaskForm
from .models import Task
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

# @csrf_exempt
# class TasksView(View):
#     def get(self, request, id=None):
#         # return HttpResponse('GET request')
#         # return render(request, "index.html") # add this line
#         form = TaskForm()
#         tasks = Task.objects.all() # add this
#         return render(request, "index.html", {"task_form": form, "tasks": tasks, "action_uri": "/tasks/store"})

    
#     def post(self, request):
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/tasks")
        
#         # body_unicode = request.body.decode('utf-8')
#         # body = json.loads(body_unicode)
#         # content = body['content']
#         # return HttpResponse('POST request\r\n {}'.format(body))

#     def put(self, request, id):
#         return HttpResponse('PUT request id: {}'.format(id))

#     def delete(self, request, id):
#         return HttpResponse('DELETE request')

class TaskListView(ListView):
    paginate_by = 2
    model = Task
    form = TaskForm
    context_object_name = 'tasks'
    template_name = "task_list.html"
    
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['action_uri'] = "/tasks/store"
        context['task_form'] = TaskForm()
        return context
    
    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        return self.request.GET.get('paginate_by', self.paginate_by)

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy('tasks:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy('tasks:task_list')
