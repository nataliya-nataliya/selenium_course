from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value = browser.find_element(By.ID, "treasure")
    number = value.get_attribute("valuex")
    res = calc(number)
    in1 = browser.find_element(By.ID, "answer")
    in1.send_keys(res)
    in2 = browser.find_element(By.ID, "robotCheckbox")
    in2.click()
    in3 = browser.find_element(By.ID, "robotsRule")
    in3.click()
    in4 = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    in4.click()

finally:
    time.sleep(10)
    browser.quit()
