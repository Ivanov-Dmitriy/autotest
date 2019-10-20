import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome('/Users/dmitrijivanov/autotest/chromedriver')
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_guest_should_see_login_link(browser):  # dopisat ,links
    # link = f"{links}/"
    browser.get('https://stepik.org/lesson/236895/step/1')
    input_filed = browser.find_element_by_css_selector(".textarea")
    answer = math.log(int(time.time()))
    input_filed.send_keys(answer)

    '''btn_submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    btn_submit.click()

    feedback_mes = browser.find_element_by_css_selector('smart-hints__hint')
    feedback_mes = feedback_mes.text
    assert feedback_mes == "Correct!"'''
