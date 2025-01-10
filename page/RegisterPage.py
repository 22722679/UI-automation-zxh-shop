from selenium.webdriver.common.by import By
from basic.BasePage import BasePage
from time import sleep


class RegisterPage(BasePage):
    # 用户名输入框
    def __init__(self, driver):
        self.driver = driver
        BasePage.__init__(self)
        # 用户名框 
        self.hc_username = (By.XPATH, '//*[@id="email"]')
        # 密码框 
        self.hc_password = (By.XPATH, '//*[@id="password"]')
        # 确认密码框
        self.cf_password = (By.XPATH, '//*[@id="password_confirm"]')
        # 注册按钮
        self.registerbtn = (By.XPATH, '/html/body/main/div/div/div/form/button')
    # 确认当前可以做的操作
    def doregister(self, uname, pwd, cfpwd):
        # 输入用户名
        self.sendkeys(self.hc_username, uname)
        sleep(1)
        # 输入密码
        self.sendkeys(self.hc_password, pwd)
        sleep(1)
        # 输入确认密码
        self.sendkeys(self.cf_password, cfpwd)
        sleep(1)
        self.click(self.registerbtn)
        sleep(1)