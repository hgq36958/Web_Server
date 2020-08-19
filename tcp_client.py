from socket import *

#  服务端地址
ADDR = ("127.0.0.1",8888)

# 默认值就是创建tcp套接字
tcp_socket = socket()

# 发起链接 对应 accept
tcp_socket.connect(ADDR)

# 发送接受消息
while True:
    msg = input("请输入：")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("服务端信息:",data.decode())

# 关闭
tcp_socket.close()