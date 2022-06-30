from selenium.webdriver.common.by import By

class CatalogPage:
    BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb')
    PRODUCT_LIST = (By.CSS_SELECTOR, '.list-group')
    FIRST_PRODUCT = (By.CSS_SELECTOR, '.product-layout')
    LIMIT_INPUT = (By.CSS_SELECTOR, '#input-limit')
    SORT_INPUT = (By.CSS_SELECTOR, '#input-sort')
