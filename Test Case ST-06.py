from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Test Scenario ST-06
def test_social_media_icons_navigation():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://itude-manado-blora.web.app/id/food/home")

    # Assuming social media icons are contained within a parent element with class "social-media-icons-container"
    social_media_container = driver.find_element(By.CSS_SELECTOR, ".social-media-icons-container")
    social_media_icons = social_media_container.find_elements(By.CSS_SELECTOR, "a")

    for icon in social_media_icons:
        icon.click()
        # Switch to the new window/tab opened by the social media link
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)  # Wait for the page to load
        # Add verification steps here, e.g., assert expected page URL, etc.
        driver.close()
        # Switch back to the main window/tab
        driver.switch_to.window(driver.window_handles[0])

    driver.quit()

# Run the test
test_social_media_icons_navigation()
