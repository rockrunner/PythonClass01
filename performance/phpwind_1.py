import requests, time, random, threading, pymysql, re

class PhpWindTest:
    def __init__(self):
        self.session = requests.session()

    def do_reg(self):
        for i in range(2, 21):
            data = {'forward':'','step':'2','regname':'pyuser_%d' % i,'regpwd':'123456','regpwdrepeat':'123456',
                    'regemail':'pyuser_%d@woniuxy.com' % i,'rgpermit':'1'}
            resp = requests.post('http://localhost/phpwind/register.php?', data=data)
            resp.encoding = 'utf-8'
            print(resp.text)

    # 课堂练习：利用Python对Phpwind实现发帖
    def do_login(self):
        data = {'forward':'','jumpurl':'http://localhost/phpwind/index.php','step':'2','lgt':'0',
                'pwuser':'pyuser_4','pwpwd':'123456','hideid':'0','cktime':'31536000'}
        resp = self.session.post('http://localhost/phpwind/login.php?', data=data)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            print("登录成功.")
        else:
            print("登录失败.")


    def do_post(self):

        resp = self.session.get('http://localhost/phpwind/post.php?fid=7')
        resp.encoding = 'utf-8'
        pattern = 'verify" value="(.*)" />'
        result = re.findall(pattern, resp.text)
        print(result[0])


        # 验证码存在的位置：通常情况下，哪个页面发起了该请求（该请求的referer字段），则验证码很有可能存在于该页面中。
        data = {'magicname':'','magicid':'','verify': result[0],'atc_title':'这是一个Python帖子标题-10000','atc_iconid':0,
                'atc_content':'这是一个Python帖子内容-10000','atc_autourl':1,'atc_usesign':1,'atc_convert':1,'atc_rvrc':0,
                'atc_enhidetype':'rvrc','atc_money':0,'atc_credittype':'money','atc_desc1':'','att_special1':0,
                'att_ctype1':'money','atc_needrvrc1':0,'step':2,'pid':'','action':'new','fid':7,'tid':'','article':0,'special':0,}
        resp = self.session.post('http://localhost/phpwind/post.php?', data=data)
        resp.encoding = 'utf-8'
        # if '发帖完毕点击进入主题列表' in resp.text:
        if re.match('.*发帖完毕点击进入主题列表.*', resp.text, re.DOTALL):   # 使用re.DOTALL标记指定 . 可以匹配\r\n
            print("发帖成功.")
        else:
            print("发帖失败.")

        # print(resp.text)



if __name__ == '__main__':
    pwt = PhpWindTest()
    # pwt.do_reg()
    pwt.do_login()
    pwt.do_post()


# 随机地向不同的板块发帖，随机地找一些帖子来进行回复，以达到灌水广告的目的。（随机的方式：通过响应关联查找，通过数据库）
# 如何模拟更加真实的情况？比如用户名能不能是一样的？比如登录完成后马上帖子就能发？多线程多循环发，监控一下性能指标（CPU，内存，带宽）
# 请问：发一个帖子需要多长时间？发帖的成功率有多高？比如发了5000个帖子，成功了多少，失败了多少？