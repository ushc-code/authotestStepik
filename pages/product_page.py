from .base_page import BasePage
from .locators import LoginPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def product_add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON_LINK)
        basket_link.click()

    def should_be_product_page(self):
        self.should_be_basket_and_product_same_name()
        self.should_be_basket_and_product_same_price()

    def should_be_basket_and_product_same_name(self):
        # Проверка того, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        # который добавили
        product_name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert product_name_basket == product_name_page, \
            f"Product names in page and basket are not the same! {product_name_page} != {product_name_basket}"

    def should_be_basket_and_product_same_price(self):
        # Проверка стоимости в корзине. Стоимость в корзине должна совпадать с ценой товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text[1:]
        assert product_price == basket_price, \
            f"Product prices in page and basket are not the same! {product_price} != {basket_price}"

    def should_disappered_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_MESSAGE), "Success message is not disappeared"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Success message is presented, but should not be"