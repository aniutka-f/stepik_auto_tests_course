
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select



try:
   

browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

finally:
    time.sleep(5)
    browser.quit()

#jll
