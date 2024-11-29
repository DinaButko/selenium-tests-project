import chromedriver_autoinstaller
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def base_url():
    """
    Fixture to provide the base URL for the test site.
    """
    return "https://dinabutko.github.io/selenium-tests-resolver/"


@pytest.fixture(scope="function")
def browser():
    """
    Fixture to initialize the Selenium WebDriver with headless Chrome and automatic Chromedriver management.
    """
    # Automatically download and install the correct version of Chromedriver
    chromedriver_autoinstaller.install()

    # Chrome options
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--disable-gpu")  # Disable GPU in headless mode
    options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
