编码：uft-8
作者：dxj728
说明：pyinstall模块打包练习文档

1. 安装pyinstaller模块

    python默认不包含pyinstaller模块，需要自行安装，含较多依赖，推荐使用pip安装，

    命令： pip install pyinstaller

    成功安装后，将在python\script\目录下增加一个pyinstaller.exe程序文件，后续将使用该程序进行打包


2. 生成可执行程序

    命令： pyinstaller 选项 源文件

    选项：
        -F, --onefile: 产生单个的可执行文件
        -D, --onedir: 产生一个目录（内含多个文件）作为可执行程序

        -w, --windowed, --noconsole: 指定程序运行是不显示命令行窗口（仅对windows有效）
        -c, --nowindowed, --console: 指定使用命令行窗口运行程序（仅对windows有效）

        -a, --ascii: 不包含Unicode字符集支持
        -d, --debug: 产生debug版本的可执行文件
        -o DIR, --out=DIR: 指定spec文件的生成目录，如果没有指定，则默认使用当前目录来生成spec文件
        -p DIR, --path=DIR: 设置python导入模块的路径（和设置环境变量的作用相似），也可以使用路径分隔符（windows使用分号，linux使用冒号）来分隔多个路径
        -n NAME, --name=NAME: 指定项目（产生的spec）名字，如果省略该选项，那么第一个脚本的主文件名将作为spec的名字
        -h, --help: 用于显示pyinstaller模块的帮助信息

    示例： pyinstaller -F -w app.py

    结果：将在cmd当前命令所在路径下生成dist目录（内含exe可执行程序）、build目录、app.spec文件等, 完成后可删除。
        -D选项：含上述外，将在dist目录中生成大量文件及exe可执行程序
