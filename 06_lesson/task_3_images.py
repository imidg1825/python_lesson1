from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # 1) ждём, пока на странице появятся все картинки (их 4)
    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) == 4)

    images = driver.find_elements(By.TAG_NAME, "img")

    # 2) ждём, пока у КАЖДОЙ картинки появится src
    for image in images:
        wait.until(lambda d: image.get_attribute("src") != "")

    # 3) берём третью картинку (индекс 2)
    third_image_src = images[2].get_attribute("src")

    # 4) выводим src в консоль
    print(third_image_src)

finally:
    driver.quit()
