from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

input = browser.find_element(By.ID, "input_value")
x = input.text
fn = str(math.log(abs(12*math.sin(int(x)))))

input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
input_answer.send_keys(fn)

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()
