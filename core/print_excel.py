import logging
from core.data import read_excel
from server.register import test_register
from server.login import test_login
from server.cart_checkout import test_cart_checkout
from log.log import Logger


def print_excel_login(logdocument, loginput):
    logger = Logger("webdriver", logdocument, CmdLevel=logging.DEBUG, FileLevel=logging.INFO)
    i = 1
    for d in read_excel(loginput):
        logger.debug("----------------------test case %d----------------------" % i)
        test_login(*d, logger)
        i+=1
    logger.info("--------------------------------test finished--------------------------------")


def print_excel_register(logdocument, loginput):
    logger = Logger("webdriver", logdocument, CmdLevel=logging.DEBUG, FileLevel=logging.INFO)
    i = 1
    for d in read_excel(loginput):
        logger.debug("----------------------test case %d----------------------" % i)
        test_register(*d, logger)
        i+=1
    logger.info("--------------------------------test finished--------------------------------")


def print_excel_cart_checkout(logdocument, loginput):
    logger = Logger("webdriver", logdocument, CmdLevel=logging.DEBUG, FileLevel=logging.INFO)
    i = 1
    for d in read_excel(loginput):
        logger.debug("----------------------test case %d----------------------" % i)
        test_cart_checkout(*d, logger)
        i+=1
    logger.info("--------------------------------test finished--------------------------------")