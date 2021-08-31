# --coding:utf-8--
# File: pyvisa_mod.py
# Author: dxj728
# Time: 2021年09月01日00时
# 说明：pyvisa库学习

# python下pyvisa官方文档: https://pyvisa.readthedocs.io/en/latest/
# PyVisa教程1: https://blog.csdn.net/hao050523/article/details/100167510
# PyVisa教程2: https://blog.csdn.net/hao050523/article/details/100398999
# PyVisa教程3: https://blog.csdn.net/hao050523/article/details/100401355
# pyvisa简明介绍和教程一: https://zhuanlan.zhihu.com/p/357335933
# pyvisa简明介绍和教程二: https://zhuanlan.zhihu.com/p/357337164

# PyVisa是用来控制各种各样的测量仪器的Python包，适用诸如GPIB、RS232、USB、Ethernet等接口。可以自由的运行在Windows，Linux和Mac上，适用于不同仪器厂家（如National Instruments，Agilent，Tektronix，Standard Research Systems）的仪器
# PyVisa是VSIA库的一种前端实现，可运行在Python 2.7或Python 3.4以上版本。可以通过pip命令安装
# PyVisa包含了封装NI-Visa库（http://ni.com/visa/）的后端。因此，需要下载安装NI-Visa（见NI-Visa安装）。有来自不同公司或组织的不同Visa实现，

import visa

#这个例程显示了PyVisa的两个目标，精简化，面向对象方法。输入visa模块之后，创建了ResourceManager对象。如果没有指定，PyVisa将使用默认的后台（NI-Visa）。
rm = visa.ResourceManager()
print(rm.list_resources())
# ('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')

# 配置好ResourceManager之后，可以通过list_resource方法列出可用的资源，输出为VISA资源名称的元组，可以采用规律性的语法筛选所需的仪器。list_resources()描述了详细的语法，默认值为”?*::INSTR“，意为默认名称以”::INSTR“结尾的仪器（特定情况下，USB RAW和TCPIP SOCKET资源不会列出）。本例中，有一GPIB仪器编号为14，可以通过ResourceManager的open “GPIB0::14::INSTR”方法获取控制权，该对象命名为my_instrument。注意，open_resource返回了GPIBInstrument类实例。
inst = rm.open_resource('GPIB0::12::INSTR')
# 通过”\*IDN?“查询该资源信息，这是一标准的GPIO信息”你是谁？“
# 可能要以ASCII或者str的形式返回，后续根据实际的调试情况可自行处理。
ret = inst.query("*IDN?")
print(ret)
# 通过write发送命令， write里面的命令，一般在仪器自己的编译手册中，一般需要到仪器的program里面去找
inst.write("")

