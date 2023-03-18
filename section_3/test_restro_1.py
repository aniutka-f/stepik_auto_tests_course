

from selenium import webdriver
import time


link = "http://www.ubudcare.com/appointment"

try:
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    time.sleep(10)
    browser.quit()


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()




# class TestMainPage1():
#     def test_click(self, browser):
#         link = "http://18.181.182.224/auth"
#         browser.get(link)
#         time.sleep(5)
#
#     if __name__ == "__main__":
#         pytest.main()