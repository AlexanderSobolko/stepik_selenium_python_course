from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input = browser.find_element(By.ID, "input_value")
    x = input.text
    print(x)
    fn = str(math.log(abs(12 * math.sin(int(x)))))
    print(fn)

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(fn)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
