from selenium                           import webdriver

from selenium.webdriver.support.ui      import WebDriverWait

from selenium.webdriver.common.by       import By

from selenium.webdriver.support.select  import Select

import unittest




class ShareOnTwitter(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()
     
    def test_ShareOnTwitter(self):
        #Locators
        twitterSharingLinkLocator   = "a[@class='wsite-com-product-social-twitter']"
        twitterUsernameFieldID      = "username_or_email"
        twitterPasswordFieldID      = "password"
        twitterSignInButtonLocator  = "input[type=submit]"
        tweetButtonLocator          = "input[value=Tweet]"
        
        #Twitter test account credentials.
        twitterUsername             = "tutorys123@gmail.com"
        twitterPassword             = "year2014"
        
        twSharingLinkElement = WebDriverWait(driver, 10).\
                        until(lambda driver: driver.find_element_by_xpath(twitterSharingLinkLocator))
         
        # Get the main Window handle
        mainWindowHandle = driver.window_handles
        print "main Window handle: %s" %mainWindowHandle
             
        # Click the "Twitter sharing" link, switch to the Twitter login window and log in
        twSharingLinkElement.click()
        allWindowsHandlesList = driver.window_handles
        print "all window handles: %s" %allWindowsHandlesList
        for handle in allWindowsHandlesList:
            if handle != mainWindowHandle[0]:
               driver.switch_to.window(handle)
               break
        twitterUsernameFieldElement   = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_id(twitterUsernameFieldID))
        
        twitterPasswordFieldElement   = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_id(twitterPasswordFieldID))
        
        twitterSignInButtonElement    = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_css_selector(twitterSignInButtonLocator))
        
        twitterUsernameFieldElement.send_keys(twitterUsername)
        twitterPasswordFieldElement.send_keys(twitterPassword)
        twitterSignInButtonElement.click()
        WebDriverWait(driver, 10).\
        until(lambda driver: driver.find_element_by_css_selector(tweetButtonLocator))
        
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



s