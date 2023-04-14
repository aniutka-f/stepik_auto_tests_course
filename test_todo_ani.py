import time
from selenium.webdriver.common.by import By
import pytest

link = "https://lovely-genie-b5af1b.netlify.app/"

info_errors = []


# 1) Позже. Одна точка входа для нескольких файлов (test.py -> )
# Проверка пустой ли список изначально; Взять id созданного todo

def create_todo(browser, type_todo):
    browser.get(link)

    input_text_todo = browser.find_element(By.CSS_SELECTOR, '[data-testid="input_content"]')
    button_add_todo = browser.find_element(By.CSS_SELECTOR, '[data-testid="add_todo"]')
    radio_type_todo = browser.find_element(By.XPATH, '//div[@class="options"]//span[@class="bubble ' + type_todo + '"]')

    init_todo_text = "type = " + type_todo

    def is_disabled_button():
        return button_add_todo.get_attribute("disabled")  # True or False

    if not is_disabled_button():
        print("button isnt disabled")

    input_text_todo.send_keys(init_todo_text)

    if not is_disabled_button():
        print("button isnt disabled")

    radio_type_todo.click()

    if is_disabled_button():
        print("button disabled")

    button_add_todo.click()

    # проверяем что текст в туду соответствует заведенному
    text_todo = browser.find_element(By.XPATH, '//section[@class="space-column"]//input[@class="todo-content"]')
    check_type = browser.find_element(By.XPATH, '//section[@class="space-column"]//span')

    text_todo_value = text_todo.get_attribute("value")

    if text_todo_value == init_todo_text:
        print("Its true")

    # Проверияем, что тип туду соответсвует заведенному
    check_type_class = check_type.get_attribute('class')
    type_point = bool(check_type_class.find(type_todo))
    print(type_point)


def check_missing_buttons(browser):  # Проверка отсутствия кнопок Clear all & Hide
    button_clear_all = browser.find_elements(By.CSS_SELECTOR, '[data-testid="clear_all"]')
    button_hide = browser.find_elements(By.CSS_SELECTOR, '[data-testid="change_visible"]')

    if button_clear_all or button_hide:
        print("Присутствует ненужная кнопка")


def editing(browser):
    # редактируем и проверка редактирования
    input_editing = browser.find_element(By.XPATH, "//section[@class='space-column']//input[@type='text']")
    input_editing_text = input_editing.get_attribute("value")
    input_editing.click()
    input_editing.send_keys("editing")
    value_ed = input_editing_text + "editing"
    input_editing_1 = browser.find_element(By.XPATH, "//section[@class='space-column']//input[@type='text']")
    input_editing_text_1 = input_editing_1.get_attribute("value")
    if value_ed in input_editing_text_1:
        print("right ed")


@pytest.mark.smoke
class TestMain:
    def test_init(self, browser):
        check_missing_buttons(browser)

        # создаем туду пункты
        create_todo(browser, 'default')

        editing(browser)  # редактируем и проверка редактирования
        input_text_todo = browser.find_element(By.XPATH, "//section[@class='space-column']//span")  # выполнено

        input_text_todo.click()
        # удалить пункт туду
        input_delete = browser.find_element(By.CSS_SELECTOR, '[data-testid = "delete"]')
        input_delete.click()
        # создать доп туду пункты
        create_todo(browser, 'default')
        create_todo(browser, 'private')
        # Отображается название кнопки Hide
        button_hide = browser.find_element(By.CSS_SELECTOR, '[data-testid="change_visible"]')
        str_hide_text = button_hide.text
        if "Hide" in str_hide_text:
            print(True)

        # Нажать на Hide
        button_hide.click()
        # Создаем новый туду
        input_text_todo = browser.find_element(By.CSS_SELECTOR, '[data-testid="input_content"]')
        input_text_todo.send_keys("111")
        radio_type_todo = browser.find_element(By.XPATH, '//div[@class="options"]//span')
        radio_type_todo.click()
        button_add = browser.find_element(By.CSS_SELECTOR, '[data-testid="add_todo"]')
        button_add.click()
        # Проверка, что пунктов туду нет
        point_todos = browser.find_elements(By.CSS_SELECTOR, '[class="todo-item"]')
        if not point_todos:
            print("Элементы отсутствуют на странице")
        # Название кнопки Show
        str_hide = button_hide.text
        if "Show" in str_hide:
            print(True)
        # нажимаем на Show и проверяем, что элементы отобразились
        button_hide.click()
        pointtodo = browser.find_element(By.CSS_SELECTOR, '[class="todo-item"]')
        # кнопка задизейблена до ввода текста (выбран тип)
        radio_type_todo.click()
        is_button_disabled = button_add.get_attribute("disabled")
        print("value of button - disabled: ", is_button_disabled)
        # создать доп туду
        create_todo(browser, 'default')
        # все очистить
        clear_all = browser.find_element(By.CSS_SELECTOR, '[data-testid="clear_all"]')
        str_clear = clear_all.text
        if "Clear all" in str_clear:
            print(True)
        clear_all.click()
        # проверить, что нет элементов после удаления
        empty_pounts = browser.find_elements(By.CSS_SELECTOR, '[class="todo-item"]')
        if not empty_pounts:
            print("Элемент отсутствует на странице")
        check_missing_buttons(browser)
