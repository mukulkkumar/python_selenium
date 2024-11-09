from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decorator import retry_on_timeout
import logging

@retry_on_timeout(max_attempts=3, wait_seconds=5)
def scroll_to_element_by_attribute_with_wait(driver, attribute, value, visible=True, clickable=True, scroll=True, wait_time=5):
    """
    Scrolls to an element on the webpage based on the given attribute and waits for it to be present, visible, or clickable.

    :param driver: Selenium WebDriver instance
    :param attribute: Attribute type (e.g., By.ID, By.CLASS_NAME)
    :param value: Value of the attribute to locate the element
    :param visible: Wait for the element to be visible (default is True)
    :param clickable: Wait for the element to be clickable (default is True)
    :param scroll: Scroll to the element if True (default is True)
    :param wait_time: Maximum time to wait for the element (default is 5 seconds)
    :return: The WebElement if found
    """

    logging.info(f"Attribute is {attribute} and value is {value}")

    # Scroll to the top of the page
    body_element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    body_element.send_keys(Keys.CONTROL + Keys.HOME)

    # Waiting for the element to be present in the DOM
    element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((attribute, value))
    )

    if scroll:
        # Scrolling to the location of the element
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})", element)

    if visible:
        # Waiting for the element to be present and visible in the DOM
        element = WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((attribute, value))
        )

    if clickable:
        # Waiting for the element to be clickable
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((attribute, value))
        )

    return element
