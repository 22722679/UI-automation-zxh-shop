from selenium import webdriver


class BasePage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(1500, -200)
        self.driver.maximize_window()

    # 打开浏览器
    def getUrl(self, url):
        self.driver.get(url)

    # 关闭浏览器
    def quitBrower(self):
        self.driver.quit()

    # 点击 *参数名 如果传入的参数是（），
    # 自动根据（）内的元素数量，进行自动解析，如果是2个，就相当于2个参数 如果3个，就相当于3个参数
    def click(self, selector):
        self.driver.find_element(*selector).click()

    # 输入文字
    def sendkeys(self, selector, context):
        self.driver.find_element(*selector).send_keys(context)

# 拖动，滑动， 双击...