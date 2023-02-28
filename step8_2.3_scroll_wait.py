
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

   
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book").click()

    browser.execute_script("window.scrollBy(0, 150);")

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button1.click()


finally:
    time.sleep(30)
    browser.quit()

#jll

   
