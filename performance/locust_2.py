from locust import HttpLocust, TaskSet, task
import time, random, re

class UserBehavior(TaskSet):
    # 初始化方法 on_start()，用于不重复运行的代码，不能被@task修饰
    def on_start(self):
        self.users = ['pyuser_1', 'pyuser_2', 'pyuser_3', 'pyuser_4', 'pyuser_5', 'pyuser_6', 'pyuser_7', 'pyuser_8',
                      'pyuser_9', 'pyuser_10']
        username = random.sample(self.users, 1)[0]
        data = {'forward': '', 'jumpurl': 'http://localhost/phpwind/index.php', 'step': '2', 'lgt': '0',
                'pwuser': username, 'pwpwd': '123456', 'hideid': '0', 'cktime': '31536000'}
        resp = self.client.post(url='/phpwind/login.php', data=data, catch_response=True)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            resp.success()  # 告诉Locust运行器，本次请求成功
        else:
            resp.failure('登录失败.')

    @task
    def test_post(self):
        # 方案二：直接从首页的响应中读取一条fid
        resp = self.client.get('/phpwind/')
        resp.encoding = 'utf-8'
        # pattern = r'thread.php\?fid=(.*)" target="_blank'
        pattern = r'thread.php\?fid=(.+?)" target="_blank'  # 非贪婪模式
        result = re.findall(pattern, resp.text)
        fid = random.sample(result, 1)[0]

        resp = self.client.get('/phpwind/post.php?fid=%s' % fid)
        resp.encoding = 'utf-8'
        pattern = 'verify" value="(.*)" />'
        result = re.findall(pattern, resp.text)

        # 验证码存在的位置：通常情况下，哪个页面发起了该请求（该请求的referer字段），则验证码很有可能存在于该页面中。
        sequence = random.randrange(10000000, 99999999)
        data = {'magicname': '', 'magicid': '', 'verify': result[0], 'atc_title': '这是一个Python帖子标题-%d' % sequence,
                'atc_iconid': 0,
                'atc_content': '这是一个Python帖子内容-%d' % sequence, 'atc_autourl': 1, 'atc_usesign': 1, 'atc_convert': 1,
                'atc_rvrc': 0,
                'atc_enhidetype': 'rvrc', 'atc_money': 0, 'atc_credittype': 'money', 'atc_desc1': '', 'att_special1': 0,
                'att_ctype1': 'money', 'atc_needrvrc1': 0, 'step': 2, 'pid': '', 'action': 'new', 'fid': fid, 'tid': '',
                'article': 0, 'special': 0, }
        resp = self.client.post('/phpwind/post.php?', data=data, catch_response=True)
        resp.encoding = 'utf-8'
        if '发帖完毕点击进入主题列表' in resp.text:
            resp.success()
        else:
            resp.failure('发帖失败.')


class WebSite(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
