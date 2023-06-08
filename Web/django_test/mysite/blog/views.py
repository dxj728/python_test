
'''views.py 视图函数(即MVC中的控制器)
'''

from django.shortcuts import render
from django.http import HttpResponse

import blog.views

from .models import BlogPost
from django.core.paginator import Paginator


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
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print("page param:", page)
    all_article = BlogPost.objects.all()
    top5_article_list = BlogPost.objects.order_by('-publish_date')[:5]

    paginator = Paginator(all_article, 1)
    page_num = paginator.num_pages
    print('page num:', page_num)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request, "blog/index.html",
                  {
                      'article_list': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_page': previous_page,
                      'top5_article_list': top5_article_list
                  }
                  )


def get_detail_page(request, article_id):
    all_article = BlogPost.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):

        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1

        if len(all_article) == 1:
            previous_index = next_index = index

        if article.id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    # curr_article = BlogPost.objects.all()[0]
    section_list = curr_article.content.split('\n')
    return render(request, "blog/detail.html",
                  {
                      'curr_article': curr_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article
                  }
                  )

