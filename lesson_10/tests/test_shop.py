import allure
import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.step("Проверяем, что Total содержит ожидаемую сумму: {expected_total}")
def assert_total_is_correct(total_text: str, expected_total: str) -> None:
    """
    Проверяет, что строка Total содержит ожидаемую сумму.

    Args:
        total_text: Текст Total со страницы (например, 'Total: $58.29').
        expected_total: Ожидаемая сумма (например, '$58.29').

    Returns:
        None
    """
    assert (
        expected_total in total_text
    ), f"Ожидали Total {expected_total}, получили: {total_text}"


@pytest.fixture()
def driver():
    """
    Создает Firefox WebDriver и закрывает его после теста.

    Yields:
        webdriver.Firefox: Экземпляр драйвера.
    """
    driver_ = webdriver.Firefox()
    driver_.maximize_window()
    yield driver_
    driver_.quit()


@allure.title("Покупка в магазине: проверка итоговой суммы")
@allure.description(
    "Сценарий: логин → добавление товаров → корзина → checkout → ввод данных покупателя → проверка Total."
)
@allure.feature("Shop / Checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(driver) -> None:
    """
    E2E тест: оформление заказа с проверкой итоговой суммы.

    Args:
        driver: Selenium WebDriver (фикстура).

    Returns:
        None
    """
    with allure.step("1) Логин"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("2) Добавляем товары и переходим в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_products()
        inventory_page.go_to_cart()

    with allure.step("3) Переходим к оформлению заказа из корзины"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("4) Заполняем данные покупателя и продолжаем"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form(
            first_name="Ivan", last_name="Ivanov", postal_code="123456"
        )
        checkout_page.click_continue()

    with allure.step("5) Получаем Total"):
        total_text = checkout_page.get_total()

    assert_total_is_correct(total_text=total_text, expected_total="$58.29")
