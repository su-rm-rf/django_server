from django.urls import path

from .controller import Todo
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('list', Todo.list, name='list'),
  path('<int:todo_id>', Todo.detail, name='detail'),
  path('add', Todo.add, name='add'),
  path('update', Todo.update, name='update'),
  path('delete', Todo.delete, name='delete'),
  path('clear', Todo.clear, name='clear'),
]