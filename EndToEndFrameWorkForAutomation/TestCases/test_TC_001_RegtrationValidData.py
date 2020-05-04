from selenium.webdriver import Chrome
from Base import InitiateDriver


def test_validate_reg():
    driver=InitiateDriver.Start_browser()
    driver.maximize_window()
    driver.get("http://thetestingworld.com/testings")
    driver.close()