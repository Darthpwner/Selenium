# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# import time

# browser = webdriver.Firefox() # Get local session of firefox
# browser.get("http://www.yahoo.com") # Load page
# assert "Yahoo!" in browser.title
# elem = browser.find_element_by_name("p") # Find the query box
# elem.send_keys("seleniumhq" + Keys.RETURN)
# time.sleep(0.2) # Let the page load, will be added to the API
# try:
#     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
# except NoSuchElementException:
#     assert 0, "can't find seleniumhq"
# browser.close()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 

import unittest

class X(unittest.TestCase):

	driver = webdriver.Firefox()

	driver.get("http://google.com")

	fLocator = "input[name=q]"

	try:
		searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, fLocator)))

		#Why doesn't this work? It says "TypeError: __init__() takes exactly 2 arguments (3 given)"
	#	searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, fLocator))
	finally:
		driver.quit()
if __Name__ == "__main__":
	unittest.main()