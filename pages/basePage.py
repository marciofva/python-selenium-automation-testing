from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    title_is, presence_of_element_located
from utils.helper import timeout


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return WebDriverWait(self.driver, timeout()).until(visibility_of_element_located(*locator))

    def get_title(self, *locator):
        return WebDriverWait(self.driver, timeout()).until(title_is(*locator))

    def presence_element(self, *locator):
        return WebDriverWait(self.driver, timeout()).until(presence_of_element_located(*locator))

    def is_elements_visible(self, *locator):
        for element in locator:
            try:
                element = WebDriverWait(self.driver, timeout()).until(visibility_of_element_located(element))
                if not(element.is_displayed()):
                    return False
            except TimeoutException:
                return False
        return True
