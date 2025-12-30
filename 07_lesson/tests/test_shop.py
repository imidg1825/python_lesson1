import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture()
def driver():
    driver_ = webdriver.Firefox()
    driver_.maximize_window()
    yield driver_
    driver_.quit()


def test_shop_total(driver):
    # 1) Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 2) Add products + go to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_products()
    inventory_page.go_to_cart()

    # 3) Checkout (cart page)
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # 4) Fill form + Continue (checkout: your info)
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form(first_name="Ivan", last_name="Ivanov", postal_code="123456")
    checkout_page.click_continue()

    # 5) Assert Total on overview page
    total_text = checkout_page.get_total()
    assert "$58.29" in total_text, f"Ожидали Total $58.29, получили: {total_text}"
