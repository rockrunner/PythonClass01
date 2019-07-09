from selenium import webdriver
import time, os, random

firefox_path = r"C:\Program Files (x86)\Mozilla Firefox 61\firefox.exe"
driver_path = r"C:\Tools\geckodriver.exe"
driver = webdriver.Firefox(firefox_binary=firefox_path, executable_path=driver_path)
driver.get("http://localhost:8088/woniusales/")
time.sleep(2)

# driver.find_element_by_XXX()  单数形式，只会根据元素的特征属性找到唯一的一个，如果有多个，则返回第一个，返回WebElement类型。
# driver.find_elements_by_XXX() 复数形式，返回所有匹配特征属性的元素，并保存到一个list对象中。

# driver.find_element_by_id('username').send_keys('admin')
# driver.find_elements_by_id('username')[0].send_keys('admin')

# input_list = driver.find_elements_by_tag_name('input')
# print(type(input_list))
# for input in input_list:
#     print(input.get_attribute('id') + ': ' + input.get_attribute('type'))

# 利用复数来为验证码输入12345
# input_list = driver.find_elements_by_tag_name('input')
# for input in input_list:
#     if input.get_attribute('onkeypress') == 'doLogin(event)':
#         input.send_keys('12345')
#
# time.sleep(3)
# input_list = driver.find_elements_by_class_name('form-control')
# # input_list[2].send_keys('34567')
# for input in input_list:
#     if input.get_attribute('onkeypress') == 'doLogin(event)':
#         input.send_keys('56789')


# driver.find_element_by_xpath("/html/body/div[4]/div/form/div[2]/input").send_keys('admin123')
# driver.find_element_by_xpath("/html/body/div[4]/div/form[@class='form-inline']/div[2]/input").send_keys('admin123')
# driver.find_element_by_xpath("//input[@type='password']").send_keys('admin123')

# driver.find_element_by_xpath("//form[@class='form-inline']/div[2]/input").send_keys('admin123')
# driver.find_element_by_xpath("//form/div[2]/input").send_keys('45678')

# driver.find_element_by_css_selector("#username").send_keys("admin456")
# driver.find_element_by_css_selector(".form-inline input").send_keys("admin789")
# driver.find_element_by_css_selector(".form-inline>div:nth-child(4)>input").send_keys('12345')

driver.find_element_by_id('username').send_keys('admin')
# driver.find_element_by_xpath("//form[@class='form-inline']/div[3]/input").send_keys('admin123')
# driver.find_element_by_css_selector("input[type='password']").send_keys('admin123')
driver.find_element_by_css_selector("input[type$='word']").send_keys('admin123')
driver.find_element_by_css_selector("form.form-inline>div:nth-child(4)>input").send_keys('0000')
driver.find_element_by_css_selector("form.form-inline>div:last-child>button").click()
