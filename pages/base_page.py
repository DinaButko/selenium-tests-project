from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """
        Wait for an element to be present on the page.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def is_element_present(self, locator, timeout=10):
        """
        Check if an element is present on the page.
        """
        try:
            self.wait_for_element(locator, timeout)
            return True
        except:
            return False

    def click(self, locator):
        """
        Wait for an element and click it.
        """
        element = self.wait_for_element(locator)
        element.click()

    def input_text(self, locator, text):
        """
        Wait for an element and input text.
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """
        Wait for an element and get its text.
        """
        element = self.wait_for_element(locator)
        return element.text
