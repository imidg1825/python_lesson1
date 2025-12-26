from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://uitestingplayground.com/textinput")

    # 1) вводим SkyPro в поле
    input_field = wait.until(EC.element_to_be_clickable((By.ID, "newButtonName")))
    input_field.clear()
    input_field.send_keys("SkyPro")

    # 2) жмём на синюю кнопку
    button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    button.click()

    # 3) ждём, пока текст кнопки станет "SkyPro"
    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))

    # 4) выводим текст кнопки в консоль
    print(button.text)

finally:
    driver.quit()
