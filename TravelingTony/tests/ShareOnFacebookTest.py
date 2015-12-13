from TravelingTony.TestCase                   import TestCase
from TravelingTony.Constants                  import TT_Constants
from TravelingTony.pages.ShareOnFacebookPage import ShareOnFacebookPage
import unittest
import time

class ShareOnFacebookTest(TestCase, unittest.TestCase):

    def setUp(self):
        super(ShareOnFacebookTest, self).setUp()
        
        
    def test_ShareOnFacebookTest(self):
        share_on_facebook_page_obj = ShareOnFacebookPage(self.driver)
        share_on_facebook_page_obj.share()
        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(ShareOnFacebookTest, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



