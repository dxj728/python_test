编码：uft-8
作者：dxj728
说明：django基本概念、项目(project)、应用(app)的学习

当前如无特别说明，均认为在windows环境下操作
1. pip install django 安装django模块，安装完成后，Script文件夹下会出现一个django-admin.py的工具，用以简化任务，创建项目目录
2. django-admin.py startproject mysite 执行命令，创建名称为mysite的项目(project)。内包含urls.py, settings.py, manage.py等多个文件
    2.1. windows下，使用"python manage.py runserver"命令可以直接运行开发服务器，但不建议将开发服务器部署至公开界面
3. manage.py startapp blog 执行命令，创建名称为blog的应用。内包含model.py, views.py, test.py等多个文件
