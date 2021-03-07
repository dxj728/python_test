# --coding:utf-8--
# File: network_test.py
# Author: dxj728
# Time: 2021年02月19日00时
# 说明：网络编程学习


"""OSI七层模型：一个试图使各种计算机在世界范围内互连为网络的标准框架
    应用层(Application Layer)：为应用程序提供服务，HTTP、FTP、SSH、SMTP、POP3
    表示层(Presentation Layer)：数据格式转化、数据加密
    会话层(Session Layer)：建立、管理和维护会话
    传输层(Transport Layer)：建立、管理和维护端到端的连接，TCP(传输控制协议)、UDP(用户数据报协议)
    网络层(Network Layer)：IP选址及路由选择，路由器，IP(网际协议)、ICMP
    数据链路层(Datalink Layer)：提供介质访问和链路管理，网桥，交换机，网卡等，ARP、RARP、PPP
    物理层(Physical Layer)：物理层，网线，集线器、中继器等
TCP/IP五层模型
    应用层、表示层、会话层————>应用层
"""


"""TCP三次握手与四次挥手
标志位介绍：SYN(发起一个新连接)、FIN(释放一个连接)、URG(紧急指针有效)、ACK(确认序号有效)、PSH(接收方应尽快将报文交给应用层)、RST(重置链接)
三次握手(TCP连接建立)
    0.客户端主动结束CLOSE状态，服务器端处于LISTEN状态
    1.客户端主动发送一段TCP报文，其中标志位SYN(发起一个新连接)，序号seq=X(默认为1)，发送后客户端进入SYN-SENT状态
    2.服务端接收到报文后，结束LISTEN阶段，后返回给客户端一段TCP报文，其中标志位SYN和ACK(确认客户端报文seq有效，服务端可以正常接收，同意创建新连接)，发送后服务端进入SYN-SENT状态
    3.客户端收到服务端的报文后，结束SYN-SENT状态，返回最后一段报文，其中标志位ACK(确认收到服务器端同意连接的信号)，发送后客户端进入ESTABLISHED状态


    服务端收到客户端报文后，结束SYN-SENT状态，也进入ESTABLISHED状态
四次挥手(TCP连接释放)
    0.客户端主动结束ESTABLISHED状态
    1.客户端主动发送一段TCP报文，其中标志位FIN(释放一个连接)，序列号seq=U，发送后客户端进入FIN-WAIT-1状态(半关闭状态，客户端不再向服务器端发送数据)
    2.服务器端接收到客户端释放连接报文后，结束ESTABLISHED状态，进入到CLOSE-WAIT状态(半关闭状态)，并返回一段TCP报文，其中标志位ACK(确认收到释放请求)，序号seq=V，随后服务器端开始准备释放客户端上的链接
      客户端收到服务器的TCP报文后，结束FIN-WAIT-1状态，进入FIN-WAIT-2状态，等待数据传输完毕。
    3.服务器等数据传输完毕后，再次向客户端发出一段TCP报文，其中：标记位为FIN和ACK(已准备好释放链接)，随后服务器端结束CLOSE-WAIT状态，进入LAST-ACK状态，并停止服务器端发送数据，但仍可接收客户端数据
    4.客户端收到服务器端TCP报文，确认服务器端已做好释放链接的准备，结束FIN-WAIT-2状态，并向服务器端发送一段报文，其中标志位为ACK(接收到服务器准备好释放链接的信号)，发送后进入TIME-WAIT状态，等待2MSL后进入CLOSE状态
      服务端收到客户端发出的TCP报文后结束LAST-ACK状态，进入CLOSE状态
备注：
    四次挥手第3步中，客户端等待2个MSL(TCP报文传输过程中最大生命周期)的原因
        服务器发送FIN报文后，在1MSL内没有收到客户端发出ACK报文的话，服务器端会再次向客户端发出FIN报文。
        故客户端在2MSL内再次收到服务器端的FIN报文，则说明服务器未能接收到客户端发出的ACK报文。则需再次发送ACK报文并重新计时2MSL。
"""

"""socket编程
    s = socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
        family参数: 指定网络类型，支持常量为AF_UNIX(UNIX网络)/AF_INET(基于IPV4的网络)/AF_INET6(基于IPV6的网络)
        type参数: 指定网络sock类型，支持选项为SOCK_STREAM(默认值，创建基于TCP协议的socket)/SOCK_DGRAM(创建基于UDP协议的socket)/SOCK_RAM(创建原始socket)
        prono参数：指定协议号，无特殊要求则该值默认为0，并可以忽略
    socket对象s提供的方法：
        1. s.accept(): 接收来自客户端socket的连接，常作为服务端socket使用
        2. s.bind(address): 作为服务端使用的socket调用该方法，将socket绑定到指定address，address可作为元组包含IP地址和端口
        3. s.close(): 关闭连接，回收资源
        4. s.connect(address): 作为客户端使用的socket调用该方法连接服务端
    

"""
