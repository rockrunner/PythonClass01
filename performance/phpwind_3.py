import requests, time, random, threading, pymysql, re

class PhpWindTest:
    def __init__(self):
        self.session = requests.session()
        self.conn = pymysql.connect('localhost', 'root', '', 'phpwind', charset='utf8')
        self.cursor = self.conn.cursor()

    # 执行update或insert的SQL语句
    def do_update(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    # 执行登录的测试
    def test_login(self):
        sequence = random.randint(1, 20)
        data = {'forward': '', 'jumpurl': 'http://localhost/phpwind/index.php', 'step': '2', 'lgt': '0',
                'pwuser': 'pyuser_%d' % sequence, 'pwpwd': '123456', 'hideid': '0', 'cktime': '31536000'}
        resp = self.session.post('http://localhost/phpwind/login.php?', data=data)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            self.do_update("update pass_fail_count set pass=pass+1 where type='login'")
        else:
            self.do_update("update pass_fail_count set fail=fail+1 where type='login'")

    # 对发帖和回帖进行封装
    def do_post(self, fid, tid='', action='new'):
        if action == 'new':
            type = 'post'
        else:
            type = 'reply'

        # 根据fid获取到对应页面的verify验证码
        resp = self.session.get('http://localhost/phpwind/post.php?fid=%s' % fid)
        resp.encoding = 'utf-8'
        pattern = 'verify" value="(.*)" />'
        result = re.findall(pattern, resp.text)

        # 实现发帖或回帖请求
        sequence = random.randrange(10000000, 99999999)
        data = {'magicname': '', 'magicid': '', 'verify': result[0], 'atc_title': '这是一个Python帖子标题-%d' % sequence,
                'atc_iconid': 0,
                'atc_content': '这是一个Python帖子内容-%d' % sequence, 'atc_autourl': 1, 'atc_usesign': 1, 'atc_convert': 1,
                'atc_rvrc': 0,
                'atc_enhidetype': 'rvrc', 'atc_money': 0, 'atc_credittype': 'money', 'atc_desc1': '', 'att_special1': 0,
                'att_ctype1': 'money', 'atc_needrvrc1': 0, 'step': 2, 'pid': '', 'action': action, 'fid': fid, 'tid': tid,
                'article': 0, 'special': 0, }
        resp = self.session.post('http://localhost/phpwind/post.php?', data=data)
        resp.encoding = 'utf-8'
        if '发帖完毕点击进入主题列表' in resp.text:
            self.do_update("update pass_fail_count set pass=pass+1 where type='%s'" % type)
        else:
            self.do_update("update pass_fail_count set fail=fail+1 where type='%s'" % type)

    # 发帖测试
    def test_post(self):
        resp = self.session.get('http://localhost/phpwind/')
        resp.encoding = 'utf-8'
        pattern = r'thread.php\?fid=(.+?)" target="_blank'  # 非贪婪模式
        result = re.findall(pattern, resp.text)
        fid = random.sample(result, 1)[0]

        self.do_post(fid=fid)

    # 测试回帖
    def test_reply(self):
        # 从首页中找fid
        resp = self.session.get('http://localhost/phpwind/')
        resp.encoding = 'utf-8'
        pattern = r'thread.php\?fid=(.+?)" target="_blank'  # 非贪婪模式
        result = re.findall(pattern, resp.text)
        fid = random.sample(result, 1)[0]

        # 从版块中找tid
        resp = self.session.get('http://localhost/phpwind/thread.php?fid=%s' % fid)
        pattern = 'id="a_ajax_(.+?)">'
        result = re.findall(pattern, resp.text)
        tid = random.sample(result, 1)[0]

        self.do_post(fid=fid, tid=tid, action='reply')

    # 调用并执行迭代，并统计每一个请求的响应时间
    def start_run(self):
        for i in range(10):
            think_time = random.randint(1,3)

            start_time = time.time() * 1000
            self.test_login()
            end_time = time.time() * 1000
            login_time = int(end_time-start_time)

            time.sleep(think_time)   # 思考时间，暂停时间, Think Time

            start_time = time.time()*1000
            self.test_post()
            end_time = time.time()*1000
            post_time = int(end_time-start_time)

            time.sleep(think_time)

            start_time = time.time() * 1000
            self.test_reply()
            end_time = time.time() * 1000
            reply_time = int(end_time - start_time)

            now_time = time.strftime('%Y-%m-%d %H:%M:%S')
            sql = "insert into response_time(version, scenario, login, post, reply, dotime) values('%s', '%s', %d, %d, %d, '%s')" % (
                '1.2', '50*10', login_time, post_time, reply_time, now_time
            )
            self.do_update(sql)

            self.session = requests.session()

if __name__ == '__main__':
    for i in range(50):
        pwt = PhpWindTest()
        threading.Thread(target=pwt.start_run).start()