socket (简称 套接字)是进程之间通信一个工具，好现实生活中的插座,
所有的家用电器要想工作都是基于插座进行，进程之间想要进行网络通信需要socket。

Socket负责进程之间的网络数据传输,好比数据的搬运工。

客户端和服务端

2个进程之间通过Socket进行相互通讯，就必须有客户端和服务端

Socket服务端(被动的)：等待其他进程的链接、可接受发来的消息、可以恢复消息
Socket客户端(主动的)：主动连接服务端、发送消息、可以接受回复


Socket服务端编程
主要分为如下步骤：
1.创建socket对象
    import socket  # 导入python内置的Socket包
    socket_sever= socket.socket()

2.绑定socket_sever到指定IP和地址
    socket_sever.bind(host, port)

3.服务端开始监听端口
    socket_sever.listen(backlog)
    # backlog为int整数，表示允许的链接数量，产出的会等待，可以不填，不会自动设置一个合理值

4.接受客户端连接，获取连接对象
    conn,address = socket_sever.accept()
    print(f"客户端连接，连接来自：{adress}")
    # accept方法是阻塞方法，如果没有连接，会卡在这一行不向下执行代码
    # accept返回值是一个二元元组，可以使用上述形式，用两个变量接受二元元组的2个元素

5.客户端连接后，通过recv方法，接受客户端发送的消息
    while True:
        data = conn.recv(1024).decode("UTF-8")
        # recv方法的返回值是字节数组(Bytes),可以通过decode使用UTF-8解码为字符串
        # recv方法的传参是buffsize， 缓冲区大小，一般设置为1024即可
        if data == 'exit'
            break
        print("接受到发送来的数据："， data)

    # 可以通过while True无限循环来持续和客户进行数据交互
    # 可以通过判定客户端发来的特殊标记，如exit，来推出无限循环

6.通过conn(客户端当次连接对象)，调用send方法可以回复消息
    while True:
        data = conn.recv(1024).decode("UTF-8")
        if data == "exit":
            break
        print("接受到发送的数据:", data)


        conn.send("你好呀哈哈哈"， encode("UTF-8"))

7.conn(客户端当次连接对象)和socket_sever对象调用close方法，关闭连接