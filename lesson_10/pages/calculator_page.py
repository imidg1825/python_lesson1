from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds: str):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(seconds)

    def press_button(self, value: str):
        btn = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        btn.click()

    def get_result(self, timeout: int = 70) -> str:
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*self.screen).text == "15"
        )
        return self.driver.find_element(*self.screen).text
