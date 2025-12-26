from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

time.sleep(2)

driver.quit()
