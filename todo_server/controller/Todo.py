from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse

import json
from django.core import serializers

from ..models import Todo3

# 列表
def list(request):
  completed = request.GET.get('completed')
  data = ''
  if completed != None and completed != '':
    data = Todo3.objects.filter(completed=completed).order_by('id')
  else:
    data = Todo3.objects.all().order_by('id')

  todo_list = serializers.serialize('json', data)
  data2 = json.loads(todo_list)

  arr = []
  for todo in data2:
    fields = todo['fields']
    arr.append({
      'id': todo['pk'],
      'text': fields['text'],
      'completed': fields['completed'],
    })

  # response = JsonResponse({'data': arr}, safe=False, json_dumps_params={'ensure_ascii': False})
  response = HttpResponse(json.dumps({'data': arr}))
  return response

# 详情
def detail(request, todo_id):
  todo = get_object_or_404(Todo3, pk=todo_id)

  res = {
    'id': todo.id,
    'text': todo.text,
    'completed': todo.completed,
  }

  response = JsonResponse({'data': res}, safe=False, json_dumps_params={'ensure_ascii': False})
  return response

# 增加
def add(request):
  data = json.loads(request.body)

  # todo = Todo3(text=data.get('text'), completed=data.get('completed'))
  todo = Todo3()
  todo.text = data.get('text')
  todo.completed = data.get('completed')
  
  id = todo.save()
  response = JsonResponse({'data': id}, safe=False)
  return response

# 修改
def update(request):
  # data = json.loads(request.body.decode())
  # todo = Todo3.objects.filter(pk=data['id'])[0]
  data = json.loads(request.body)
  todo = Todo3.objects.filter(pk=data.get('id'))[0]

  if 'text' in data:
    todo.text = data['text']
  if 'completed' in data:
    todo.completed = data['completed']
    
  res = todo.save()

  response = JsonResponse({'data': res}, safe=False)
  return response

# 删除
def delete(request):
  data = json.loads(request.body)
  todo = Todo3.objects.filter(pk=data.get('id'))[0]

  res = todo.delete()

  response = JsonResponse({'data': res[0]}, safe=False)
  return response

# 清空
def clear(request):
  res = Todo3.objects.all().delete()

  response = JsonResponse({'data': res[0]}, safe=False)
  return response