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
screenshot_folder = os.getenv("TARGET_FOLDER")

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

time.sleep(3)

# Go To Grade field

driver.get(grade_url)
time.sleep(3)

# Capture screenshot and save it to a file
# driver.save_screenshot("grades.png") # Saves screenshot to the current working directory

# Or You can save it to folder of your choice by changing to it:
os.chdir(screenshot_folder)
driver.save_screenshot("grades.png")
time.sleep(3)

# Close the browser
driver.quit()