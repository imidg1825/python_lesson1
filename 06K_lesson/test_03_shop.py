from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = "https://www.saucedemo.com/"


def create_driver() -> webdriver.Firefox:
    options = Options()

    # Не ждём "полную загрузку" — Firefox часто зависает на get()
    options.page_load_strategy = "none"

    # Убираем прокси/велком-страницы, которые мешают старту
    options.set_preference("network.proxy.type", 0)
    options.set_preference("browser.aboutwelcome.enabled", False)
    options.set_preference("browser.newtabpage.enabled", False)

    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(10)
    return driver


def open_url_stable(driver: webdriver.Firefox, wait: WebDriverWait, url: str) -> None:
    driver.get("about:blank")

    try:
        driver.get(url)
    except Exception:
        pass

    driver.execute_script("window.location.href = arguments[0];", url)

    # Ждём не URL, а реальный "якорь" страницы — поле логина
    wait.until(EC.presence_of_element_located((By.ID, "user-name")))


def test_shop_purchase_total():
    driver = None

    # Ретраи с пересозданием драйвера (иначе InvalidSessionId/NoSuchWindow)
    for attempt in range(2):
        try:
            driver = create_driver()
            wait = WebDriverWait(driver, 40)

            open_url_stable(driver, wait, URL)

            wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys(
                "standard_user"
            )
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()

            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
            )

            driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
            driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            wait.until(
                EC.presence_of_element_located((By.ID, "cart_contents_container"))
            )

            driver.find_element(By.ID, "checkout").click()
            wait.until(
                EC.presence_of_element_located((By.ID, "checkout_info_container"))
            )

            driver.find_element(By.ID, "first-name").send_keys("Иван")
            driver.find_element(By.ID, "last-name").send_keys("Петров")
            driver.find_element(By.ID, "postal-code").send_keys("123456")

            driver.find_element(By.ID, "continue").click()
            wait.until(
                EC.presence_of_element_located((By.ID, "checkout_summary_container"))
            )

            total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
            total_value = total_text.split("$")[-1].strip()

            assert total_value == "58.29", (
                f"Ожидали 58.29, получили {total_value} ({total_text})"
            )
            return

        except Exception:
            if attempt == 1:
                raise
        finally:
            if driver is not None:
                try:
                    driver.quit()
                except Exception:
                    pass
                driver = None
