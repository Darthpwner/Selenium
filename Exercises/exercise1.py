from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://travelingtony.weebly.com/contact.html")

#1 Locate the page header "Traveling Tony's Photography" by substring "Traveling" using Xpath
driver.find_element_by_xpath("//span[contains(@id, 'wsite-title')]")
print("#1 passed")

#2 Locate the "search" field by class using Css
driver.find_element_by_css_selector("input.wsite-search-input")
print("#2 passed")

#3 Locate the "search" field by name using Css
driver.find_element_by_css_selector("[name=q]")
print("#3 passed")

#4 Locate the "search" field by class using Xpath
driver.find_element_by_xpath("//input[@class='wsite-search-input']")
print("#4 passed")

#5 Locate the "search" field by name using Xpath
driver.find_element_by_xpath("//input[@name='q']")
print("#5 passed")

driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")

#6 Locate the "Quantity" drop-down by id using Css
driver.find_element_by_css_selector("select#wsite-com-product-option-Quantity")
print("#6 passed")

#7 Locate the "Quantity" drop-down by class using Css
driver.find_element_by_css_selector("select.wsite-field")
print("#7 passed")

#8 Locate the "Quantity" drop-down by name using Xpath
driver.find_element_by_xpath("//select[@name='Quantity']")
print("#8 passed")

driver.quit()