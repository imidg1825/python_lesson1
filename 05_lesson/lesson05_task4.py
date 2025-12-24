from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

message = driver.find_element(By.ID, "flash").text
print(message)

time.sleep(2)

driver.quit()
