import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestMainPage():

    def test_check_add_to_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        add_to_basket_button = None
        try: # пытаемся найти нужную кнопку на странице
            browser.implicitly_wait(5)
            add_to_basket_button = browser.find_element(By.CSS_SELECTOR,
                                                        '[class="btn btn-lg btn-primary btn-add-to-basket"]')
        finally: # проверку заносим в этот блок, чтобы проверка произошла в любом случае
            assert add_to_basket_button.is_displayed(), print(f"ERROR: 'Add to basket button' is not displayed!")
            sleep(5)
