import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)

check = browser.find_element(By.ID, "robotCheckbox")
check.click()

radio = browser.find_element(By.ID, "robotsRule")
radio.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
webdriver.Chrome().quit()
