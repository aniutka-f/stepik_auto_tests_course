
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element(By.ID, "treasure")
    x = box.get_attribute("valuex")
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    option3 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    option3.click()

finally:
    time.sleep(30)
    browser.quit()

#jll
