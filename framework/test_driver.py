import time, os

from selenium.webdriver.common.by import By
from framework.support import Support
from framework.testcase_sell import TestSell
from framework.testcase_batch import TestBatch

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class TestDriver:
    def __init__(self):
        brower = 'firefox'
        self.support = Support()
        self.driver = Support.get_webdriver(brower)
        self.sell = TestSell(brower, self.support)
        self.batch = TestBatch(brower, self.support)

    def prepare(self):
        self.driver.get('http://localhost:8088/woniusales/')
        time.sleep(2)

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("admin1234")
        self.driver.find_element_by_id("verifycode").clear()
        self.driver.find_element_by_id("verifycode").send_keys("0000")
        self.driver.find_element_by_css_selector("button.form-control.btn-primary").click()

        if self.support.is_element_present(By.LINK_TEXT, u"注销"):
            self.support.write_result('测试登录功能\t成功')
        else:
            self.support.write_result('测试登录功能\t失败')
            self.support.capture_screen()


    def start_test(self):
        self.sell.main_test()
        self.batch.main_test()


    # 测试结束后，发送邮件
    def send_email(self, file_name):
        sender = 'student@woniuxy.com'  # 发送邮箱
        receivers = 'dengqiang@woniuxy.com'  # 接收邮箱

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # message = MIMEText('<p style="color: red; font-size: 30px">这是一封来自Python发送的测试邮件的内容...</p>', 'html', 'utf-8')
        # message['Subject'] = Header('一封Python发送的邮件', 'utf-8')

        msg = MIMEMultipart()
        msg['Subject'] = '一封Python发送的邮件'
        msg['From'] = sender
        msg['To'] = receivers

        content = MIMEText('<p style="color: red; font-size: 30px">这是一封来自Python发送的测试邮件的内容...</p>', 'html', 'utf-8')
        # content = '这是一封来自Python发送的测试邮件的内容...'
        msg.attach(content)

        attachment = MIMEApplication(open(file_name, 'rb').read())
        attachment.add_header('Content-Disposition', 'attachment', filename='test.jpg')
        msg.attach(attachment)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect('mail.woniuxy.com', '25')
            smtpObj.login(user='student@woniuxy.com', password='Student123')
            smtpObj.sendmail(sender, receivers, str(msg))
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

    # 发送测试短信
    def send_sms(self):
        # 去短信平台注册一个企业短信账号
        # 用Python+UIAutomation驱动手机助手发短信
        pass

    # 压缩报表目录
    def compress_report(cls):
        report_folder = os.path.abspath(".") + "/report"
        winrar_file = r'"C:\Program Files (x86)\WinRAR\WinRAR.exe"'
        cmd = winrar_file + " a report.rar " + report_folder
        os.system(cmd)
        time.sleep(3)
        return os.path.abspath(".") + "/report.rar"


if __name__ == '__main__':
    driver = TestDriver()
    # driver.prepare()
    # driver.start_test()
    driver.send_email(r'D:\022104084679376.jpg')

    # 如何全自动地运行，或者在规定的时间运行，或者在某个条件下自动启动测试脚本?
    # 持续集成 CI   https://www.cnblogs.com/fnng/p/8232410.html

