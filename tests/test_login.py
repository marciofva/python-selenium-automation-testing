from pages.loginPage import LoginPage
from utils import path_directory
from utils.webdriver_factory import DriverFactory
from utils.helper import config_yaml, get_environment
import unittest


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.env = get_environment()

    def setUp(self):
        self.data_file = config_yaml(path_directory.Path.ROOT.value + "/data/Login.yaml")
        self.driver = DriverFactory.get_driver("chrome")
        url = config_yaml(path_directory.Path.ROOT.value + "/env/url.yaml")
        self.driver.get(url[self.env]["URL"])

    def test_SubmitLoginSuccessfully(self):
        is_valid = LoginPage(self.driver)\
            .submit_login(self.data_file["valid_credentials"])\
            .is_visible_account_page()

        self.assertTrue(is_valid)
        self.assertEqual(self.driver.title, "My account - My Store")

    def test_LoginWithInvalidEmail(self):
        error_message = LoginPage(self.driver)\
            .submit_login(self.data_file["invalid_email"])\
            .get_flash_error_message()

        self.assertEqual(error_message, "Authentication failed.")

    def test_LoginWithInvalidPassword(self):
        error_message = LoginPage(self.driver)\
            .submit_login(self.data_file["invalid_password"])\
            .get_flash_error_message()

        self.assertEqual(error_message, "Authentication failed.")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
