
'''models.py 数据模型
    更多支持字段类型详见官方文档： http://docs.djangoproject.com/en/dev/ref/models/fields/#field-types
'''

from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)    # 使用CharField类型(可用于较短的单行文本)作为博文的title，并限制该字段的最大长度
    body = models.TextField()       # TextField类型适用于较长的文本，如正文
    timestamp = models.DateTimeField()      # 时间戳使用DateTimeField类型，本质上为python的datatime.datetime对象
    




