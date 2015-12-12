from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 

driver = webdriver.Firefox()

driver.get("http://google.com")

fLocator = "input[name=q]"

try:
	searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, fLocator)))

	#Why doesn't this work? It says "TypeError: __init__() takes exactly 2 arguments (3 given)"
#	searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, fLocator))
finally:
	driver.quit()