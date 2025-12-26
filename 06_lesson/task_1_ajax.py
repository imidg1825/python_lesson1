from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:
    driver.get("http://uitestingplayground.com/ajax")

    # 1) нажимаем на синюю кнопку
    driver.find_element(By.ID, "ajaxButton").click()

    # 2) ждём, пока появится нужный элемент с текстом
    message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content p.bg-success"))
    )

    # 3) дополнительно ждём, пока текст станет НЕ пустым
    wait.until(lambda d: message.text.strip() != "")

    # 4) выводим текст в консоль
    print(message.text)

finally:
    driver.quit()
