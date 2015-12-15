from selenium                           import webdriver

from selenium.webdriver.support.ui      import WebDriverWait

from selenium.webdriver.common.by       import By

from selenium.webdriver.support.select  import Select

import unittest

class SwitchToWindow(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/p3/Asala_Loadge.html")
        driver.maximize_window()
     
    def test_SwitchToFacebookWindow(self):
        #Locators
        facebookSharingLinkLocator   = "a.wsite-com-product-social-facebook"
        facebookUsernameFieldID      = "email"
        facebookPasswordFieldID      = "pass"
        facebookLoginButtonName      = "login"
        facebookShareLinkButtonName  = "share"
        
        #Facebook credentials.
        facebookUsername             = "tutorys123@gmail.com"
        facebookPassword             = "year2014"
        
        fbSharingLinkElement = WebDriverWait(driver, 10).\
                        until(lambda driver: driver.find_element_by_css_selector(facebookSharingLinkLocator))
         
        # Get the main Window handle
        mainWindowHandle = driver.window_handles
        print "main Window handle: %s" %mainWindowHandle
             
        # Click the "Facebook sharing" link, switch to the Facebook login window and log in
        fbSharingLinkElement.click()
        allWindowsHandlesList = driver.window_handles
        print "all window handles: %s" %allWindowsHandlesList
        for handle in allWindowsHandlesList:
            if handle != mainWindowHandle[0]:
               driver.switch_to.window(handle)
               break
        facebookUsernameFieldElement   = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_id(facebookUsernameFieldID))
        
        facebookPasswordFieldElement   = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_id(facebookPasswordFieldID))
        
        facebookLoginButtonElement     = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_name(facebookLoginButtonName))
        
        facebookUsernameFieldElement.send_keys(facebookUsername)
        facebookPasswordFieldElement.send_keys(facebookPassword)
        facebookLoginButtonElement.click()
        WebDriverWait(driver, 10).\
        until(lambda driver: driver.find_element_by_name(facebookShareLinkButtonName))
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



