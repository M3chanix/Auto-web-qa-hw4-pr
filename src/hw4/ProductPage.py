from selenium.webdriver.common.by import By

class ProductPage:
    PRICE = (By.CSS_SELECTOR, '.list-unstyled h2')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    THUMBNAIL = (By.CSS_SELECTOR, '.thumbnail')
    ADD_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    RATING_STARS = (By.CSS_SELECTOR, '.rating')

