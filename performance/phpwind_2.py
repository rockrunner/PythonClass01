# 随机地向不同的板块发帖，随机地找一些帖子来进行回复，以达到灌水广告的目的。（随机的方式：通过响应关联查找，通过数据库）
# 如何模拟更加真实的情况？比如用户名能不能是一样的？比如登录完成后马上帖子就能发？多线程多循环发，监控一下性能指标（CPU，内存，带宽）
# 请问：发一个帖子需要多长时间？发帖的成功率有多高？比如发了5000个帖子，成功了多少，失败了多少？

import requests, time, random, threading, pymysql, re

class PhpWindTest:

    login_pass_count = 0
    login_fail_count = 0

    post_pass_count = 0
    post_fail_count = 0

    reply_pass_count = 0
    reply_fail_count = 0

    def __init__(self):
        self.session = requests.session()
        self.conn = pymysql.connect('localhost', 'root', '', 'phpwind', charset='utf8')
        self.cursor = self.conn.cursor()

    def do_login(self):
        sequence = random.randint(1, 20)
        data = {'forward':'','jumpurl':'http://localhost/phpwind/index.php','step':'2','lgt':'0',
                'pwuser':'pyuser_%d' % sequence,'pwpwd':'123456','hideid':'0','cktime':'31536000'}
        resp = self.session.post('http://localhost/phpwind/login.php?', data=data)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            PhpWindTest.login_pass_count += 1
        else:
            PhpWindTest.login_fail_count += 1
            print(resp.text)

    def do_post(self):
        # 随机找到一个版块编号
        # 方案一：直接从数据库读取一条随机的fid
        # sql = "select fid from pw_forums where type='forum' order by RAND() limit 0,1"
        # self.cursor.execute(sql)
        # result = self.cursor.fetchone()
        # fid = result[0]

        # 方案二：直接从首页的响应中读取一条fid
        resp = self.session.get('http://localhost/phpwind/')
        resp.encoding = 'utf-8'
        # pattern = r'thread.php\?fid=(.*)" target="_blank'
        pattern = r'thread.php\?fid=(.+?)" target="_blank'   #  非贪婪模式
        result = re.findall(pattern, resp.text)
        fid = random.sample(result, 1)[0]

        resp = self.session.get('http://localhost/phpwind/post.php?fid=%s' % fid)
        resp.encoding = 'utf-8'
        pattern = 'verify" value="(.*)" />'
        result = re.findall(pattern, resp.text)

        # 验证码存在的位置：通常情况下，哪个页面发起了该请求（该请求的referer字段），则验证码很有可能存在于该页面中。
        sequence = random.randrange(10000000, 99999999)
        data = {'magicname':'','magicid':'','verify': result[0],'atc_title':'这是一个Python帖子标题-%d' % sequence,'atc_iconid':0,
                'atc_content':'这是一个Python帖子内容-%d' % sequence,'atc_autourl':1,'atc_usesign':1,'atc_convert':1,'atc_rvrc':0,
                'atc_enhidetype':'rvrc','atc_money':0,'atc_credittype':'money','atc_desc1':'','att_special1':0,
                'att_ctype1':'money','atc_needrvrc1':0,'step':2,'pid':'','action':'new','fid':fid,'tid':'','article':0,'special':0,}
        resp = self.session.post('http://localhost/phpwind/post.php?', data=data)
        resp.encoding = 'utf-8'
        # if '发帖完毕点击进入主题列表' in resp.text:
        if re.match('.*发帖完毕点击进入主题列表.*', resp.text, re.DOTALL):   # 使用re.DOTALL标记指定 . 可以匹配\r\n
            PhpWindTest.post_pass_count += 1
        else:
            PhpWindTest.post_fail_count += 1
            print(resp.text)

    def do_reply(self):
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

        # 从发帖页面中找verify
        resp = self.session.get('http://localhost/phpwind/post.php?fid=%s' % fid)
        resp.encoding = 'utf-8'
        pattern = 'verify" value="(.*)" />'
        result = re.findall(pattern, resp.text)

        # 对该帖子进行回复
        sequence = random.randrange(10000000, 99999999)
        data = {'magicname': '', 'magicid': '', 'verify': result[0], 'atc_title': 'Re:这是一个Python帖子标题-%d' % sequence,
                'atc_iconid': 0,
                'atc_content': 'Re:这是一个Python帖子内容-%d' % sequence, 'atc_autourl': 1, 'atc_usesign': 1, 'atc_convert': 1,
                'atc_rvrc': 0,
                'atc_enhidetype': 'rvrc', 'atc_money': 0, 'atc_credittype': 'money', 'atc_desc1': '', 'att_special1': 0,
                'att_ctype1': 'money', 'atc_needrvrc1': 0, 'step': 2, 'pid': '', 'action': 'reply', 'fid': fid, 'tid': tid,
                'article': 0, 'special': 0, }
        resp = self.session.post('http://localhost/phpwind/post.php?', data=data)
        resp.encoding = 'utf-8'
        # if '发帖完毕点击进入主题列表' in resp.text:
        if re.match('.*发帖完毕点击进入主题列表.*', resp.text, re.DOTALL):  # 使用re.DOTALL标记指定 . 可以匹配\r\n
            PhpWindTest.reply_pass_count += 1
        else:
            PhpWindTest.reply_fail_count += 1
            print(resp.text)


    def main_test(self):
        for i in range(20):
            self.do_login()

            think_time = random.randint(1, 3)
            time.sleep(think_time)   # 思考时间，暂停时间, Think Time

            start_time = time.time()*1000
            self.do_post()
            end_time = time.time()*1000
            print(int(end_time-start_time))

            time.sleep(think_time)

            self.do_reply()

            self.session = requests.session()


if __name__ == '__main__':

    for i in range(50):
        pwt = PhpWindTest()
        threading.Thread(target=pwt.main_test).start()


    time.sleep(10)
    print('登录成功数：%d, 登录失败数：%d，发帖成功数：%d，发帖失败数：%d，回复成功数：%d，回复失败数：%d' % (
        PhpWindTest.login_pass_count, PhpWindTest.login_fail_count,
        PhpWindTest.post_pass_count, PhpWindTest.post_fail_count,
        PhpWindTest.reply_pass_count, PhpWindTest.reply_fail_count
    ))
