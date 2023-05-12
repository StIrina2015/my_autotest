from locators.elements_page_locators import *
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_field(self):
        full_name = "Denis Denisov"
        email = "qwert@vr.ry"
        current_address = "Tampa"
        permanent_address = "Tampa"
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_field(self):
        full_name = self.elements_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.elements_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.elements_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.elements_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address










