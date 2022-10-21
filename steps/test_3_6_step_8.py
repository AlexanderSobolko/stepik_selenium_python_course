import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_1(browser):

    browser.get("http://selenium1py.pythonanywhere.com")
    time.sleep(3)
