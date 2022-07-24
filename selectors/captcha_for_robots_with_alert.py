from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/alert_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)

  button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button1.click()
  confirm = browser.switch_to.alert
  browser.switch_to.window(browser.window_handles[0])
  confirm.accept()
  value = browser.find_element(By.ID, "input_value")
  number = calc(value.text)
  in1 = browser.find_element(By.ID, "answer")
  in1.send_keys(number)
  button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button2.click()


finally:
    time.sleep(10)
    browser.quit()