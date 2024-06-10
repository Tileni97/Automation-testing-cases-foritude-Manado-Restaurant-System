from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_signup_valid():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://itude-manado-blora.web.app/id/food/register")

    try:
        # Print page source for debugging
        print(driver.page_source)

        # Enter valid signup data
        driver.find_element(By.ID, "name").send_keys("Tems Timmy")
        driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
        driver.find_element(By.ID, "phone").send_keys("0857738141")  # Assuming phone field for phone number
        driver.find_element(By.ID, "signUp-button").click()

        # Verify signup success
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "success-message"))
        )
        assert "Signup successful" in success_message.text

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


# Run the test
test_user_signup_valid()
