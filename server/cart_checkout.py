from page.CartCheckout import CartCheckout
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
    "url, productN, quantity, unitprice, cvv, assertl",
    read_excel("ddt_test_cart_checkout.xlsx"),
)
def test_cart_checkout(url, email, email_password, productN, quantity, unitprice, cvv, assertl, logger):
    # 检查是否为空
    if check_null(url, logger) or check_null(productN, logger) or check_null(quantity, logger) or check_null(unitprice, logger) or check_null(cvv, logger) or check_null(assertl, logger) or check_null(email, logger) or check_null(email_password, logger):
        return
    
    # 实例化
    lp = CartCheckout(BasePage)
    lp.getUrl(url)

    try:
        _ = lp.driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/span')
    except NoSuchElementException:
        lp.dologin(email, email_password)
        logger.info("account UnLogin, login now!")
        lp.returnHome()
    
    lp.docheckout(productN, quantity, unitprice, cvv)

    ass = lp.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div')
    if ass.text == assertl:
        logger.info("info message!")
    else:
        logger.error("error message: Page hopping failure!")
    # assert check.text == "Hot sale"