import unittest
from selenium import webdriver
import time


linkSite_1 = "http://suninjuly.github.io/registration1.html"
linkSite_2 = "http://suninjuly.github.io/registration2.html"


class TestAbs(unittest.TestCase):
    def test_firstLink(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(linkSite_1)
            firstname = browser.find_element_by_css_selector('body>div>form>div.first_block>'
                                                             'div.form-group.first_class>input')
            firstname.send_keys('John')

            # находим поле last name
            lastname = browser.find_element_by_css_selector('body>div>form>div.first_block>'
                                                            'div.form-group.second_class>input')
            lastname.send_keys('Snow')

            # находим поле email
            emailfield = browser.find_element_by_css_selector('body>div>form>div.first_block>div.'
                                                              'form-group.third_class>input')
            emailfield.send_keys('test@test.com')

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            time.sleep(1)

        finally:
            text_succes = browser.find_element_by_css_selector('.container>h1')
            text_succes = text_succes.text
            self.assertEqual(text_succes, "Congratulations! You have successfully registered!",
                             "не осуществился переход на конечную страницу")
            browser.quit()

    def test_secondLink(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(linkSite_2)
            firstname = browser.find_element_by_css_selector('body>div>form>div.first_block>'
                                                             'div.form-group.first_class>input')
            firstname.send_keys('John')

            # находим поле last name
            lastname = browser.find_element_by_css_selector('body>div>form>div.first_block>'
                                                            'div.form-group.second_class>input')
            lastname.send_keys('Snow')

            # находим поле email
            emailfield = browser.find_element_by_css_selector('body>div>form>div.first_block>'
                                                              'div.form-group.third_class>input')
            emailfield.send_keys('test@test.com')

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            time.sleep(1)

        finally:
            text_succes = browser.find_element_by_css_selector('.container>h1').text()
            self.assertEqual(text_succes, "Congratulations! You have successfully registered!",
                             "не осуществился переход на конечную страницу")
            browser.quit()


if __name__ == "__main__":
    unittest.main()
