from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Todo3

def index(request):
  # return HttpResponse('Hello Python')

  # todo_list = Todo3.objects.order_by('-id')[:2]
  todo_list = Todo3.objects.order_by('id')
  
  # output = ', '.join(todo.text for todo in todo_list)
  # return HttpResponse(output)

  # template = loader.get_template('todo_server/index.html')
  # context = {
  #   'todo_list': todo_list
  # }
  # return HttpResponse(template.render(context, request))

  context = {
    'todo_list': todo_list
  }
  return render(request, 'todo_server/index.html', context)

def detail(request, todo_id):
  # try:
  #   todo = Todo3.objects.get(pk=todo_id)
  #   context = {
  #     'todo': todo
  #   }
  # except Todo3.DoesNotExist:
  #   raise Http404('todo not found')
  # return render(request, 'todo_server/detail.html', context)
  todo = get_object_or_404(Todo3, pk=todo_id)
  context = {
    'todo': todo
  }
  return render(request, 'todo_server/detail.html', context)