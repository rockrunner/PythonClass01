from pykeyboard import PyKeyboard
from selenium import webdriver
import time, os, random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class OtherUsage:
    # 初始化WebDriver
    def __init__(self):
        self.keyboard = PyKeyboard()
        # firefox_path = r"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe"
        # driver_path = r"C:\Tools\geckodriver.exe"
        # self.driver = webdriver.Firefox(firefox_binary=firefox_path, executable_path=driver_path)

        # chrome_driver = r"C:\Tools\chromedriver.exe"
        # self.driver = webdriver.Chrome(executable_path=chrome_driver)

        ie_driver = r"C:\Tools\IEDriverServer.exe"
        self.driver = webdriver.Ie(executable_path=ie_driver)

        self.driver.get("http://localhost:8088/woniusales/")
        time.sleep(2)

        # 页面操作常见方式
        # print(self.driver.title)
        # print(self.driver.current_url)
        # print(self.driver.page_source)
        # print(self.driver.get_window_size())
        # print(self.driver.fullscreen_window())
        self.driver.refresh()
        self.driver.back()
        self.driver.forward()


    def login(self):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("admin123")
        self.driver.find_element_by_id("verifycode").clear()
        self.driver.find_element_by_id("verifycode").send_keys("0000")
        self.driver.find_element_by_css_selector("button.form-control.btn-primary").click()

    # 窗口的切换
    def switch_window(self):
        # 对话框的切换: Alert/Confirm/Prompt
        # self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.driver.find_element_by_id("barcode").send_keys('6955203655011')
        # 当前窗口的标题和句柄：当前页面元素在操作系统中的一个唯一编号
        print('当前窗口标题为：%s' % self.driver.title)
        print('当前窗口句柄为：%s' % self.driver.current_window_handle)
        before_handle = self.driver.current_window_handle

        time.sleep(2)

        # 新的浏览器窗口
        # 在“销售出库”的超链接上点击右键，并在新标签页打开，模拟出双页面切换的效果
        # 所有的链式操作，在最后必须调用perform()方法完成执行
        # ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        batch_link = self.driver.find_element_by_link_text("会员管理")
        ActionChains(self.driver).context_click(batch_link).perform()
        self.keyboard.press_key(self.keyboard.down_key)
        self.keyboard.release_key(self.keyboard.down_key)
        self.keyboard.press_key(self.keyboard.enter_key)
        self.keyboard.release_key(self.keyboard.enter_key)
        time.sleep(2)

        # 在新页面中的窗口标题和句柄
        window_handles = self.driver.window_handles
        for handle in window_handles:
            if handle != before_handle:
                self.driver.switch_to.window(handle)
                if '会员管理' in self.driver.title:
                    break

        print('当前窗口标题为：%s' % self.driver.title)
        print('当前窗口句柄为：%s' % self.driver.current_window_handle)

        # 在新页面中：会员管理页面，点击查询按钮
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        time.sleep(2)


        # 回到旧页面，点击条码旁边的确认按钮
        self.driver.switch_to.window(before_handle)
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()


    def js_execute(self):
        time.sleep(2)
        # self.driver.execute_script("document.getElementById('barcode').value='6955203659590'")
        # self.driver.execute_script("document.getElementsByTagName('input')[5].click()")

        js_script = '''
            document.getElementById('username').value='admin';
            document.getElementById('username').style.border='solid 3px red';
            document.getElementById('password').value='admin123'
            document.getElementById('password').style.border='solid 3px blue';
            document.getElementById('verifycode').value='0000';
            doLogin('null');
        '''

        # self.driver.execute_script("document.getElementById('username').value='admin'")
        # self.driver.execute_script("document.getElementById('password').value='admin123'")
        # self.driver.execute_script("document.getElementById('verifycode').value='0000'")
        # self.driver.execute_script("doLogin('null')")

        self.driver.execute_script(js_script)
        time.sleep(2)
        self.driver.execute_script("document.getElementById('oldcredit').value='12345'")


    def capture_screen(self):
        self.driver.get_screenshot_as_file('D:/myscreen.png')


if __name__ == '__main__':
    other = OtherUsage()
    # other.login()
    # other.switch_window()
    # other.js_execute()
    # other.capture_screen()