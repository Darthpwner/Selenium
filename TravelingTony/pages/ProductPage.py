from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support               import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                      import abstractmethod
from TravelingTony.Constants                  import LocatorMode
from BasePage import BasePage

class ProductPage(BasePage):

  def __init__(self, driver):
    super(ProductPage, self).__init__(driver)

  def _verify_page(self):
    try:
      self.wait_for_element_visibility(10, "id", "wsite-com-product-option-Quantity")
    except:
      raise IncorrectPageException  #Used if we don't find the correct page

  def click_on_facebook_share_button(self):
    mainWindowHandle = self.driver.window_handles
    self.click(10, "xpath", "//a[@titles='Share on Facebook']") #Click on FB share buton
    allWindowHandles = self.driver.window_handles
    for handle in allWindowHandles:
    if handle != mainWindowHandle[0]:
      self.switch_to_window(handle)
      break