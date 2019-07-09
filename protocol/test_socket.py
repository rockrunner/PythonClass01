import socket, time

# Python实现UDP或TCP通信，总共分三步：
# 1. 建议连接：指定IP和端口
# 2. 发送数据。
# 3. 关闭连接：

# 默认情况下，socket()指定构造参数，则使用TCP协议建立连接
# s = socket.socket()
# s.connect(('192.168.49.128', 554))
# s.send('你好蜗牛学院'.encode('GBK'))
# s.close()


# 使用Python+UDP协议完成与飞秋的通信
for i in range(1000):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.connect(('192.168.49.128', 2425))
    packetId = str(time.time())
    name = "Qiang"
    host = "MyHostName"
    command = str(0x00000020)
    content = "This is the 消息 from Python.";
    message = "1.0:" + packetId + ":" + name + ":" + host +\
              ":" + command + ":" + content
    s.send(message.encode('GBK'))
    s.close()