from BasePage                import BasePage
from ShareOnFacebookPage     import ShareOnFacebookPage
from BasePage                import IncorrectPageException


class FacebookLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(FacebookLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "id", 
                                           "email"
          )
        except:   
          raise IncorrectPageException
    
    def login(self):
        self.fill_out_field("id", 
                            "email", 
                            self.username
        )
        self.fill_out_field("id", 
                            "pass", 
                            self.password
        )
        self.click(10, "name", "login")
        return ShareOnFacebookPage(self.driver)
        
        
    
      
    




