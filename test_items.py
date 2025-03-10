import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_btn(browser):
    browser.get(link)
    time.sleep(30)
    try:
        addToCart_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    except Exception as e:
        pytest.fail(f'Кнопка "Добавить в корзину" не найдена на странице. Ошибка: {e}')
    assert addToCart_button.is_displayed(), 'Кнопка "Добавить в корзину" не отображается на странице'
    