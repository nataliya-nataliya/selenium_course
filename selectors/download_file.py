from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    in1 = browser.find_element(By.NAME, "firstname")
    in1.send_keys("Ivanov")
    in2 = browser.find_element(By.NAME, "lastname")
    in2.send_keys("Ivan")
    in3 = browser.find_element(By.NAME, "email")
    in3.send_keys("a@a.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element =  browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    button.click()
finally:
    time.sleep(10)
    browser.quit()



