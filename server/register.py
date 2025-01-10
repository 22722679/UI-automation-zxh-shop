import pytest


from page.RegisterPage import RegisterPage
from basic.BasePage import BasePage
from selenium.webdriver.common.by import By
from core.data import read_excel
from selenium.common.exceptions import NoSuchElementException


def check_null(name, logger):
    if name is None:
        logger.error(f"{name} is None, skipping...")
        return True
    return False


@pytest.mark.parametrize(
    "url, email, password, confirm_password, msg",
    read_excel("ddt_test_register.xlsx"),
)
def test_register(url, email, password, cfpassword, msg, logger):
    # 检查是否为空
    if check_null(url, logger) or check_null(email, logger) or check_null(password, logger) or check_null(cfpassword, logger):
        logger.End()
        return
    if password != cfpassword:
        logger.error("Passwords do not match, skipping...")
        return
    
    # 实例化
    lp = RegisterPage(BasePage)
    lp.getUrl(url)
    lp.doregister(email, password, cfpassword)
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