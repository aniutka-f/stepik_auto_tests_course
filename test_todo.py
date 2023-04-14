
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://lovely-genie-b5af1b.netlify.app/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    todo_options = []
    for option in browser.find_elements(By.CLASS_NAME, "option"):
        option_type = option.find_element(By.TAG_NAME, "input").get_attribute("value")
        todo_options.append(option_type)


    def create_todo(todo_option):
        add_todo = browser.find_element(By.CSS_SELECTOR, '[data-testid="input_content"]')
        value = "my option = " + todo_option
        add_todo.send_keys(value)
        button_add = browser.find_element(By.CSS_SELECTOR, '[data-testid="add_todo"]')
        is_button_disabled = button_add.get_attribute("disabled")
        print("value of button - disabled: ", is_button_disabled)
        assert is_button_disabled is not None, "Button not disabled"
        option_element = browser.find_element(By.XPATH, '//div[@class="options"]//span[@class="bubble ' + todo_option + '"]')
        option_element.click()
        button_add.click()

  for option_type in todo_options:
        create_todo(option_type)

    def right_values():
        input_text = browser.find_element(By.CSS_SELECTOR, '[class = "todo-content"]')
        input_text_value = input_text.get_attribute("value")
        print("value of input:", input_text_value)

    right_values()
    def editing():
        input_editing = browser.find_element(By.XPATH, "//section[@class='space-column']//input[@type='text']")
        input_editing.click()
        input_editing.send_keys("editing")

    editing()

    def todo_ready():
        input_todo = browser.find_element(By.XPATH, "//section[@class='space-column']//span")
        input_todo.click()

    todo_ready()


    def change_visible():
        change_visible = browser.find_element(By.CSS_SELECTOR, '[data-testid="change_visible"]').click()
        change_visible()
    def clear_all():
        button_clear_all = browser.find_element(By.CSS_SELECTOR, '[class="action-button clear-all-button"]').click()

    clear_all()

    for option_type in todo_options:
        create_todo(option_type)

    def delete_todo():
        button_delete = browser.find_element(By.CSS_SELECTOR, '[data-testid="delete"]')
        button_delete.click()

    delete_todo()


finally:
    browser.quit()



