import pytest
from selenium import webdriver

from pages.calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator_sum(driver):
    page = CalculatorPage(driver)

    page.open()
    page.set_delay("45")

    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")

    result = page.get_result()
    assert result == "15"
