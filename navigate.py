from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.google.com")

driver = webdriver.Firefox()

driver.get("http://www.facebook.com")

#driver = webdriver.Safari()

#driver.get("http://www.Apple.com")

driver.quit()