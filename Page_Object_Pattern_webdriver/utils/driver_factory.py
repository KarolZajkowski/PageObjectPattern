from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.capabilities("browserName", "chrome")
            # return webdriver.Chrome(ChromeDriverManager().install(), options=options)
            return webdriver.Remote("http://192.168.56.1:4444/wd/hub", options=options)

        elif browser == 'firefox':
            options= webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

        raise Exception('Provide valid driver name')