import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = "https://lovely-genie-b5af1b.netlify.app/"

@pytest.mark.smoke
@pytest.mark.parametrize('option', ["default", "private"])
class TestMain:
    def test_create_todo(self, browser, option):
        browser.get(link)
        print(option)
        add_todo = browser.find_element(By.CSS_SELECTOR, '[data-testid="input_content"]')
        add_todo.send_keys("123 " + option)
        button_add = browser.find_element(By.CSS_SELECTOR, '[data-testid="add_todo"]')
        is_button_disabled = button_add.get_attribute("disabled")
        print("value of button - disabled: ", is_button_disabled)
        assert is_button_disabled is not None, "Button not disabled"
        option_element = browser.find_element(By.XPATH, '//div[@class="options"]//span[@class="bubble ' + option + '"]')
        option_element.click()
        button_add.click()
        input_text = browser.find_element(By.CSS_SELECTOR, '[class = "todo-content"]')
        input_text_value = input_text.get_attribute("value")
        time.sleep(3)
        print("value of input:", input_text_value)
        # этот тест запустится 2 раза

# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# class TestLogin:
#     def test_create_todo(self, browser, option):
#         browser.get(link)
#         print(option)
#         add_todo = browser.find_element(By.CSS_SELECTOR, '[data-testid="input_content"]')
#         add_todo.send_keys("123")
#         button_add = browser.find_element(By.CSS_SELECTOR, '[data-testid="add_todo"]')
#         is_button_disabled = button_add.get_attribute("disabled")
#         print("value of button - disabled: ", is_button_disabled)
#         assert is_button_disabled is not None, "Button not disabled"
#         option_element = browser.find_element(By.XPATH, '//div[@class="' + option +'"]//span')
#         option_element.click()
#         button_add.click()
#         input_text = browser.find_element(By.CSS_SELECTOR, '[class = "todo-content"]')
#         input_text_value = input_text.get_attribute("value")
#         time.sleep(30)
#         print("value of input:", input_text_value)
#
#
#
#
#     def test_right_values(self, browser):
#         browser.get(link)
#         add_todo = browser.find_element(By.CSS_SELECTOR, '[data-testid="input_content"]')
#         add_todo.send_keys("123")
#         button_add = browser.find_element(By.CSS_SELECTOR, '[data-testid="add_todo"]')
#         is_button_disabled = button_add.get_attribute("disabled")
#         print("value of button - disabled: ", is_button_disabled)
#         assert is_button_disabled is not None, "Button not disabled"
#         option_element = browser.find_element(By.XPATH, '//div[@class="options"]//span[2]')
#         option_element.click()
#         button_add.click()
#         input_text = browser.find_element(By.CSS_SELECTOR, '[class = "todo-content"]')
#         input_text_value = input_text.get_attribute("value")
#         print("value of input:", input_text_value)
#
#
# #end