import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test3213(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
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

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "нет")

    def test_2(self):
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

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "нет")


if __name__ == "__main__":
    unittest.main()
