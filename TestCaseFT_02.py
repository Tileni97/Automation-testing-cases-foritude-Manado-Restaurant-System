from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_signup_invalid():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://itude-manado-blora.web.app/id/food/register")

    try:
        # Print page source for debugging
        print(driver.page_source)

        # Enter invalid signup data
        driver.find_element(By.ID, "name").send_keys("Tems Timmy")
        driver.find_element(By.ID, "email").send_keys("jumanji")  # Invalid email format
        driver.find_element(By.ID, "phone").send_keys("0857738141")      # Assuming phone field for phone number
        driver.find_element(By.ID, "signUp-button").click()

        # Verify error message
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "error-message"))
        )
        assert "Invalid email format" in error_message.text

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

# Run the test
test_user_signup_invalid()
