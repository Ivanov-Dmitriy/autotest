from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


# формула подсчета указанной на сайте функции (изначально спрятанный элемент, появляется после нажатия на батон book)
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome('/Users/dmitrijivanov/Downloads/chromedriver')
linkSite = 'http://suninjuly.github.io/explicit_wait2.html'


try:
    # открываем браузер в фулскрин
    browser.maximize_window()
    # открываем ссылку, указанную в переменной linkSite
    browser.get(linkSite)

    bookBtn = browser.find_element_by_css_selector('#book')
    # !*!*!*!
    inputField = browser.find_element_by_css_selector('#answer')
    """Даем браузеру 12 секунд на то, чтобы записать в переменную значение элемента, 
    когда оно будет=$100 (число динамическое)"""
    priceValue = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    bookBtn.click()
    # скролим пейдж до тех пор, пока он не будет вверху страницы (насколько это возможно)
    browser.execute_script("return arguments[0].scrollIntoView(true);", inputField)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    inputField.send_keys(y)

    submitBtn = browser.find_element_by_css_selector('#solve').click()

finally:
    time.sleep(6)
    browser.quit()
