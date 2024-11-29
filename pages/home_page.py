from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "inputEmail")
    PASSWORD_INPUT = (By.ID, "inputPassword")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LIST_ITEMS = (By.CLASS_NAME, "list-group-item")
    DROPDOWN_BUTTON = (By.ID, "dropdownMenuButton")
    DROPDOWN_OPTION = "//a[contains(text(), '{}')]"
    BUTTONS = (By.CLASS_NAME, "btn")
    BUTTON_TEST5 = (By.ID, "test5-button")
    ALERT_TEST5 = (By.ID, "test5-alert")
    TABLE_CELL = "//table/tbody/tr[{row}]/td[{col}]"

    # Methods
    def login(self, email, password):
        """
        Log in by entering email and password and clicking the login button.
        """
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_list_items(self):
        """
        Get all list items on the page.
        :return: List of WebElements representing the list items.
        """
        return self.driver.find_elements(*self.LIST_ITEMS)

    def get_list_item_details(self, index):
        """
        Get the main text and badge value of a list item at a specific index.
        :param index: Index of the list item (0-based).
        :return: Tuple (item_text, badge_value).
        """
        items = self.get_list_items()
        list_item = items[index]

        # Extract the full text of the list item (including badge)
        full_text = list_item.text

        # Extract the badge value
        badge_value = list_item.find_element(By.CLASS_NAME, "badge").text

        # Remove the badge value from the full text to isolate the main text
        item_text = full_text.replace(badge_value, "").strip()

        return item_text, badge_value

    def get_dropdown_button_text(self):
        """
        Get the currently displayed text of the dropdown button.
        :return: String representing the text of the dropdown button.
        """
        return self.driver.find_element(*self.DROPDOWN_BUTTON).text

    def select_dropdown_option(self, option_text):
        """
        Select an option from the dropdown by its text.
        :param option_text: Text of the option to select.
        """
        self.click(self.DROPDOWN_BUTTON)
        option_locator = (By.XPATH, self.DROPDOWN_OPTION.format(option_text))
        self.click(option_locator)

    def get_buttons(self):
        """
        Get the buttons
        :return: List of WebElement buttons.
        """
        test_4_div = self.driver.find_element(By.ID, "test-4-div")
        return test_4_div.find_elements(By.CLASS_NAME, "btn")

    def get_table_cell_value(self, row, col):
        """
        Get the value of a cell in the table based on row and column (0-based index).
        :param row: Row index (0-based).
        :param col: Column index (0-based).
        :return: String representing the cell's value.
        """
        cell_locator = (By.XPATH, self.TABLE_CELL.format(row=row + 1, col=col + 1))
        return self.driver.find_element(*cell_locator).text

    def wait_and_click(self, locator, timeout=10):
        """
        Wait for an element to become visible , then click it.
        :param locator: Locator tuple for the element (e.g., (By.ID, "test5-button")).
        :param timeout: Maximum wait time in seconds.
        """
        button = WebDriverWait(self.driver, timeout).until(
            # Wait for element to be clickable
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def is_element_present(self, locator, timeout=10):
        """
        Check if an element is present on the page.
        :param locator: Locator tuple for the element.
        :param timeout: Maximum wait time in seconds.
        :return: True if the element is found, False otherwise.
        """
        try:
            self.wait_for_element(locator, timeout)
            return True
        except:
            return False

    def is_button_enabled(self, locator):
        """
        Check if a button is enabled (not disabled).
        :param locator: Locator tuple for the button (e.g., (By.ID, "test5-button")).
        :return: True if the button is enabled, False otherwise.
        """
        button = self.driver.find_element(*locator)
        return button.is_enabled()
