from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support               import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                      import abstractmethod
from TravelingTony.Constants                  import LocatorMode
from BasePage import BasePage

class FacebookLoginPage(BasePage):

  def __init__(self, drive, username, password):
    super(FacebookLoginPage, self).__init__(driver)
    self.username = username
    self.password = password

  def _verify_page(self):
    try:
      self.wait_for_element_visibility(10, "id", "wsite-com-product-option-Quantity")
    except:
      raise IncorrectPageException  #Used if we don't find the correct page

  #Locate the field using email
  def login(self):
    self.fill_out_field("id", "email", self.username)
    self.fill_out_field("id", "pass", self.password)
    self.click(10, "name", "login")