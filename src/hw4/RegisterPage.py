from selenium.webdriver.common.by import By

class RegisterPage:
    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="input-firstname"]')
    LOGIN_PAGE_LINK = (By.XPATH, '//*[@id="content"]/p/a')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="input-password"]')
    SUBSCRIBE_YES_CHECKBOX = (By.CSS_SELECTOR, '.radio-inline')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

