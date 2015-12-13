from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support               import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                      import abstractmethod
from TravelingTony.Constants                  import LocatorMode
from BasePage import BasePage
from TravelingTony.UIMap import ShareOnFacebookPageMap

class ShareOnFacebookPage(BasePage):

  def __init__(self, driver):
    super(ShareOnFacebookPage, self).__init__(driver)

  def _verify_page(self):
    try:
      self.wait_for_element_visibility(10, "name", "share")
    except:
      raise IncorrectPageException  #Used if we don't find the correct page

  def share(self):
    self.click(10, "name", "share")
