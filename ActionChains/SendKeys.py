from selenium                                       import webdriver

from selenium.webdriver.support.ui                  import WebDriverWait

from selenium.webdriver.common.by                   import By

from selenium.webdriver.common.action_chains        import ActionChains

from selenium.webdriver.common.keys                 import Keys

import unittest

import time


class sendKeys(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com")
        driver.maximize_window()
    
    
    
    def test_sendKeys(self):
        #Locators
        searchFieldName      = "q"
        turtlePictureLocator = "//div[@title='Leatherback Turtle Picture']"
        
        searchFieldElement   = WebDriverWait(driver, 10).\
                               until(lambda driver: driver.find_element_by_name(searchFieldName))
        
        actions = ActionChains(driver)  #Used to create action chains
        actions.send_keys_to_element(searchFieldElement, "Leatherback")
        actions.send_keys_to_element(searchFieldElement, Keys.ENTER)
        actions.perform()
        
        WebDriverWait(driver, 10).\
            until(lambda driver: driver.find_element_by_xpath(turtlePictureLocator))



    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



