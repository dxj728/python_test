venv虚拟环境：
学习参考链接：https://zhuanlan.zhihu.com/p/640957757

venv 文件夹内容：
    Lib / site-packages文件夹：pip安装的依赖项
    Scripts文件夹：包含python.exe，pip.exe，以及激活文件（activate）、退出激活文件（deactivate）等脚本
    pyvenv.cfg：通过该文件改变改变虚拟环境指向的base PATH环境
一、命令行安装方式
1.新建虚拟环境：在项目目录下执行： python -m venv venv	（在当前目录下创建venv文件夹并在其中生成虚拟环境）。
2.激活/进入环境：进入venv/Script/路径下，activate.bat(激活)/deactivate.bat(退出)，linux下需进入bin/路径下，使用 source activate 激活，直接输入 deactivate 命令退出虚拟环境。
3.包安装：进入venv虚拟环境后，直接使用pip安装相关依赖包，linux下需要使用pip2/pip3区分下载包版本。
4.生成requirements：使用 pip freeze > requirements.txt 命令，将venv环境中所有的依赖包输出至当前路径下文本
5.在其他环境使用requirements包安装：pip install -r  requirements.txt
二、使用pycharm新建
1.新建新项目时附建虚拟环境：New Project直接选定New environment using Virtualenv，并确定项目Location，点击创建，即可在新项目中使用venv
2.已有项目切换已有虚拟环境：PyCharm>Preferences> Project :项目名称>Python Interpreter >向下箭头>Show ALL，即可在此选择其他项目的venv应用
3.已有项目创建新建虚拟环境：Pycharm->Preferences->Python Interpreter ->add