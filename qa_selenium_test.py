import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    chrome_options = Options()
    # Initialize Chrome WebDriver (Selenium will automatically manage the driver version)
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture(scope="module")
def driver():
    driver_instance = setup_driver()
    yield driver_instance  # Provide the driver to test functions
    driver_instance.quit()  # Cleanup: Close the browser after tests complete


def test_search_functionality(driver):

    #Open the web page
    url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    driver.get(url)

    #Locate the search box and wait until it's visible
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']")))

    #Perform search for 'New York'
    search_term = "New York"
    search_box.clear()  # Clear any previous text
    search_box.send_keys(search_term)  # Enter search query
    search_box.send_keys(Keys.RETURN)  # Press Enter

    #Wait until search results update
    wait.until(EC.text_to_be_present_in_element((By.ID, "example_info"), "Showing"))

    #Validate that exactly 5 rows are displayed
    rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")
    visible_rows = [row for row in rows if row.is_displayed()]

    assert len(visible_rows) == 5, f"Expected 5 visible rows, but got {len(visible_rows)}"

    #Ensure all displayed rows contain 'New York'
    for row in visible_rows:
        assert "New York" in row.text, f"Row does not contain expected text: {row.text}"

    #Verify total entries text (confirming '24 total entries')
    entries_text = driver.find_element(By.ID, "example_info").text
    assert "filtered from 24 total entries" in entries_text, f"Total entries text validation failed. Found: {entries_text}"

    print("Test completed successfully.")
