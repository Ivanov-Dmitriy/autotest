from selenium import webdriver
import time
import os

linkSite = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(linkSite)

    fName = browser.find_element_by_css_selector('[name="firstname"]')
    fName.send_keys('Jerome')

    sName = browser.find_element_by_css_selector('[name="lastname"]')
    sName.send_keys('Pele')

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('testio@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

    attachFile  = browser.find_element_by_css_selector('#file')
    attachFile.send_keys(file_path)

    btnSubmit = browser.find_element_by_css_selector('.btn')
    btnSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()