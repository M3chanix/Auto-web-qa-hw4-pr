from selenium.webdriver.common.by import By

class AdminPage:
    NAVBAR_IMAGE = (By.CSS_SELECTOR, '[href*="common/login"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[name="username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')
    FORGOT_LINK = (By.CSS_SELECTOR, '[href$="forgotten"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

