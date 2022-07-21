from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element(By.ID, "input_value")
    number = value.text
    res = calc(number)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    in1 = browser.find_element(By.ID, "answer")
    in1.send_keys(res)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    in2 = browser.find_element(By.ID, "robotCheckbox")
    in2.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    in3 = browser.find_element(By.ID, "robotsRule")
    in3.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()



