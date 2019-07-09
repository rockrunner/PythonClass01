from gevent import monkey
monkey.patch_all()  # 利用monkey库给Python的代码注入补丁，让其支持协程
import gevent, multiprocessing, threading
import time, random, requests, re

# def test_1():
#     for i in range(5):
#         now = time.strftime('%Y-%m-%d %H:%M:%S')
#         print('test_1: ' + now)
#         time.sleep(1)
#
# def test_2():
#     for j in range(5):
#         now = time.strftime('%Y-%m-%d %H:%M:%S')
#         print('test_2: ' + now)
#         time.sleep(1)
#
# def test_3():
#     for j in range(5):
#         now = time.strftime('%Y-%m-%d %H:%M:%S')
#         print('test_3: ' + now)
#         time.sleep(1)
#
#
# # 将两个函数添加到事件队列中
# g1 = gevent.spawn(test_1)
# g2 = gevent.spawn(test_2)
# g3 = gevent.spawn(test_3)
# gevent.joinall([g1, g2, g3])



# 利用协程模拟登录和发帖
def test_phpwind():
    session = requests.session()

    users = ['pyuser_1', 'pyuser_2', 'pyuser_3', 'pyuser_4', 'pyuser_5', 'pyuser_6', 'pyuser_7', 'pyuser_8',
                  'pyuser_9', 'pyuser_10']
    username = random.sample(users, 1)[0]
    data = {'forward': '', 'jumpurl': 'http://localhost/phpwind/index.php', 'step': '2', 'lgt': '0',
            'pwuser': username, 'pwpwd': '123456', 'hideid': '0', 'cktime': '31536000'}
    resp = session.post(url='http://localhost/phpwind/login.php', data=data)
    resp.encoding = 'utf-8'
    if '您已经顺利登录' in resp.text:
        print("登录成功")  # 告诉Locust运行器，本次请求成功
    else:
        print('登录失败.')

    # 方案二：直接从首页的响应中读取一条fid
    resp = session.get('http://localhost/phpwind/')
    resp.encoding = 'utf-8'
    # pattern = r'thread.php\?fid=(.*)" target="_blank'
    pattern = r'thread.php\?fid=(.+?)" target="_blank'  # 非贪婪模式
    result = re.findall(pattern, resp.text)
    fid = random.sample(result, 1)[0]

    resp = session.get('http://localhost/phpwind/post.php?fid=%s' % fid)
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
    resp = session.post('http://localhost/phpwind/post.php?', data=data)
    resp.encoding = 'utf-8'
    if '发帖完毕点击进入主题列表' in resp.text:
        print("发帖成功")
    else:
        print('发帖失败.')


if __name__ == '__main__':
    list = []
    for i in range(100):
        # 多进程调用
        # multiprocessing.Process(target=test_phpwind).start()

        # 多线程调用
        # threading.Thread(target=test_phpwind).start()

        # 协程调用
        g = gevent.spawn(test_phpwind)
        list.append(g)

    gevent.joinall(list)
