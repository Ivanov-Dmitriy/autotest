from selenium import webdriver
import time
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


linkSite = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(linkSite)

    btnBlue = browser.find_element_by_css_selector('.btn')
    btnBlue.click()

    confirmWindow = browser.switch_to.alert
    confirmWindow.accept()

    time.sleep(1)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    inputField = browser.find_element_by_css_selector('#answer')
    inputField.send_keys(y)

    btnSubmit = browser.find_element_by_css_selector('.btn')
    btnSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
