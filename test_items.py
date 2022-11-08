import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_get_correct_feedback(browser):

    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    text_check_buttom = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "btn-add-to-basket"))
    ).text
    print("ТУТ!!!!" + text_check_buttom)
    time.sleep(5)
    assert text_check_buttom != 0, "На странице отсутствует кнопка 'Добавить в корзину'"
