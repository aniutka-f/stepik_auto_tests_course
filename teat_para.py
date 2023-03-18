import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1"])

class TestMainPage1():
    def test_click(self, browser, links):
        link = links
        browser.get(link)
        time.sleep(5)
        # exit(1)

        button = browser.find_element(By.ID, "ember33")
        button.click()
        input1 = browser.find_element(By.NAME, "login")
        input1.send_keys("anya.bondarenko.95@yandex.ru")
        input2 = browser.find_element(By.NAME, "password")
        input2.send_keys("1219nljko78d")
        time.sleep(1)
        button1 = browser.find_element(By.CSS_SELECTOR, '[class="sign-form__btn button_with-loader "]')
        button1.click()
        time.sleep(10)

        answer = str(math.log(int(time.time())))
        input_for_answer = browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')
        input_for_answer.send_keys(answer)

        button2 = browser.find_element(By.CSS_SELECTOR, '[class="submit-submission"]')
        button2.click()
        time.sleep(10)
        find_answer = browser.find_element(By.CSS_SELECTOR, '[class="smart-hints__hint"]').text
        text_find = "Correct!"
        assert find_answer == text_find, "ERR"

        if __name__ == "__main__":
            pytest.main()



