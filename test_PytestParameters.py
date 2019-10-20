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


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links):
    link = f"{links}/"
    browser.get(link)
    time.sleep(4)
    input_filed = browser.find_element_by_css_selector(".textarea.ember-text-area.ember-view")

    answer = math.log(int(time.time()))
    t_text = str(answer)
    input_filed.send_keys(t_text)

    btn_submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    btn_submit.click()

    time.sleep(1)
    feedback_mes = browser.find_element_by_css_selector('.smart-hints__feedback.hints__component.'
                                                        'hints__component_showed.ember-view>.smart-hints__hint')
    feedback_mes = feedback_mes.text
    assert feedback_mes == "Correct!"
