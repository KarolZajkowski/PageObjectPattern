from allure_commons.types import AttachmentType

from Page_Object_Pattern.locators.locators import SearchHotelLocators
import logging
import allure


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.search_hotel_span_xpath = SearchHotelLocators.search_hotel_span_xpath
        self.search_hotel_input_xpath = SearchHotelLocators.search_hotel_input_xpath
        self.location_match_xpath = SearchHotelLocators.location_match_xpath
        self.check_in_input_name = SearchHotelLocators.check_in_input_name
        self.check_out_input_name = SearchHotelLocators.check_out_input_name
        self.travellers_input_id = SearchHotelLocators.travellers_input_id
        self.adult_input_id = SearchHotelLocators.adult_input_id
        self.child_input_id = SearchHotelLocators.child_input_id
        self.search_button_xpath = SearchHotelLocators.search_button_xpath

    @allure.step("setting city name '{1}'") #zamiast jedynki zostanie podmieniony parametr pierwszy czyli city
    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set city", attachment_type=AttachmentType.PNG) # do screena

    @allure.step("setting date range from '{1}' to '{2}'")  # zamiast jedynki zostanie podmieniony parametr pierwszy czyli check_in
    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting check in {checkin} and {checkout} dates".format(checkin = check_in, checkout = check_out))
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in)
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_out)
        allure.attach(self.driver.get_screenshot_as_png(), name="set date range", attachment_type=AttachmentType.PNG)

    @allure.step("setting travelers- adults - '{1}' and kids - '{2}'")
    def set_travelers(self, adults, child): #liczba?
        self.logger.info("Setting check in adults - {adults} and child - {child} dates".format(adults = adults, child = child))
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adults)
        self.driver.find_element_by_id(self.child_input_id).clear()
        self.driver.find_element_by_id(self.child_input_id).send_keys(child)
        allure.attach(self.driver.get_screenshot_as_png(), name="set travelers", attachment_type=AttachmentType.PNG)

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element_by_xpath(self.search_button_xpath).click()


