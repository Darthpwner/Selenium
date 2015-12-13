from TravelingTony.TestCase                   import TestCase
from TravelingTony.Constants                  import TT_Constants
from TravelingTony.pages.ShareOnFacebookPage  import ShareOnFacebookPage
import unittest
import nose
from nose.plugins.attrib import attr


class ShareOnFacebookTest(TestCase, unittest.TestCase):

    def setUp(self):
        super(ShareOnFacebookTest, self).setUp()
      
    @attr(priority="low")  
    def test_ShareOnFacebookTest(self):
        share_on_facebook_page_obj = ShareOnFacebookPage(self.driver)
        share_on_facebook_page_obj.share()
    
    def tearDown(self):
        super(ShareOnFacebookTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



