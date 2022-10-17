from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input = browser.find_element(By.ID, "input_value")
    x = input.text
    fn = str(math.log(abs(12 * math.sin(int(x)))))

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(fn)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
