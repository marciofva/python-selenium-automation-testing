from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.basePage import BasePage
from utils.helper import generate_uuid


class RegistrationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self._EMAIL_CREATE_INPUT = (By.CSS_SELECTOR, "#email_create")
        self._CREATE_BTN = (By.CSS_SELECTOR, "#SubmitCreate")
        self._NAME_INPUT = (By.CSS_SELECTOR, "#customer_firstname")
        self._LASTNAME_INPUT = (By.CSS_SELECTOR, "#customer_lastname")
        self._PASSWORD_INPUT = (By.CSS_SELECTOR, "#passwd")
        self._DAY_DROPBOX = (By.CSS_SELECTOR, "#days")
        self._MONTH_DROPBOX = (By.CSS_SELECTOR, "#months")
        self._YEAR_DROPBOX = (By.CSS_SELECTOR, "#years")
        self._ADDRESS1_INPUT = (By.CSS_SELECTOR, "#address1")
        self._ADDRESS2_INPUT = (By.CSS_SELECTOR, "#address2")
        self._CITY_INPUT = (By.CSS_SELECTOR, "#city")
        self._STATE_INPUT = (By.CSS_SELECTOR, "#id_state")
        self._POSTCODE_INPUT = (By.CSS_SELECTOR, "#postcode")
        self._ADDITIONAL_INFO_INPUT = (By.CSS_SELECTOR, "#other")
        self._PHONE_INPUT = (By.CSS_SELECTOR, "#phone")
        self._MOBILE_PHONE_INPUT = (By.CSS_SELECTOR, "#phone_mobile")
        self._ALIAS_INPUT = (By.CSS_SELECTOR, "#alias")
        self._SUBMIT_BTN = (By.CSS_SELECTOR, "#submitAccount")
        self._SIGNOUT_BTN = (By.CSS_SELECTOR, ".header_user_info a[href*='mylogout']")

    def register_new_user(self, data_file):
        new_email = data_file["email"].replace("xxxxxxxxxx", generate_uuid(10))
        self.find_element(self._EMAIL_CREATE_INPUT).send_keys(new_email)
        self.find_element(self._CREATE_BTN).click()
        self.find_element(self._NAME_INPUT).send_keys(data_file["firstName"])
        self.find_element(self._LASTNAME_INPUT).send_keys(data_file["secondName"])
        self.find_element(self._PASSWORD_INPUT).send_keys(data_file["password"])
        Select(self.presence_element(self._DAY_DROPBOX)).select_by_value(str(data_file["days"]))
        Select(self.presence_element(self._MONTH_DROPBOX)).select_by_value(str(data_file["months"]))
        Select(self.presence_element(self._YEAR_DROPBOX)).select_by_value(str(data_file["years"]))
        self.find_element(self._ADDRESS1_INPUT).send_keys(data_file["address1"])
        self.find_element(self._ADDRESS2_INPUT).send_keys(data_file["address2"])
        self.find_element(self._CITY_INPUT).send_keys(data_file["city"])
        Select(self.presence_element(self._STATE_INPUT)).select_by_visible_text(str(data_file["state"]))
        self.find_element(self._POSTCODE_INPUT).send_keys(data_file["postcode"])
        self.find_element(self._ADDITIONAL_INFO_INPUT).send_keys(data_file["additionalInformation"])
        self.find_element(self._PHONE_INPUT).send_keys(data_file["phone"])
        self.find_element(self._MOBILE_PHONE_INPUT).send_keys(data_file["mobile"])
        self.find_element(self._ALIAS_INPUT).send_keys(data_file["alias"])
        self.find_element(self._SUBMIT_BTN).click()
        return self

    def is_visible_account_page(self):
        return self.is_elements_visible(self._SIGNOUT_BTN)
