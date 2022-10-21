from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get("https://stepik.org/lesson/25969/step/8")
