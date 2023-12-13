from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elementList = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elementList:
        element.send_keys("1")

    inputBtn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    inputBtn.click()

finally:
    time.sleep(30)
    webdriver.Chrome().quit()
