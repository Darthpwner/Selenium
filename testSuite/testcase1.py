from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by  import By

import unittest


class TestCase1(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com")
    
    
    def test_WaitForCheckOutPhotosButton(self):
        bLocator = "//span[.='Check out my coolest photos']"
        seebutton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, bLocator)))

    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



