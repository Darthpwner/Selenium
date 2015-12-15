from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by  import By

import unittest

import time


class BasicActions(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com")
        driver.maximize_window()
    
    
    
    def test_BasicActions(self):
        contactMenuLocator = "//a[.='Contact']"
        nameFieldLocator   = "//input[contains(@name, 'first')]"
        contactMenuElement = WebDriverWait(driver, 10).\
                             until(lambda driver: driver.find_element_by_xpath(contactMenuLocator))
        contactMenuElement.click()

        nameFieldElement   = WebDriverWait(driver, 10).\
                             until(lambda driver: driver.find_element_by_xpath(nameFieldLocator))
        nameFieldElement.send_keys("George")
        time.sleep(6)
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



