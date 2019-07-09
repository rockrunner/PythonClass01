import requests

# resp = requests.get('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather?theCityCode=上海&theUserID=')
# resp.encoding = 'utf-8'
# print(resp.text)

# data = {'theCityCode':'成都', 'theUserID':''}
# resp = requests.post('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather', data=data)
# print(resp.text)


# from suds.client import Client
#
# wsdl = "http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl"
# client = Client(wsdl)
# resp = client.service.getMobileCodeInfo('13812345678')
# print(resp)



# from suds.client import Client
#
# wsdl = "http://ws.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl"
# client = Client(wsdl)
# resp = client.service.getCountryCityByIp("121.40.123.1")
# print("该IP地址的所在地为：" + str(resp))
# print("该IP地址的所在地为：" + resp[0][1])



# from suds.client import Client
#
# wsdl = "http://127.0.0.1:8899/ws/MyWebService?WSDL"
# client = Client(wsdl)
# # resp = client.service.readFromFile('D:/Test.txt')
# resp = client.service.writeToFile('D:/Test2.txt', 'Hello Python.')
# print(resp)
