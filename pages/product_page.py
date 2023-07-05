from selenium.common.exceptions import NoAlertPresentException
from .locators import BucketButton
from .base_page import BasePage
import math


class ProductPage(BasePage):
    def push_the_button(self):
        self.browser.find_element(*BucketButton.B_BUTTON).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_added_item(self):
        assert self.browser.find_element(*BucketButton.ADDED_ITEM).text ==\
               self.browser.find_element(*BucketButton.ITEM_NAME).text

    def check_success_message_isep(self):
        assert self.is_not_element_present(*BucketButton.SUCCESS_MESSAGE)

    def check_success_message_id(self):
        assert self.is_disappeared(*BucketButton.SUCCESS_MESSAGE)
