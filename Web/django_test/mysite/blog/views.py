
'''views.py 视图函数(即MVC中的控制器)
'''

from django.shortcuts import render
from django.http import HttpResponse

import blog.views

# Create your views here.

def hello_world(request):
    return HttpResponse("hello_world")