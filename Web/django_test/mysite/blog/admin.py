from django.contrib import admin


# Register your models here.
from . import models


admin.site.register(models.BlogPost)        # 注册模型
