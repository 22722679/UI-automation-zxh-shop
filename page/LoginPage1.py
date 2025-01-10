# 当定义了页面后
# 干两件事  1.把这个页面的元素定位信息写到这个页面类中 2.把这个页面的操作能做的操作方法写成函数
## 先学着 怎么分页面的元素

"""
共享元素（多个页面都有的元素）独立到一个其他页面中
共享元素，独立到一个其他元素去，你可以去虚构一个页面
"""
from selenium.webdriver.common.by import By
from basic.BasePage import BasePage
from time import sleep


class LoginPage(BasePage):
    # 用户名输入框
    def __init__(self, driver):
        self.driver = driver
        BasePage.__init__(self)
        # 用户名框 
        self.hc_username = (By.XPATH, '//*[@id="email"]')
        # 密码框 
        self.hc_password = (By.XPATH, '//*[@id="password"]')
        # 登录按钮
        self.loginbtn = (By.XPATH, '/html/body/main/div/div/div/form/button')
    # 确认当前可以做的操作
    def dologin(self, uname, pwd):
        # 输入用户名
        self.sendkeys(self.hc_username, uname)
        sleep(1)
        # 输入密码
        self.sendkeys(self.hc_password, pwd)
        sleep(1)
        self.click(self.loginbtn)
        sleep(1)

"""
解决问题：1.确认输入的用户名应该是在哪个元素里？ 2.确认输入的密码应该是在哪个元素里？ 3.确认点击登录按钮应该是在哪个元素里？
"""