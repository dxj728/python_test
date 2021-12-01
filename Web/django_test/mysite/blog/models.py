
'''models.py 数据模型
'''

from django.db import models

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateField()




