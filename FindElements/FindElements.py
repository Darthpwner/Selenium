from selenium import webdriver

from selenium.webdriver.common.by  import By

from selenium.webdriver.support.ui import WebDriverWait

import unittest


class FindElements(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/c2/Lope.html")
        #driver.implicitly_wait(15)
    
    
    def test_FindElements(self):
        #webElementsList      = driver.find_elements_by_xpath("//img")
        #webElementsList      = driver.find_elements_by_css_selector("img")
        webElementsList      = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath("//img"))
        #webElementsList      = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_css_selector(""))
        print webElementsList
    
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



