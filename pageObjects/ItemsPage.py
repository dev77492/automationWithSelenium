from selenium.webdriver.common.by import By


class ItemsPage:


    web_itemsContainer = (By.XPATH, "//div/div/div/div/div/div/h4/a")


    def get_ItemsInList(self,driver):

        items=driver.find_elements(*ItemsPage.web_itemsContainer)

        for item in items:
            print (item.text)

    