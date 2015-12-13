from TravelingTony.TestCase                   import TestCase
from TravelingTony.Constants                  import TT_Constants
from TravelingTony.Common                     import Common
import unittest
import time

class ShareOnFacebookTest(TestCase, unittest.TestCase):

    def setUp(self):
        super(ShareOnFacebookTest, self).setUp()
        
        
    def test_SendRequestTest(self):
        common_obj = Common(self.driver)
        common_obj.click(10, "name", "share")
        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(ShareOnFacebookTest, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



