from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


linkSite = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

bookBtn = WebDriverWait(browser, 12).until(
    EC.element_selection_state_to_be('#price', 100)
)