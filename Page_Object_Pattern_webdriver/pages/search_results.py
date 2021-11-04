from Page_Object_Pattern.locators.locators import SerachResultLocators
import logging
import allure
from allure_commons.types import AttachmentType

class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.hotel_names_xpath = SerachResultLocators.hotel_names_xpath
        self.hotel_prices_xpath = SerachResultLocators.hotel_prices_xpath

    @allure.step("Checking results travellers")
    def get_hotel_names(self):
        hotels = self.driver.find_elements_by_xpath(self.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        allure.attach(self.driver.get_screenshot_as_png(), name="Results", attachment_type=AttachmentType.PNG)
        self.logger.info("Available hotels are: ")
        for name in names:
            self.logger.info(name)
        return names

    def get_hotel_price(self):
        prices = self.driver.find_elements_by_xpath(self.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]

        self.logger.info("Prices of hotels are: ")
        for price in hotel_prices:
            self.logger.info(price)
        return hotel_prices

