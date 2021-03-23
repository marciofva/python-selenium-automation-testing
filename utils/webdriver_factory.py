from selenium import webdriver
from utils import path_directory


class DriverFactory:

    @staticmethod
    def get_driver(browser):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.headless = False
            return webdriver.Chrome(executable_path=path_directory.Path.ROOT.value + "/drivers/chromedriver",
                                    options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.headless = False
            return webdriver.Firefox(executable_path=path_directory.Path.ROOT.value + "/drivers/geckodriver",
                                     options=options)

        raise Exception("'{}' is not a supported browser".format(browser))
