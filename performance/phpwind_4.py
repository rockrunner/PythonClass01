# 解决请求数量和完整性的问题

import requests, time, random, threading, pymysql, re

class PhpWindTest:
    def __init__(self):
        self.session = requests.session()

    # 定义一个专门用于下载页面资源文件的方法
    def do_download(self, content):

        res_list = []

        # 找所有css文件
        pattern_css = 'css" href="(.+?)" />'
        css_list = re.findall(pattern_css, content)
        for css in css_list:
            res_list.append(css)

        # 找所有的图片
        pattern_img = 'url\((.+?)\)'
        img_list = re.findall(pattern_img, content)
        for img in img_list:
            res_list.append(img)

        pattern_img_2 = 'img src="(.+?)"'
        img_list_2 = re.findall(pattern_img_2, content)
        for img2 in img_list_2:
            res_list.append(img2)

        # 找所有的javascript
        pattern_js = 'src="(.+?).js'
        js_list = re.findall(pattern_js, content)
        for js in js_list:
            res_list.append(js + '.js')

        # print(len(res_list))
        res_set = set(res_list)
        # print(len(res_set))

        for res in res_set:
            url = 'http://localhost/phpwind/' + res
            resp = self.session.get(url)


        # for i in range(len(res_list)):
        #     res = res_list[i]
        #     for j in range(i+1, len(res_list)):
        #         if res == res_list[j]:
        #             res_list[j] = 9999
        #
        # print(res_list)


    def do_prepare(self):
        # 第一步：打开首页
        resp = self.session.get('http://localhost/phpwind')
        resp.encoding = 'utf-8'
        self.do_download(resp.text)

        resp = self.session.get('http://localhost/phpwind/login.php')
        resp.encoding = 'utf-8'
        self.do_download(resp.text)

    # 执行登录的测试
    def test_login(self):
        sequence = random.randint(1, 20)
        data = {'forward': '', 'jumpurl': 'http://localhost/phpwind/index.php', 'step': '2', 'lgt': '0',
                'pwuser': 'pyuser_%d' % sequence, 'pwpwd': '123456', 'hideid': '0', 'cktime': '31536000'}
        resp = self.session.post('http://localhost/phpwind/login.php?', data=data)
        resp.encoding = 'utf-8'


    def start_run(self):
        for i in range(50):
            self.do_prepare()
            self.test_login()
            time.sleep(2)


if __name__ == '__main__':
    for i in range(20):
        for j in range(10):
            pwt = PhpWindTest()
            threading.Thread(target=pwt.start_run).start()
        time.sleep(5)



session = requests.session()

sequence = random.randint(1, 20)
data = {'forward': '', 'jumpurl': 'http://localhost/phpwind/index.php', 'step': '2', 'lgt': '0',
        'pwuser': 'pyuser_%d' % sequence, 'pwpwd': '123456', 'hideid': '0', 'cktime': '31536000'}
resp = session.post('http://localhost/phpwind/login.php', data=data)
resp.encoding = 'utf-8'

resp = session.get('http://localhost/phpwind/')
resp.encoding = 'utf-8'
print(resp.text)