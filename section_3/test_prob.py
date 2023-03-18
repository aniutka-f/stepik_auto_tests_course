from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



link = "https://stepik.org/lesson/236895/step/1"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.ID,"ember33").click()
    time.sleep(5)


    input1 = browser.find_element(By.NAME, "login")
    input1.send_keys("anya.bondarenko.95@yandex.ru")
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys("1219nljko78d")
    time.sleep(5)
    button1 = browser.find_element(By.CSS_SELECTOR,'[class="sign-form__btn button_with-loader "]')
    button1.click()
    time.sleep(5)

    input3 = browser.find_element(By.ID,"ember91")
    input3.send_keys(str(math.log(int(time.time()))))
    time.sleep(5)
    button2 = browser.find_element(By.CSS_SELECTOR, '[class="submit-submission"]').click()
    time.sleep(10)




finally:
    browser.quit()