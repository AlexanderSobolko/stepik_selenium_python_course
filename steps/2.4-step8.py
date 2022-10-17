from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button1 = browser.find_element(By.ID, "book")
    button1.click()

    input = browser.find_element(By.ID, "input_value")
    x = input.text
    print(x)
    fn = str(math.log(abs(12 * math.sin(int(x)))))
    print(fn)

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(fn)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
