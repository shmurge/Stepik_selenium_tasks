import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestMainPage():

    def test_check_add_to_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        add_to_basket_button = False
        try:
            browser.implicitly_wait(5)
            add_to_basket_button = browser.find_element(By.CSS_SELECTOR,
                                                        '[class="btn btn-lg btn-primary btn-add-to-basket"]').is_displayed()
        finally:
            assert add_to_basket_button is True, print(f"ERROR: 'Add to basket button' is not displayed!")
            sleep(5)
