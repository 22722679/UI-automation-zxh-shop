from core.print_excel import print_excel_cart_checkout, print_excel_login, print_excel_register


def Login():
    print_excel_login("test_login.log", "ddt-test_login.xlsx")


def Register():
    print_excel_register("test_register.log", "ddt-test_register.xlsx")
    
    
def CartCheckout():
    print_excel_cart_checkout("test_cart_checkout.log", "ddt_test_cart_checkout.xlsx")


if __name__ == '__main__':
    # 登录测试
    # Login()

    # 注册测试
    # Register()
    CartCheckout()