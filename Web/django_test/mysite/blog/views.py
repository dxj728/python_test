
'''views.py 视图函数(即MVC中的控制器)
'''

from django.shortcuts import render
from django.http import HttpResponse

import blog.views

from .models import BlogPost

# Create your views here.

def hello_world(request):
    return HttpResponse("hello_world")


def article_content(request):
    article = BlogPost.objects.all()[0]
    article_id = article.id
    title = article.title
    brief_connect = article.brief
    content = article.content
    publish_time = article.publish_date
    ret_str = 'title: {} \r\n' \
              'brief:{} \r\n' \
              'content:{} \r\n' \
              'id:{} \r\n' \
              'time:{} '.format(title, brief_connect, content, article_id, publish_time)
    return HttpResponse(ret_str)


def get_index_page(request):
    all_article = BlogPost.objects.all()
    return render(request, "blog/index.html",
                  {
                      'article_list': all_article
                  }
                  )


