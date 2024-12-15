from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver (Replace with your WebDriver if not using Chrome)
driver = webdriver.Edge()  # Ensure ChromeDriver is installed and accessible

# Step 1: Navigate to the home page
driver.get("https://the-internet.herokuapp.com/")
print("Website loaded successfully!")

# Step 2: Test the Login Form
try:
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()  # Navigate to the Login page
    time.sleep(2)  # Allow time for the page to load

    driver.find_element(By.ID, "username").send_keys("tomsmith")  # Enter username
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")  # Enter password
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Click Login

    # Validate login success
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
    print(f"Login Success Message: {success_message}")
except Exception as e:
    print(f"Error testing login form: {e}")

# Step 3: Interact with Checkboxes
try:
    driver.get("https://the-internet.herokuapp.com/checkboxes")  # Navigate to Checkboxes page
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    for index, checkbox in enumerate(checkboxes, start=1):
        if not checkbox.is_selected():
            checkbox.click()
            print(f"Checkbox {index} selected.")
        else:
            print(f"Checkbox {index} was already selected.")
except Exception as e:
    print(f"Error interacting with checkboxes: {e}")

# Step 4: Interact with Dropdowns
try:
    driver.get("https://the-internet.herokuapp.com/dropdown")  # Navigate to Dropdown page
    dropdown = Select(driver.find_element(By.ID, "dropdown"))  # Locate the dropdown
    dropdown.select_by_visible_text("Option 1")  # Select Option 1
    print("Dropdown Option 1 selected.")
    dropdown.select_by_visible_text("Option 2")  # Select Option 2
    print("Dropdown Option 2 selected.")
except Exception as e:
    print(f"Error interacting with dropdown: {e}")

# Step 5: Handle JavaScript Alerts
try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")  # Navigate to JavaScript Alerts page

    # Test JS Alert
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    print(f"JS Alert Text: {alert.text}")
    alert.accept()  # Accept the alert

    # Test JS Confirm
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    confirm = driver.switch_to.alert
    print(f"JS Confirm Text: {confirm.text}")
    confirm.dismiss()  # Dismiss the confirm alert

    # Test JS Prompt
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    prompt = driver.switch_to.alert
    print(f"JS Prompt Text: {prompt.text}")
    prompt.send_keys("Testing Prompt")  # Send text to the prompt
    prompt.accept()  # Accept the prompt
except Exception as e:
    print(f"Error handling JavaScript alerts: {e}")

# Close the browser after completing the tests
driver.quit()
print("Test completed!")