from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class BucketButton():
    B_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_ITEM = (By.CSS_SELECTOR, ".alert-noicon:nth-child(1) strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class Basket():
    MESSAGE_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class RegForm():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FIELD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_FIELD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")
