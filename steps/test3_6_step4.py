import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mas = []


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    print(mas)
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_1(browser, link):

    browser.get(link)

    textarea = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                                "textarea.ember-text-area")))
    answer = math.log(int(time.time()))
    textarea.send_keys(answer)

    submit_button = browser.find_element(By.CLASS_NAME, "submit-submission")
    submit_button.click()

    hint = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))
    text = hint.text
    print(text)
    mas.append(text)
    assert text == "Correct!", "Text should be even Correct!"
