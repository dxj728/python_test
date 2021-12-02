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
    4.2 manage.py makegration 执行命令，让django知道我们的模型有所变更
    备注，此步骤可能提示需要安装mysql客户端
            pip install mysql-python
         或 pip install PyMySQL(此库需要在settings.py所在目录下_init_.py中增加导入语句: import pymysql \ pymysql.install_as_MySQLdb())
