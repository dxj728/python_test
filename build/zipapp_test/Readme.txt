编码：uft-8
作者：dxj728
说明：zipapp模块学习

1.简单打包使用说明

    语法： python -m zipapp source [options]

            python -m zipapp: 代表python指定使用zipapp模块
            source: 代表打包的python源程序或目录，可以是单个的python文件或者文件夹，文件夹时打包该文件夹中所有的python文件
            -o, --output=: 该选项指定输出档案包的文件名。如果不指定该选项，所生成的档案包文件默认为source参数值，并加上.pyz后缀
            -p, --python=: 用于指定python解释器
            -m, --main=: 用于指定python的入口函数，选项为pkg.mod:fn的形式，其中pkg.mod是档案包中的包或模块，fn是指定模块中的函数，如果不指定该项，则默认为模块中的__main__.py开始执行
            -c, --compress: 无值，python3.7后支持选项，用于指定是否对档案包进行压缩来减少大小，默认不压缩
            --info: 用于在诊断时西安市档案包中的解释器
            -h, --help: 用于显示zipapp模块的帮助信息

    示例： python -m zipapp D:\git\python_test\build\zipapp_test -m "app:main"

    结果： 在D:\git\python_test\build目录下生成zipapp_test.pyz文件

    使用： 在cmd中执行python zipapp_test.pyz命令，将会输出相关执行结果


2.独立打包使用说明（自带依赖库）

    首先： python -m pip install -r D:\git\python_test\build\zipapp_test\pack_require.txt --target D:\git\python_test\build\zipapp_test\pack

            python -m pip install: 使用自带pip模块开安装依赖模块
            -r参数：选项支持两个值    a.直接指定要安装的模块或包
                                    b.使用清单文件指定要安装的模块和包，文件内每行定义一个模块
            --target参数：指定将模块安装到指定目录下

    打包：python -m zipapp D:\git\python_test\build\zipapp_test\pack

    备注：
        a.在pip安装完成后，建议删除指定目录下.dist-info结尾的目录
        b.如果打包目录中含有__main__.py文件， 则不需要指定-m选项及入口函数