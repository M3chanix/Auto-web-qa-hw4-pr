from selenium.webdriver.common.by import By

class MainPage:
    CURRENCY_SWITCH = (By.ID, 'form-currency')
    SLIDE_PANNEL = (By.ID, 'slideshow0')
    SUPPORT_PHONE = (By.CSS_SELECTOR, 'ul.list-inline > li')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart button')
    FEATURED_LIST = (By.CSS_SELECTOR, '.product-thumb')
