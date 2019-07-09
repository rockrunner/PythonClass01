from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os


class WoniuSalesOne:
    def __init__(self):
        # 使用默认的Firefox和Driver路径
        # self.driver = webdriver.Firefox()
        # self.driver.get("http://localhost:8088/woniusales/")

        # 运行之前先结束已经启动的firefox.exe进程
        os.system('taskkill /F /IM firefox.exe')

        # 手工指定Firefox的路径和Driver的路径
        firefox_path = r"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe"
        driver_path = r"C:\Tools\geckodriver.exe"
        self.driver = webdriver.Firefox(firefox_binary=firefox_path, executable_path=driver_path)
        self.driver.get("http://localhost:8088/woniusales/")

    def login(self):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("admin123")
        self.driver.find_element_by_id("verifycode").clear()
        self.driver.find_element_by_id("verifycode").send_keys("0000")
        self.driver.find_element_by_css_selector("button.form-control.btn-primary").click()

        if self.is_element_present(By.LINK_TEXT, u"注销"):
            print("登录成功.")
        else:
            print("登录失败.")


    def sell(self):
        self.driver.find_element_by_id("barcode").clear()
        self.driver.find_element_by_id("barcode").send_keys("6955203659590")
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()

        time.sleep(2)

        if self.driver.find_element_by_id('tempbuyprice').text == '96.75':
            print("扫码成功.")
        else:
            print('扫码失败.')

        # self.driver.find_element_by_id("barcode").clear()
        # self.driver.find_element_by_id("barcode").send_keys("6955203659590")
        # self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        #
        # if self.driver.find_element_by_id('tempbuyprice').text == '193.50':
        #     print("扫码成功.")
        # else:
        #     print('扫码失败.')


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except:
            return False
        else:
            return True


    def __del__(self):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    wso = WoniuSalesOne()
    wso.login()
    wso.sell()