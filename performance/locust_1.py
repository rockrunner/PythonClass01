from locust import HttpLocust, TaskSet, task
import time, random, re

class UserBehavior(TaskSet):
    @task
    def test_login(self):
        self.users = ['pyuser_1', 'pyuser_2', 'pyuser_3', 'pyuser_4', 'pyuser_5', 'pyuser_6', 'pyuser_7', 'pyuser_8',
                      'pyuser_9', 'pyuser_10']
        username = random.sample(self.users, 1)[0]
        data = {'forward': '', 'jumpurl': 'http://localhost/phpwind/index.php', 'step': '2', 'lgt': '0',
                'pwuser': username, 'pwpwd': '123456', 'hideid': '0', 'cktime': '31536000'}
        resp = self.client.post(url='/phpwind/login.php', data=data, catch_response=True)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            resp.success()      # 告诉Locust运行器，本次请求成功
        else:
            resp.failure('登录失败.')


        resp = self.client.get('/phpwind/')
        resp.encoding = 'utf-8'
        pattern = 'quit&verify=(.+?)">'
        verify = re.findall(pattern, resp.text)[0]

        self.client.get('/phpwind/login.php?action=quit&verify=%s' % verify)


class WebSite(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
