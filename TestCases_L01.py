from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Initialize WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open the website
    driver.get("https://itude-manado-blora.web.app/id/food/home")
    wait = WebDriverWait(driver, 15)

    # Ensure the page is fully loaded
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Step 2: Navigate to the language selection option
    language_select_element = wait.until(
        EC.presence_of_element_located((By.ID, 'language'))
    )

    # Scroll into view and select "English"
    driver.execute_script("arguments[0].scrollIntoView();", language_select_element)
    language_select_element = wait.until(
        EC.element_to_be_clickable((By.ID, 'language'))
    )
    language_select = Select(language_select_element)
    language_select.select_by_value('en-US')

    # Wait for the language change to take effect (you might need to add some time here)

    # Check if the language has changed to English (verify any element with English text)
    english_option = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//option[@value="en-US"]'))
    )

    assert english_option.text == 'English', "Language change to English unsuccessful"
    print("Test Case LT-01: Pass")

finally:
    driver.quit()
