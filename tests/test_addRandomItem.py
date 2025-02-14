import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
import pytest

from EcommerceProject.tests.test_UserLogin import TestUserLogin


class AddItemToCart(TestUserLogin):
    def __init__(self):
        TestUserLogin.test_CreateUser()
        TestUserLogin.test_login()

    def test_addItemToCart(self):

        driver= self.driver


