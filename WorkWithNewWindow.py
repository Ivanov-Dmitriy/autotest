from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


linkSite = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(linkSite)

    jumpBtn = browser.find_element_by_css_selector('.trollface.btn')
    # jumpBtn.sleep(2)
    jumpBtn.click()

    secondWindow = browser.window_handles[1]
    firstWindow = browser.window_handles[0]
    browser.switch_to.window(secondWindow)

    print('!!!!!!name for second tab', secondWindow)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    print(y, ' - значение формулы')

    inputField = browser.find_element_by_css_selector('#answer')
    inputField.send_keys(y)

    btnSubmit = browser.find_element_by_css_selector('.btn')
    btnSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
