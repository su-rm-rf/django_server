# 安装
pip install django==4.1

# 三步曲
创建项目
> django-admin startproject django_server

创建应用
> python manage.py startapp todo_server

运行
> python manage.py runserver 8801

# 组织结构
```
django_server         --- 容器
  django_server       --- 全局项目
    settings.py       --- 项目配置
    urls.py           --- 项目路由配置
  todo_server         --- 单个应用
    controller        --- 控制器
    admin.py          --- 注册模型
    apps.py           --- 应用入口
    models.py         --- 创建模型
    tests.py
    urls.py           --- 应用路由配置
  manage.py           --- 管理项目
```