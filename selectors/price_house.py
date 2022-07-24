import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 12).until(
    expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button2 = browser.find_element(By.ID, "book")
button2.click()
value = browser.find_element(By.ID, "input_value")
number = calc(value.text)
in1 = browser.find_element(By.ID, "answer")
in1.send_keys(number)
button3 = browser.find_element(By.ID, "solve")
button3.click()