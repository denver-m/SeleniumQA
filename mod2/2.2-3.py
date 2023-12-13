from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, "num1")
num1 = num1.text

num2 = browser.find_element(By.ID, "num2")
num2 = num2.text

summ = int(num1) + int(num2)

sel = Select(browser.find_element(By.TAG_NAME, "select"))
sel.select_by_value(str(summ))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
webdriver.Chrome().quit()
