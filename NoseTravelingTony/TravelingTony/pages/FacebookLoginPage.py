from BasePage                import BasePage
from ShareOnFacebookPage     import ShareOnFacebookPage
from BasePage                import IncorrectPageException
from TravelingTony.UIMap     import FacebookLoginPageMap


class FacebookLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(FacebookLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "id", 
                                           FacebookLoginPageMap['UsernameFieldID']
          )
        except:   
          raise IncorrectPageException
    
    def login(self):
        self.fill_out_field("id", 
                            FacebookLoginPageMap['UsernameFieldID'], 
                            self.username
        )
        self.fill_out_field("id", 
                            FacebookLoginPageMap['PasswordFieldID'], 
                            self.password
        )
        self.click(10, 
                   "name", 
                   FacebookLoginPageMap['LoginButtonName']
        )
        return ShareOnFacebookPage(self.driver)
        
        
    
      
    




