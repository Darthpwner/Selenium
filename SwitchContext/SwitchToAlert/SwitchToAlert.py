from selenium                           import webdriver

from selenium.webdriver.support.ui      import WebDriverWait

from selenium.webdriver.common.by       import By

from selenium.webdriver.support.select  import Select

import unittest

import time


class SwitchToAlert(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.tizag.com/javascriptT/javascriptconfirm.php")
        driver.maximize_window()
    
    def test_SwitchToAlert(self):
        #Locators
        leaveButtonLocator    = "//input[@value='Leave Tizag.com']"
        leaveButtonElement    = WebDriverWait(driver, 10).\
                                until(lambda driver: driver.find_element_by_xpath(leaveButtonLocator))
        leaveButtonElement.click()
        alert = driver.switch_to.alert
        alert.accept() #Accepts the alert
        
        """
        I am only using time.sleep() here for you to see the last action of selenium webdriver. I do not recommend using it in your tests.
        """
        time.sleep(6)
        
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



