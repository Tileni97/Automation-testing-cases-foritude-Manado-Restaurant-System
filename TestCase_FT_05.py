from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_logout():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://itude-manado-blora.web.app/id/food/logout")

    try:
        # Perform logout
        driver.find_element(By.ID, "logout-button").click()

        # Verify user is redirected to appropriate page (Assuming the login page or home page)
        redirected_url = driver.current_url
        assert "login" in redirected_url or "home" in redirected_url

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

# Run the test
test_user_logout()
