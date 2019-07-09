# import random, time, os
#
# # print(random.randint(0, 5))
# # print(random.randrange(0, 5))
# #
# # print(int('1000')*25)
# #
# # print(time.strftime('%Y%m%d_%H%M%S'))
#
# # os.system('"C:\Program Files (x86)\Internet Explorer\iexplore.exe" http://192.168.1.128:8088/woniusales')
#
# # for i in range(100, 110):
# #     os.system('adb shell screencap -p /data/local/tmp/myscreen_%d.png' % i)
# #     os.system('adb pull /data/local/tmp/myscreen_%d.png d:/Other/myscreen_%d.png' % (i, i))
# #     time.sleep(2)
#
# # import http.client
# #
# # conn = http.client.HTTPConnection(host='localhost', port=8088)
# # conn.request(method='GET', url='/woniusales/')
# # resp = conn.getresponse()
# # print(resp.headers)
# # print(resp.read().decode())
# # conn.request(method='POST', url='', body='', headers='')
#
#
# import psutil, locust, time
#
# # for i in range(10):
# #     print(psutil.cpu_percent())
# #     print(psutil.cpu_times().user)
# #     print(psutil.virtual_memory().available)
# #     print(psutil.disk_usage('D:'))
# #     print(psutil.net_io_counters())
# #     time.sleep(3)
#
# from locust import HttpLocust, TaskSet, task
# class UserBehavior(TaskSet):
#     @task
#     def getIndex(self):
#         self.client.get('/')
#
# class WebSite(HttpLocust):
#     task_set = UserBehavior
#     min_wait = 3000
#     max_wait = 6000

#
# import time
# start_time = time.time() * 1000
# print(start_time)
# time.sleep(2.58)
# end_time = time.time() * 1000
# print(int(end_time-start_time))

import random
users = ['pyuser_1','pyuser_2','pyuser_3','pyuser_4','pyuser_5','pyuser_6']
print(random.sample(users, 1))