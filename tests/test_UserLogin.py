import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from EcommerceProject.attributes.BaseClass import BaseClass
from selenium.webdriver.common.alert import Alert
import pytest

from EcommerceProject.pageObjects.HomePage import HomePage


class TestUserLogin(BaseClass):

    def test_CreateUser(self):
        # pass
        driver = self.driver

        homePage = HomePage()
        try:
            homePage.signUp(driver)
            wait = WebDriverWait(driver, 5)
            wait.until(expected_conditions.alert_is_present())
            # Switch to alert
            alert = driver.switch_to.alert
            popUpText = alert.text
            print("Popup Text:", popUpText)

            # Take a screenshot after closing alert
            # driver.save_screenshot("popUp.png")

            # Accept the alert (click OK)
            alert.accept()
            assert "successful" in popUpText


        except Exception as e:
            print("The exception is  :" + str(e))

    def test_login(self):
        driver = self.driver
        try:

            logiinPage=HomePage()
            logiinPage.signIn(driver)
            self.waitforTextToAppear(HomePage.userValidation, "Welcome")
            welcomeText = driver.find_element(*HomePage.userValidation).text
            # print("Msg: " + welcomeText)
            assert f"Welcome {logiinPage.userName}" == welcomeText

        except Exception as e:
            print("Login failed :" + str(e))







