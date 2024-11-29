import allure
from utilities.logger import setup_logger
from pages.home_page import HomePage
import pytest

# Set up the logger
log = setup_logger(__name__)


@pytest.fixture
def home_page(browser, base_url):
    """Fixture to navigate to the base URL and return a HomePage instance."""
    browser.get(base_url)
    return HomePage(browser)


def log_test_start(test_name):
    """Helper to log the start of a test."""
    log.info(f"{test_name} started")


def log_test_completion(test_name):
    """Helper to log the successful completion of a test."""
    log.info(f"{test_name} successfully completed")


@allure.description("Test 1 - Verifies email, password inputs, and login button functionality.")
def test_test1(home_page):
    log_test_start("Test 1")

    # Assert email, password inputs, and login button are present
    assert home_page.is_element_present(HomePage.EMAIL_INPUT), "Email input not found"
    assert home_page.is_element_present(HomePage.PASSWORD_INPUT), "Password input not found"
    assert home_page.is_element_present(HomePage.LOGIN_BUTTON), "Login button not found"

    # Enter email and password
    home_page.login("dinatest@gmail.com", "test")

    log_test_completion("Test 1")


@allure.description("Test 2 - Verifies the list items and their details in Test 2 section.")
def test_test2(home_page):
    log_test_start("Test 2")

    # Assert there are three list items
    items = home_page.get_list_items()
    assert len(items) == 3

    # Assert the second item's text and badge value
    second_item_text, second_item_badge = home_page.get_list_item_details(1)
    assert second_item_text == "List Item 2", "Second item's text does not match"
    assert second_item_badge == "6", "Second item's badge value does not match"

    log_test_completion("Test 2")


@allure.description("Test 3 - Verifies dropdown functionality and selection updates in Test 3 section.")
def test_test3(home_page):
    log_test_start("Test 3")

    # Assert "Option 1" is the default selected value in the dropdown
    assert home_page.get_dropdown_button_text() == "Option 1", "Default dropdown value does not match"

    # Select "Option 3" from the dropdown
    home_page.select_dropdown_option("Option 3")

    # Assert the selected value is now "Option 3"
    assert home_page.get_dropdown_button_text() == "Option 3", "Dropdown value did not update"

    log_test_completion("Test 3")


@allure.description("Test 4 - Verifies button states in Test 4 section.")
def test_test4(home_page):
    log_test_start("Test 4")

    # Assert first button is enabled and second button is disabled
    buttons = home_page.get_buttons()
    assert buttons[0].is_enabled(), "First button is not enabled"
    assert not buttons[1].is_enabled(), "Second button is not disabled"

    log_test_completion("Test 4")


@allure.description("Test 5 - Verifies dynamic button appearance and success message functionality.")
def test_test5(home_page):
    log_test_start("Test 5")

    # Wait for the button to be displayed, then click it
    home_page.wait_and_click(HomePage.BUTTON_TEST5)

    # Assert success message is displayed
    assert home_page.is_element_present(HomePage.ALERT_TEST5), "Success message not displayed"

    # Assert the button is now disabled
    assert not home_page.is_button_enabled(HomePage.BUTTON_TEST5), "Button is still enabled after being clicked"

    log_test_completion("Test 5")


@allure.description("Test 6 - Verifies the value of a specific table cell.")
def test_test6(home_page):
    log_test_start("Test 6")

    # Get the value of cell (2, 2) and assert its value
    cell_value = home_page.get_table_cell_value(2, 2)
    assert cell_value == "Ventosanzap", "Table cell value does not match"

    log_test_completion("Test 6")


