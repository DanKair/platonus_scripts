# Grade Scraper From Platonus
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv


# Loading data from .env file
load_dotenv()
user_login = os.getenv("LOGIN")
user_password = os.getenv("PASSWORD")
grade_url = os.getenv("GRADE_URL")
# screenshot_folder = os.getenv("TARGET_FOLDER")

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the login page
driver.get("https://platonus.iitu.edu.kz/")

# Find and fill the username field
username_field = driver.find_element(By.NAME, "login")
username_field.send_keys(user_login)

# Find and fill the password field
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(user_password)

# Find and click the login button
login_button = driver.find_element(By.ID, "Submit1")
login_button.click()

time.sleep(2)

# Go To Grade field

driver.get(grade_url)
time.sleep(2)


os.getcwd() # If you don't know path, uncomment this
if not os.path.exists("screenshots"):
    os.mkdir("screenshots")
os.chdir("screenshots")

# Capture screenshot to "screenshot" folder and save it
driver.save_screenshot("grades1.png")

driver.execute_script("window.scrollBy(0, 600)") # Scroll down to 600 pixels
time.sleep(1)
driver.save_screenshot("grades2.png")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.save_screenshot("grades3.png")
time.sleep(2)

# Or You can save it to folder of your choice by changing to it:
# os.chdir(screenshot_folder)
# driver.save_screenshot("grades1.png")
#
# driver.execute_script("window.scrollBy(0, 600)") # Scroll down to 600 pixels
# time.sleep(1)
# driver.save_screenshot("grades2.png")
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(1)
# driver.save_screenshot("grades3.png")
# time.sleep(2)

# Close the browser
driver.quit()