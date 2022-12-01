from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

# @csrf_exempt
class TasksView(View):
    def get(self, request, id=None):
        return HttpResponse('GET request')
    
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # content = body['content']
        return HttpResponse('POST request\r\n {}'.format(body))

    def put(self, request, id):
        return HttpResponse('PUT request id: {}'.format(id))

    def delete(self, request, id):
        return HttpResponse('DELETE request')