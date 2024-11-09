from selenium.webdriver.common.by import By
from selenium import webdriver
from mixins import *
import logging
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

try:
    element = scroll_to_element_by_attribute_with_wait(driver, By.NAME, "q", visible=True, clickable=True)
    element.send_keys('Python')
    element.submit()
    time.sleep(5)
except Exception as e:
    logging.error(f"Error: {e}")
finally:
    driver.quit()
