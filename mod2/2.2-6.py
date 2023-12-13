import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

browser.find_element(By.ID, "answer").send_keys(y)

check = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", check)
check.click()

browser.find_element(By.ID, "robotsRule").click()
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(5)
webdriver.Chrome().quit()
