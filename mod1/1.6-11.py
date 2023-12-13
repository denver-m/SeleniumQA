# окружение: macOS, PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # тест падает с ошибкой если заменить в ссылке registration1 на registration2
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
    input1.send_keys("1")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
    input2.send_keys("2")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
    input3.send_keys("3")

    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    webdriver.Chrome().quit()