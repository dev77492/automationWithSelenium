import pytest
from selenium import webdriver
driver=None

@pytest.fixture(params=["chrome","firefox"],scope="class")
def setup(request):
    global driver
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif(request.param=="firefox"):
        driver = webdriver.Firefox()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield
    driver.close()



