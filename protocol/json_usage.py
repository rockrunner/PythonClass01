import json, http.client


# 如何把一个字典字符串转换为一个字典对象
# dict_str = '{"childsex":"女","creditcloth":3065,"creditkids":500,"createtime":"2017-10-01 15:40:06","counts":8, ' \
#            '"totals":973,"userid":1,"childdate":"2015-12-31","customerphone":"18683645768","customerid":1,' \
#            '"credittotal":3565,"customername":"某人","updatetime":"2018-12-12 12:15:18"}'
#
# dict_obj = eval(dict_str)
# print(dict_obj['customerphone'])
#
# list_str = '[111, 222, 333, 444, 555, 666]'
# # print(type(eval(list_str)))
# print(list_str[4])
# list_obj = eval(list_str)
# print(list_obj[4])


conn = http.client.HTTPConnection(host='localhost', port=8088)
header = {'Content-Type': 'application/x-www-form-urlencoded'}
data = 'customerphone=&page=1'
conn.request(method='POST', url='/woniusales/customer/search', body=data, headers=header)
resp = conn.getresponse()
content = resp.read().decode()
# content_list = eval(content)        # 使用Python内置函数eval来进行类型的转换，进而将JSON字符串转换为Python的List和Dict
content_list = json.loads(content)    # 使用Python的json库中的loads函数来进行转换, 将JSON字符串转换为Python的List和Dict

for content_dict in content_list:
    print(content_dict['customerid'], content_dict['customerphone'])


my_list_obj = [111, 222, 333, 444, 555, 666]
print(type(my_list_obj))
my_list_str = json.dumps(my_list_obj)
print(type(my_list_str))
print(type(str(my_list_obj)))