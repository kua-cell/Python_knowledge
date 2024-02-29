import socket


def client():
    host = 'localhost'
    port = 443

    try:
        # 创建套接字并连接服务器
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print('成功连接到服务器')

            # 发送数据
            message = 'Hello, server!'
            s.sendall(message.encode())

            # 接收响应并打印
            data = s.recv(1024).decode()
            print('从服务器接收到的数据:', data)

    except ConnectionRefusedError:
        print('连接被拒绝，请确认服务器是否运行和地址端口是否正确')


if __name__ == '__main__':
    client()
