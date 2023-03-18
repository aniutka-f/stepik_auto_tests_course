
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button1.click()

finally:
    time.sleep(6)
    browser.quit()

#jll
