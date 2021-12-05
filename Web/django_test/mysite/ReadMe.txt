编码：uft-8
作者：dxj728
说明：django基本概念、项目(project)、应用(app)的学习

python .\manage.py runserver ：直接运行开发服务器，访问链接: http://localhost:8000

当前如无特别说明，均认为在windows环境下操作, py文件执行命令前默认有python解释器
1. pip install django 安装django模块，安装完成后，Script文件夹下会出现一个django-admin.py的工具，用以简化任务，创建项目目录
2. django-admin.py startproject mysite 执行命令，创建名称为mysite的项目(project)。内包含urls.py, settings.py, manage.py等多个文件
    2.1. windows下，使用"python manage.py runserver"命令可以直接运行开发服务器，但不建议将开发服务器部署至公开界面
3. manage.py startapp blog 执行命令，创建名称为blog的应用。内包含model.py, views.py, test.py等多个文件
4. 在项目文件夹下的settings.py文件中找到DATABASES配置项，填充对应的数据库连接字段
    4.1 manage.py migrate 执行命令，创建表结构
    4.2 manage.py makemigrations 执行命令，让django知道我们的模型有所变更
    备注，此步骤可能提示需要安装mysql客户端
            pip install mysql-python
         或 pip install PyMySQL(此库需要在settings.py所在目录下_init_.py中增加导入语句: import pymysql \ pymysql.install_as_MySQLdb())
5. manage.py createsuperuser 执行该命令创建超级用户，需要输入username, E-mail, password(again)等信息
6. manage.py shell 执行该命令启动django shell, 通过此巩固，可以实例化模型，并与应用交互，这些任务在WEB应用开发中不易完成
    4.1 from blog.models import BlogPost 执行该命令在django shell中导入BlogPost模型
    4.2 BlogPost.objects.all() 执行该命令在django shell中查询数据库中的BlogPost实例个数，获取数据库中存储的所有BlogPost对象的列表
    4.3 bp = BlogPost(title="test cmd shell", body='''hello, world''', timestamp=datetime.now()) 在django shell中实例化对象
    4.4 bp.save() 在django shell中将其写入到数据库中
    4.5 BlogPost.objects.count() 在django shell中获取该对象实例总个数
    4.6 bp = BlogPost.objects.all()[0] 在django shell中获取含有所有BlogPost对象的列表中的第一个元素
    4.7 print(bp.title) 在django shell中输出该元素的属性
7.
