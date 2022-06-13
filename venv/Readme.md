venv虚拟环境
1.新建虚拟环境：在项目目录下执行： python -m venv venv	（在当前目录下创建venv文件夹并在其中生成虚拟环境）。
2.激活/进入环境：进入venv/Script/路径下，activate.bat(激活)/deactivate.bat(退出)，linux下需进入bin/路径下，使用 source activate 激活，直接输入 deactivate 命令退出虚拟环境。
3.包安装：进入venv虚拟环境后，直接使用pip安装相关依赖包，linux下需要使用pip2/pip3区分下载包版本。
4.生成requirements：使用 pip freeze > requirements.txt 命令，将venv环境中所有的依赖包输出至当前路径下文本
5.在其他环境使用requirements包安装：pip install -r  requirements.txt