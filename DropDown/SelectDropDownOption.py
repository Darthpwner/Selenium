from selenium                           import webdriver

from selenium.webdriver.support.ui      import WebDriverWait

from selenium.webdriver.common.by       import By

from selenium.webdriver.support.select  import Select

import unittest

import time


class SelectDropDownOption(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()
     
    def test_SelectDropDownOption(self):

        # First Method
        
        # dropDownID         = "wsite-com-product-option-Quantity"
        # dropDownElement    = WebDriverWait(driver, 10).\
        #                      until(lambda driver: driver.find_element_by_id(dropDownID))
        # Select(dropDownElement).select_by_visible_text("2")

        # Second method
        
        dropDownOption        = "select#wsite-com-product-option-Quantity option[value='2']"
        dropDownOptionElement = WebDriverWait(driver, 10).\
                             until(lambda driver: driver.find_element_by_css_selector(dropDownOption))
        dropDownOptionElement.click()
        """
            This is a comment!
        """

        """
        I am only using time.sleep() here for you to see the last action of 
        selenium webdriver.I do not recommend using it in your tests.
        """
        time.sleep(6)
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



