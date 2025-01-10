from selenium.webdriver.common.by import By
from basic.BasePage import BasePage

from time import sleep


class CartCheckout(BasePage):
    # 用户名输入框
    def __init__(self, driver):
        self.driver = driver
        BasePage.__init__(self)
        # 商品数量
        self.quantity = (By.XPATH, '//*[@id="productNum"]')
        # 点击购物车
        self.addcart = (By.XPATH, '/html/body/main/div/div/div/div/div[3]/form/input[3]')
        # 创建订单
        self.cartcommit = (By.XPATH, '/html/body/main/div/div/div/div/a')
        # cvv
        self.cvv = (By.XPATH, '//*[@id="cvv"]')
        # 提交订单
        self.checkoutcommit = (By.XPATH, '/html/body/main/div/div/div/form/div[9]/div/input')
        # 商品
        self.product = (By.XPATH, '/html/body/main/div/div/div[2]/a')
        
        # 登录
        # 用户名框 
        self.hc_username = (By.XPATH, '//*[@id="email"]')
        # 密码框 
        self.hc_password = (By.XPATH, '//*[@id="password"]')
        # 登录按钮
        self.loginbtn = (By.XPATH, '/html/body/main/div/div/div/form/button')
    
    # 确认当前可以做的操作
    def docheckout(self, productN, quantity, unitprice, cvv):
        # 选择商品
        self.product = (By.XPATH, productN)
        print(self.product)
        try:
            self.click(self.product)
        except Exception as e:
            _ = e
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            self.click(self.product)
        # 选择数量
        self.sendkeys(self.quantity, quantity)
        sleep(1)
        # 添加入购物车
        self.click(self.addcart)
        sleep(1)
        # 创建订单
        self.click(self.cartcommit)
        sleep(1)
        # 订单信息输入
        self.sendkeys(self.cvv, cvv)
        # 下滑页面
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(4)
        # 订单提交
        self.click(self.checkoutcommit)
        sleep(10)

    # 返回首页
    def returnHome(self):
        self.click((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/a'))

    # 重新登陆
    def dologin(self, uname, pwd):
        # 跳转到登录页面
        self.click((By.XPATH, '//*[@id="navbarSupportedContent"]/div/a'))
        # 输入用户名
        self.sendkeys(self.hc_username, uname)
        sleep(1)
        # 输入密码
        self.sendkeys(self.hc_password, pwd)
        sleep(1)
        self.click(self.loginbtn)
        sleep(1)