from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    text_field_name = browser.find_element(By.CSS_SELECTOR, '[name=firstname]')
    text_field_name.send_keys("Ivan")
    text_field_last_name = browser.find_element(By.CSS_SELECTOR, '[name=lastname]')
    text_field_last_name.send_keys("Ivanov")
    text_field_email = browser.find_element(By.CSS_SELECTOR, '[name=email]')
    text_field_email.send_keys("test@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test_file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
