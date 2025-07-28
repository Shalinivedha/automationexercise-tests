from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
            logging.info(f"Clicked on element: {by_locator}")
        except TimeoutException:
            logging.error(f"Could not click on element: {by_locator}")
            raise

    def enter_text(self, by_locator, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            element.clear()
            element.send_keys(value)
            logging.info(f"Entered text '{value}' in element: {by_locator}")
        except TimeoutException:
            logging.error(f"Could not enter text in element: {by_locator}")
            raise

    def get_text(self, by_locator):
        try:
            text = self.wait.until(EC.visibility_of_element_located(by_locator)).text
            logging.info(f"Text found: '{text}' in element: {by_locator}")
            return text
        except TimeoutException:
            logging.error(f"Could not get text from element: {by_locator}")
            raise

    def is_visible(self, by_locator):
        try:
            visible = self.wait.until(EC.visibility_of_element_located(by_locator)).is_displayed()
            logging.info(f"Element visibility for {by_locator}: {visible}")
            return visible
        except TimeoutException:
            logging.error(f"Element not visible: {by_locator}")
            raise

    def select_dropdown(self, by_locator, visible_text):
        from selenium.webdriver.support.ui import Select
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located(by_locator))
            Select(dropdown).select_by_visible_text(visible_text)
            logging.info(f"Selected dropdown '{visible_text}' for element: {by_locator}")
        except TimeoutException:
            logging.error(f"Could not select from dropdown: {by_locator}")
            raise
# base_page.py