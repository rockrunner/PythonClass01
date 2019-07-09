import requests

# resp = requests.get('http://localhost:8088/woniusales')
# print(resp.text)

# 下载一张图片：读取二进制响应
# resp = requests.get('http://www.woniuxy.com/page/img/banner/PEBT%205.0-home.jpg')
# with open("d:/myimage.jpg", mode='wb') as file:
#     file.write(resp.content)

# 用字典为构造POST请求的正文
# data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
# resp = requests.post('http://localhost:8088/woniusales/user/login', data=data)
# print(resp.text)


# 利用requests完成woniusales的会员新增
# data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
# resp = requests.post('http://localhost:8088/woniusales/user/login', data=data)
# cookie = resp.cookies
#
# data = {'customername':'接口测试','customerphone':'13843562345','childsex':'男',
#         'childdate':'2017-12-10','creditkids':'200','creditcloth':'150'}
# resp = requests.post(url='http://localhost:8088/woniusales/customer/add', data=data, cookies=cookie)
# print(resp.text)


# 利用session对象直接发请求，节省维护cookie的代码
# session = requests.session()
# data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
# session.post('http://localhost:8088/woniusales/user/login', data=data)
#
# data = {'customername':'接口测试','customerphone':'13843562346','childsex':'男',
#         'childdate':'2017-12-10','creditkids':'200','creditcloth':'150'}
# resp = session.post(url='http://localhost:8088/woniusales/customer/add', data=data)
# print(resp.text)


# 利用requests库进行文件上传
# session = requests.session()
# data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
# session.post('http://localhost:8088/woniusales/user/login', data=data)

# 文件上传
# data = {'batchname': 'GB20181121'}
# # file = {'batchfile': open('D:/Other/SaleList-20171020-Test.xls', mode='rb')}
# # 如果文件名是中文：一，直接修改中文名为英文名，二，给文件指定一个英文别名，供上传使用.
# file = {'batchfile': ('SaleList-1.xls', open('D:/Other/销售出库单-20171020-Test.xls', mode='rb'))}
# resp = session.post(url='http://localhost:8088/woniusales/goods/upload', data=data, files=file)
# print(resp.text)


# PostMan，SoapUI，Fiddler, Fiddler监控APP，HTTPS协议, WebService（SOAP）,SMTP发邮件
# 综合练习：WoniuSales销售出库模块，批次管理模块，商品入库。