from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

alert = browser.switch_to.alert
# нажать кнопку ОК в окне alert или confirm
alert.accept()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(5)
webdriver.Chrome().quit()