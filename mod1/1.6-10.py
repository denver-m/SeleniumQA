from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elementList = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    for element in elementList:
        element.send_keys("1")

    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    webdriver.Chrome().quit()