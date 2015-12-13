from BasePage                import BasePage
from FacebookLoginPage       import FacebookLoginPage
from TravelingTony.Constants import TT_Constants
from BasePage                import IncorrectPageException


class ProductPage(BasePage):

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)
  

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "id", 
                                         "wsite-com-product-option-Quantity"
          )
        except:   
          raise IncorrectPageException
    
    def click_share_on_facebook_button(self):
        mainWindowHandle = self.driver.window_handles
        self.click(10, "xpath", "//a[@title='Share on Facebook']")
        allWindowHandles = self.driver.window_handles
        for handle in allWindowHandles:
         if handle != mainWindowHandle[0]:
          self.switch_to_window(handle)
          break
        return FacebookLoginPage(self.driver, 
                                 TT_Constants['Facebook_Username'],
                                 TT_Constants['Facebook_Password'] 
        )
        
    
      
    

