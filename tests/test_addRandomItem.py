import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
import pytest
from typing import ClassVar
from selenium.webdriver import Chrome

from EcommerceProject.attributes.BaseClass import BaseClass
from EcommerceProject.pageObjects.ItemsPage import ItemsPage
from EcommerceProject.tests.test_UserLogin import TestUserLogin

@pytest.mark.usefixtures("setup")
class AddItemToCart():
    driver: ClassVar[Chrome]

    def __init__(self):
        TestUserLogin.test_login()

    def test_addItemToCart(self):
        driver = self.driver
        itemList = ItemsPage()
        itemList.get_ItemsInList(driver)


