from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Test Case FT-06: Verify menu browsing and filtering on homepage
def test_menu_browsing_and_filtering():
    # Start the WebDriver
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # Load the website homepage
        driver.get("https://itude-manado-blora.web.app/id/food/home")

        # 1. Locate main menu categories using the updated CSS selector
        main_menu_categories = driver.find_elements(By.CSS_SELECTOR, "a[class*='mat-ripple'][href*='/id/food/menu/']")

        # 2. Click on a category
        for category in main_menu_categories:
            category.click()

            # Wait for the page to load
            driver.implicitly_wait(5)

            # Assert that the category click navigates to a subpage
            assert "%20" in driver.current_url, f"Category click did not navigate to a subpage: {driver.current_url}"

            # Navigate back to the homepage for the next category click
            driver.back()

    finally:
        # Quit the WebDriver
        driver.quit()


# Run the test
test_menu_browsing_and_filtering()
