from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')
time.sleep(3)

driver.find_element_by_css_selector('#form>span>input').send_keys('Python')
time.sleep(2)
print(driver.page_source)
driver.find_element_by_css_selector('#form>span>input:first-child').click()