from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time, os, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class WoniuSalesTwo:
    def __init__(self):
        # 手工指定Firefox的路径和Driver的路径:
        firefox_path = r"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe"
        driver_path = r"C:\Tools\geckodriver.exe"
        # 打开浏览器，启动GeckoDriver应用程序
        self.driver = webdriver.Firefox(firefox_binary=firefox_path, executable_path=driver_path)

        # 让浏览器最大化
        self.driver.maximize_window()
        # 设置等待的超时时间
        self.driver.set_page_load_timeout(10)    # 页面加载的超时时间
        self.driver.set_script_timeout(10)       # 执行JavaScript脚本的超时时间
        self.driver.implicitly_wait(10)         # 如果元素没有找到，尝试继续等待的时间

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
        # 输入商品条码
        self.driver.find_element_by_id("barcode").clear()
        self.driver.find_element_by_id("barcode").send_keys("6955203659590")
        # 利用WebDriver的Keys类完成在某个HTML元素上的回车键。
        self.driver.find_element_by_id('barcode').send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()

        time.sleep(2)

        if self.driver.find_element_by_id('tempbuyprice').text == '96.75':
            print("扫码成功.")
        else:
            print('扫码失败.')

        # 选择支付方式(下拉框的处理)
        pay_method = self.driver.find_element_by_id('paymethod')
        options = Select(pay_method).options    # 获取到整个下拉框的选项
        # Select(pay_method).select_by_visible_text('微信')     # 根据选项的文本来选择
        # Select(pay_method).select_by_value('微信')            # 根据option标签的value属性来选择
        # Select(pay_method).select_by_index(2)                 # 根据选项的索引来进行选择

        # 利用索引随机选择支付方式
        random_index = random.randrange(0, len(options))
        Select(pay_method).select_by_index(random_index)


        # 输入会员信息
        self.driver.find_element_by_id('customerphone').send_keys('18683645768')
        # self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        self.driver.find_element_by_id('submit').click()

        # 处理弹出确认框Alert/Confirm/Prompt
        # self.driver.switch_to.alert.accept()    # 点击弹框的确定按钮
        # self.driver.switch_to.alert.dismiss()   # 点击弹框的取消按钮
        # self.driver.switch_to.alert.send_keys('在window.prompt里面输入的内容')
        # content = self.driver.switch_to.alert.text        # 获取弹出框里面的提示内容
        # if '没有提供会员信息' in content:
        #     print("表示没有提供会员信息的弹框")
        # else:
        #     print("干点别的什么事")

        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.driver.switch_to.alert.accept()


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
    wst = WoniuSalesTwo()
    wst.login()
    wst.sell()