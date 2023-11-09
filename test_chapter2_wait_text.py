from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.ID, "book")
    wait = WebDriverWait(browser, 20)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    value_x = int(browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text)
    y = calc(value_x)
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()