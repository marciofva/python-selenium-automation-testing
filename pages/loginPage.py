from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self._LOGIN_INPUT = (By.ID, "email")
        self._PASSWORD_INPUT = (By.NAME, "passwd")
        self._SUBMIT_LOGIN_BTN = (By.ID, "SubmitLogin")
        self._FLASH_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger>ol>li")
        self._SIGNOUT_BTN = (By.CSS_SELECTOR, ".header_user_info a[href*='mylogout']")
        self._HEADING_ACCOUNT = (By.CSS_SELECTOR, "div.row.addresses-lists")

    def submit_login(self, data_file):
        self.find_element(self._LOGIN_INPUT).send_keys(data_file["email"])
        self.find_element(self._PASSWORD_INPUT).send_keys(data_file["password"])
        self.find_element(self._SUBMIT_LOGIN_BTN).click()
        return self

    def is_visible_account_page(self):
        return self.is_elements_visible(self._SIGNOUT_BTN, self._HEADING_ACCOUNT)

    def get_flash_error_message(self):
        return self.find_element(self._FLASH_MESSAGE).text
