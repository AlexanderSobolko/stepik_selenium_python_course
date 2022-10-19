import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_first_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first[required]')
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[required]')
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third[required]')
        input_email.send_keys("alexander.sobolko@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be text")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_first_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first[required]')
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[required]')
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third[required]')
        input_email.send_keys("alexander.sobolko@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be text")


if __name__ == "__main__":
    unittest.main()
