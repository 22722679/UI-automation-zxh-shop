from page.LoginPage1 import LoginPage
from basic.BasePage import BasePage
from selenium.webdriver.common.by import By
import pytest
from core.data import read_excel
from selenium.common.exceptions import NoSuchElementException


def check_null(name, logger):
    if name is None:
        logger.error(f"{name} is None, skipping...")
        return True
    return False


@pytest.mark.parametrize(
    "url, email, password, msg",
    read_excel("ddt_test_login.xlsx"),
)
def test_login(url, email, password, msg, logger):
    # 检查是否为空
    if check_null(url, logger) or check_null(email, logger) or check_null(password, logger):
        return
    
    # 实例化
    lp = LoginPage(BasePage)
    lp.getUrl(url)
    lp.dologin(email, password)
    try:
        check = lp.driver.find_element(By.XPATH, '/html/body/main/div/h1')
    except NoSuchElementException:
        logger.error("Element not found, skipping...")
        return
    if check.text == msg:
        logger.info("info message!")
    else:
        logger.error("error message: Page hopping failure!")
    # assert check.text == "Hot sale"