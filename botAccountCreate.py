import random
from tkinter.tix import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import time
import argparse

parser = argparse.ArgumentParser()

# Connect to the Selenium server
options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

#saves the login & pass into accounts.txt file.
acc = open("accounts.txt", "a")

name = account.username()

# Visit Instagram's homepage
driver.get("https://www.instagram.com")
time.sleep(5)

# Wait for the page to load
driver.implicitly_wait(10)  # Waits up to 10 seconds

# Locate and click the anchor tag with the href "/accounts/emailsignup/?"
try:
    signup_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/accounts/emailsignup/"]')
    signup_link.click()
    print("Navigated to the signup page.")
except Exception as e:
    print("Could not find the signup link:", e)


#Fill the email value
email_field = driver.find_element_by_name('emailOrPhone')
fake_email = email.getFakeMail()
email_field.send_keys(fake_email)
print(fake_email)

# Fill the fullname value
fullname_field = driver.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())

# Fill username value
username_field = driver.find_element_by_name('username')
username_field.send_keys(name)
print(name)

# Fill password value
password_field = driver.find_element_by_name('password')
acc_password = account.generatePassword()
password_field.send_keys(acc_password) # You can determine another password here.

print(name+":"+acc_password, file=acc)

acc.close()

sign_up_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up' and @type='submit']"))
    )
sign_up_button.click()
time.sleep(8)

# Generate a random date before 2004
year = random.randint(1980, 2003)  # Random year between 1900 and 2003
month = random.randint(1, 12)  # Random month between 1 and 12
# Days vary based on the month
if month in [1, 3, 5, 7, 8, 10, 12]:
    day = random.randint(1, 31)  # 31 days in these months
elif month == 2:
    # Check for leap year to determine the number of days in February
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        day = random.randint(1, 29)  # 29 days in February if leap year
    else:
        day = random.randint(1, 28)  # 28 days in February if not leap year
else:
    day = random.randint(1, 30)  # 30 days in these months

print(f"Selected random date: {month}/{day}/{year}")

try:
    # Wait for the month dropdown to be present and select a value
    month_dropdown = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "select[title='Month:']"))
    )
    month_select = Select(month_dropdown)
    month_select.select_by_value(str(month))  # Change to desired month

    # Wait for the day dropdown to be present and select a value
    day_dropdown = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "select[title='Day:']"))
    )
    day_select = Select(day_dropdown)
    day_select.select_by_value(str(day))  # Change to desired day

    # Wait for the year dropdown to be present and select a value
    year_dropdown = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "select[title='Year:']"))
    )
    year_select = Select(year_dropdown)
    year_select.select_by_value(str(year))  # Change to desired year

    print("Selected random date of birth.")

except Exception as e:
    print(f"An error occurred: {e}")
    
    
next_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Next' and @type='button']"))
    )
next_button.click()
time.sleep(3)
#
fMail = fake_email[0].split("@")
mailName = fMail[0]
domain = fMail[1]
instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
time.sleep(10)

#accepting the notifications.
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(2)

#logout
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div").click()

try:
    not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
    if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
      time.sleep(1)
      driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
      time.sleep(10)
      instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
      confInput = driver.find_element_by_name('email_confirmation_code')
      confInput.send_keys(Keys.CONTROL + "a")
      confInput.send_keys(Keys.DELETE)
      confInput.send_keys(instCodeNew, Keys.ENTER)
except:
      pass

time.sleep(5)
driver.quit()
