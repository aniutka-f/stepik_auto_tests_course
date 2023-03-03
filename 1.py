import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def test_welcome_text(link):


    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys("mail")
    time.sleep(1)
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    time.sleep(1)
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    time.sleep(1)

    time.sleep(1)    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться

    # ждем загрузки страницы

    time.sleep(3)

    # находим элемент, содержащий текст

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    # записываем в переменную welcome_text текст из элемента welcome_text_elt

    welcome_text = welcome_text_elt.text

    return welcome_text


class TestAbs(unittest.TestCase):

    def test_link1(self):
        welcome_text_link1 = test_welcome_text(link1)

        self.assertEqual(welcome_text_link1, "Congratulations! You have successfully registered!", "no_ok")

    def test_link2(self):
        welcome_text_link1 = test_welcome_text(link2)

        self.assertEqual(welcome_text_link1, "Congratulations! You have successfully registered!", "no_ok")


if __name__ == "__main__":
    unittest.main()