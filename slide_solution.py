# coding=utf-8
# @公众号 : "鹏哥贼优秀"
# @Date : 2020/3/20
# @Software : PyCharm 
# @Python version: Python 3.7.2
from selenium.webdriver import ActionChains
import time
from jpype import *

def slide_solution1(slide_btn,driver):
    action = ActionChains(driver)
    action.click_and_hold(slide_btn).perform()
    for i in range(200):
        try:
            action.move_by_offset(i*2,0).perform()
        except:
            break
        action.reset_actions()
        time.sleep(0.1)

def slide_solution2():
    jvmPath = jpype.get_default_jvm_path()
    # Djava.class.path是本地的sikuliapi.jar包路径，需要提前下载好
    jpype.startJVM(jvmPath, '-ea', '-Djava.class.path=F:\\sikuli\\1\\sikulixapi.jar')
    Screen = JClass('org.sikuli.script.Screen')
    myscreen = Screen()
    myscreen.drag('start.PNG','end.PNG')
    time.sleep(0.5)