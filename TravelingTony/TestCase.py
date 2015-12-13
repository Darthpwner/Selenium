from TravelingTony.BaseTestCase            import BaseTestCase
from TravelingTony.Constants               import TT_Constants
from TravelingTony.Common                  import Common

class TestCase(BaseTestCase):

  def setUp(self):
      super(TestCase, self).setUp()
      productPageURL = TT_Constants['Base_URL']+"store/p1/Leatherback_Turtle_Picture.html"
      self.navigate_to_page(productPageURL)
      common_obj = Common(self.driver)
      common_obj.wait_for_element_visibility(10, 
                                             "id", 
                                             "wsite-com-product-option-Quantity"
      )
      mainWindowHandle  = self.driver.window_handles
      common_obj.click(10, "xpath", "//a[@title='Share on Facebook']")
      allWindowsHandles = self.driver.window_handles
      for handle in allWindowsHandles:
        if handle != mainWindowHandle[0]:
          common_obj.switch_to_window(handle)
          break
      common_obj.wait_for_element_visibility(10, 
                                             "id", 
                                             "email"
      )
      common_obj.fill_out_field("id",
                                "email", 
                                TT_Constants['Facebook_Username']
      )
      common_obj.fill_out_field("id", 
                                "pass", 
                                TT_Constants['Facebook_Password']
      )
      common_obj.click(10, "name", "login")
      common_obj.wait_for_element_visibility(10, 
                                             "name", 
                                             "share"
      )
      
      
      
  def tearDown(self):
  	  super(TestCase, self).tearDown()
