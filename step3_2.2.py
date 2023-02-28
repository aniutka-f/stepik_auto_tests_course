from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    c = str(int(x) + int(y))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)

    option = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    option.click()
finally:
    time.sleep(5)
    browser.quit()

#jll
