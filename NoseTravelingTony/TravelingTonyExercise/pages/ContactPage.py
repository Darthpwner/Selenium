from BasePage                import BasePage
from BasePage                import IncorrectPageException
from TravelingTony.UIMap     import ContactPageMap


class ContactPage(BasePage):

    def __init__(self, driver):
		super(ContactPage, self).__init__(driver)
  

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "xpath", 
                                           ContactPageMap['FirstNameFieldXpath']
          )
        except:   
          raise IncorrectPageException
    
    def submit_request(self):
    	self.fill_out_field("xpath", 
                            ContactPageMap['FirstNameFieldXpath'], 
                            "Paul"
        )
    	self.fill_out_field("xpath", 
                            ContactPageMap['LastNameFieldXpath'], 
                            "Pierce"
        )
    	self.fill_out_field("xpath", 
                            ContactPageMap['EmailFieldXpath'], 
                            "contactemail@test.com"
        )
        self.fill_out_field("xpath", 
                            ContactPageMap['CommentFieldXpath'], 
                            "My comment"
        )
        self.click(10, 
                   "xpath", 
                   ContactPageMap['SubmitButtonXpath']
        )
        self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         ContactPageMap['ThankYouMessageXpath']
        )

    def validation_check(self):
        self.fill_out_field("xpath", 
                            ContactPageMap['FirstNameFieldXpath'], 
                            "Paul"
        )
        self.fill_out_field("xpath", 
                            ContactPageMap['LastNameFieldXpath'], 
                            "Pierce"
        )
        self.fill_out_field("xpath", 
                            ContactPageMap['EmailFieldXpath'], 
                            "contactemail@"
        )
        self.fill_out_field("xpath", 
                            ContactPageMap['CommentFieldXpath'], 
                            "My comment"
        )
        self.click(10, 
                   "xpath", 
                   ContactPageMap['SubmitButtonXpath']
        )
        return self
