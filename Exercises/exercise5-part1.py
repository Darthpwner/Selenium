from TravelingTony.Constants            import TT_Constants
from TravelingTony.BaseTestCase         import BaseTestCase
from TravelingTony.Common               import Common
import unittest
import time


class SearchProductTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(SearchProductTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_SearchProductTest(self):
        common_obj = Common(self.driver)
        # Wait for the "search" field to display. We are locating the search field by name.
        common_obj.wait_for_element_visibility(10, 
                                               "name",
                                               "q"
        )
        # Enter the word "leatherback" into the search field
        common_obj.fill_out_field("name",
                                  "q",
                                  "leatherback"
        )
        # Submit the search by clicking the "search submit" button. We are locating the search field by class using Css Selector.
        common_obj.click(10, "cssSelector", "span.wsite-search-button")
        
        # Verify that the turtle picture is displayed. We are locating the picture item by class using Css Selector
        common_obj.wait_for_element_visibility(10, 
                                               "cssSelector",
                                               "div.wsite-search-product-image-container"
        )

        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)

    
    def tearDown(self):
        super(SearchProductTest, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



