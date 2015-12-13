from selenium                                 import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support               import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                      import abstractmethod
from TravelingTony.Constants                  import LocatorMode
from BasePage import BasePage
from TravelingTony.UIMap import ContactPageMap

class ContactPage(BasePage):

  def __init__(self, driver):
    super(ContactPage, self).__init__(driver)

  def _verify_page(self):
    try:
      self.wait_for_element_visibility(10, "xpath", "//input[contains(@name, 'first')]")
    except:
      raise IncorrectPageException  #Used if we don't find the correct page

  def submit_request(self):
      self.fill_out_field("xpath", "//input[contains(@name, 'first')]", "Paul")
      self.fill_out_field("xpath", "//input[contains(@name, 'last')]", "Pierce")
      self.fill_out_field("xpath", "(//input[contains(@id, 'input')])[3]", "contactemail@test.com")
      self.fill_out_field("xpath", "//textarea", "My comment")
      self.click(10, "xpath", "//span[.='Submit']")
      self.wait_for_element_visibility(10, "xpath", "//div[contains(text(), 'Thank you')]")

  def validation_check(self):
      self.fill_out_field("xpath", "//input[contains(@name, 'first')]", "Paul")
      self.fill_out_field("xpath", "//input[contains(@name, 'last')]", "Pierce")
      self.fill_out_field("xpath", "(//input[contains(@id, 'input')])[3]", "contactemail@test.com")
      self.fill_out_field("xpath", "//textarea", "My comment")
      self.click(10, "xpath", "//span[.='Submit']")
      return self #returns the contact page