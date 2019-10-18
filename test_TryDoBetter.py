import unittest
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)


def registration(url):
    browser.get(url)

    fname_field = browser.find_element_by_css_selector('body>div>form>div.first_block>'
                                                       'div.form-group.first_class>input')
    fname_field.send_keys('John')
    lname_field = browser.find_element_by_css_selector('body>div>form>div.first_block>'
                                                       'div.form-group.second_class>input')
    lname_field.send_keys('Lebovski')
    email_field = browser.find_element_by_css_selector('body>div>form>div.first_block>div.'
                                                       'form-group.third_class>input')
    email_field.send_keys('lebovski@test.com')

    # отправляем заполненую форму
    button_send = browser.find_element_by_css_selector('button.btn')
    button_send.click()

    # проверяем, что смогли зарегистрироваться
    time.sleep(1)

    text_succes = browser.find_element_by_css_selector('.container>h1')
    # обновляем переменную, записываем в переменную только текст элемента
    text_succes = text_succes.text

    return text_succes


class TestRun(unittest.TestCase):
    def test_url1(self):
        url = 'http://suninjuly.github.io/registration1.html'
        # вызываем проверку, что параметр "text_succes" == 2-му параметру
        self.assertEqual("Congratulations! You have successfully registered!", registration(url),
                         "should be message of success registration")

    def test_url2(self):
        # другой url
        try:
            url = 'http://suninjuly.github.io/registration2.html'
            # вызываем проверку, что параметр "text_succes" == 2-му параметру
            self.assertEqual("Congratulations! You have successfully registered!", registration(url),
                             "should be message of success registration")

        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
