from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID,"id_login-password")
    LOGIN_BUTTON = (By.NAME,"login_submit")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_USERNAME = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
class ProductPageLocators():
    BASKET_BUTTON_LINK = (By.CSS_SELECTOR, "form#add_to_basket_form > button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.row h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")