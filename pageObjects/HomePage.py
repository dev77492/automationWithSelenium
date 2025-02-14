import time

from selenium.webdriver.common.by import By
from random import randint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    userName = "Harshad" + str(randint(1,1000))
    password = "IamAScammer"  + str(randint(1,1000))

    signUpBtn = (By.CSS_SELECTOR, "#signin2")
    userNameContainer = (By.CSS_SELECTOR, "#sign-username")
    passContainer = (By.CSS_SELECTOR, "#sign-password")
    signUpContainer = (By.XPATH, "//button[normalize-space()='Sign up']")

    signInContainer= (By.CSS_SELECTOR, "#login2")
    signIn_UsrNameContainer= (By.CSS_SELECTOR, "#loginusername")
    signIn_passContainer = (By.CSS_SELECTOR, "#loginpassword")
    signInBtn = (By.XPATH, "//div/button[@onclick='logIn()']")
    userValidation = (By.XPATH, "//a[@id='nameofuser']")
    def signUp(self, driver):
        driver.find_element(*HomePage.signUpBtn).click()
        driver.find_element(*HomePage.userNameContainer).send_keys(HomePage.userName)
        driver.find_element(*HomePage.passContainer).send_keys(HomePage.password)
        driver.find_element(*HomePage.signUpContainer).click()
        return


    def signIn(self, driver):
        driver.find_element(*HomePage.signInContainer).click()
        driver.find_element(*HomePage.signIn_UsrNameContainer).send_keys(HomePage.userName)
        driver.find_element(*HomePage.signIn_passContainer).send_keys(HomePage.password)
        driver.find_element(*HomePage.signInBtn).click()
        welcomeText = driver.find_element(By.XPATH, "//a[@id='nameofuser']").text
        print("Msg: " + welcomeText)
        # try:
        #     # Wait for the welcome message to be visible and have non-empty text
        #     welcome_element = WebDriverWait(driver, 10).until(
        #         EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome")
        #     )
        #     welcomeText = driver.find_element(By.ID, "nameofuser").text
        #     print("Msg: " + welcomeText)
        # except Exception as e:
        #     print("Failed to fetch welcome message: " + str(e))






