import requests

session = requests.session()
data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
session.post('https://localhost:8443/woniusales/user/login', data=data, verify='D:/localhost.crt')

data = {'customername':'HTTPS','customerphone':'13843561237','childsex':'男',
        'childdate':'2017-12-10','creditkids':'200','creditcloth':'150'}
resp = session.post(url='https://localhost:8443/woniusales/customer/add', data=data, verify=False)
print(resp.text)

# verify参数取值：False 忽略证书,  指定证书路径

