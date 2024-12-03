from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

# Path to Chrome User Data
user_data_dir = r"C:\Users\svenf\AppData\Local\Google\Chrome\User Data"
profile = "Profile 4"  # Replace with your profile folder name

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")  # Path to user data
chrome_options.add_argument(f"--profile-directory={profile}")  # Specific profile

# Path to ChromeDriver
driver_path = r"C:\Users\svenf\Ali\TradingServer\chromedriver.exe"  # Replace with your ChromeDriver path

# Initialize WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Variable to store the timestamp of the last printed alert
last_alert_time = None
last_alert_message = None  # Variable to store the last alert message

def get_latest_alert():
    try:
        # Wait for the alert log items to load
        alert_items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-name="alert-log-item"]'))
        )
        if alert_items:
            # Get the first (newest) alert item
            newest_alert_element = alert_items[0]
            alert_message = newest_alert_element.find_element(By.CLASS_NAME, "message-PQUvhamm").text
            
            # Extract the timestamp from the alert message (assuming it's always in this format)
            alert_timestamp_str = alert_message.split('@')[1].split('.')[0]  # "2024-11-26T08:04:00Z"
            alert_timestamp = datetime.strptime(alert_timestamp_str, "%Y-%m-%dT%H:%M:%SZ")

            # Check if the current alert's timestamp is newer than the last printed one
            global last_alert_time, last_alert_message
            if last_alert_time is None or alert_timestamp > last_alert_time:
                # Print the alert message
                print("\033[32m" + alert_message + "\033[0m")
                # Update the last_alert_time and last_alert_message with the current alert's data
                last_alert_time = alert_timestamp
                last_alert_message = alert_message
                return alert_message
            elif alert_message != last_alert_message:
                # If the message has changed but not the timestamp, print the new message
                print("\033[32m" + alert_message + "\033[0m")
                # Update the last_alert_message
                last_alert_message = alert_message
                return alert_message
            else:
                # If the message hasn't changed, notify that no new alert was printed
                print("\033[31mNo new alert message.\033[0m")
    except Exception as e:
        print("Error fetching alert:", e)
    return None

try:
    # Open the target page
    driver.get("https://www.tradingview.com/chart/494aE1o5/")

    # Wait for the "Log" tab button to be clickable and click it
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-name="light-tab-1"]'))
    ).click()

    # Main loop to continuously check for new alerts
    while True:
        get_latest_alert()
        # Wait for a few seconds before checking again (adjust as needed)
        time.sleep(5)

finally:
    # Close the browser
    driver.quit()
