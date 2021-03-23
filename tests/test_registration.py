from pages.registrationPage import RegistrationPage
from utils import path_directory
from utils.helper import config_yaml, get_environment
from utils.webdriver_factory import DriverFactory
import unittest


class TestRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.env = get_environment()

    def setUp(self):
        self.data_file = config_yaml(path_directory.Path.ROOT.value + "/data/Register.yaml")
        self.driver = DriverFactory.get_driver("chrome")
        url = config_yaml(path_directory.Path.ROOT.value + "/env/url.yaml")
        self.driver.get(url[self.env]["URL"])

    def test_registration(self):
        is_valid = RegistrationPage(self.driver).register_new_user(self.data_file["registration"]).is_visible_account_page()

        self.assertTrue(is_valid)
        self.assertEqual(self.driver.title, "My account - My Store")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
