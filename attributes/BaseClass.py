import pytest
import logging
from typing import ClassVar
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    driver: ClassVar[Chrome]

    def waitForEntity(self,entity):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(entity))

    def waitforTextToAppear(self,entity, text):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.text_to_be_present_in_element(entity, text))