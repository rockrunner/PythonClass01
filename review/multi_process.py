import multiprocessing, requests, random, re

pass_count = 0
fail_count = 0

def test(n):
    for i in range(n):
        session = requests.session()

        global pass_count, fail_count
        sequence = random.randint(1, 20)
        data = {'forward': '', 'jumpurl': 'http://localhost/phpwind/index.php', 'step': '2', 'lgt': '0',
                'pwuser': 'pyuser_%d' % sequence, 'pwpwd': '123456', 'hideid': '0', 'cktime': '31536000'}
        resp = session.post('http://localhost/phpwind/login.php?', data=data)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            print("登录成功: %d 次" % pass_count)
            pass_count += 1
        else:
            print("登录成功: %d 次" % fail_count)
            fail_count += 1

        resp = session.get('http://localhost/phpwind/post.php?fid=5')
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
                'att_ctype1': 'money', 'atc_needrvrc1': 0, 'step': 2, 'pid': '', 'action': 'new', 'fid': 5, 'tid': '',
                'article': 0, 'special': 0, }
        resp = session.post('http://localhost/phpwind/post.php?', data=data)
        resp.encoding = 'utf-8'
        if '发帖完毕点击进入主题列表' in resp.text:
            print("发帖成功: %d 次" % pass_count)
        else:
            print("发帖失败: %d 次" % fail_count)


if __name__ == '__main__':
    for i in range(50):
        multiprocessing.Process(target=test, args=(50,)).start()