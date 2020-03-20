# coding=utf-8
# @公众号 : "鹏哥贼优秀"
# @Date : 2020/3/20
# @Software : PyCharm
# @Python version: Python 3.7.2
from selenium import webdriver
from slide_solution import *
import time

def visit_website(url):
    # 配置window.navigator.webdrive
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome('F:\\Python成长之路\\\滑块问题\\chromedriver.exe',options=option)
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    # 输入帐户密码
    driver.find_element_by_name('account').send_keys('手机号')
    driver.find_element_by_name('password').send_keys('password')
    slide_btn = driver.find_element_by_css_selector('span[class="nc_iconfont btn_slide"]')
    # 滑块解决方法1
    slide_solution1(slide_btn,driver)
    # 点击登录
    driver.find_element_by_class_name('btn').click()
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    url = 'https://login.zhipin.com/?ka=header-login'
    visit_website(url)