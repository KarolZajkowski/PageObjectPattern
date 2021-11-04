import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Page_Object_Pattern.pages.search_hotel import SearchHotelPage
from Page_Object_Pattern.pages.search_results import SearchResultPage
import allure
# from Page_Object_Pattern.test.base_test import BaseTest
from Page_Object_Pattern.utils.read_excel import ExcelReader


@pytest.mark.usefixtures("setup")    # metoda setup z BaseTest
# class TestHotelSearch(BaseTest):
class TestHotelSearch:

    @allure.title("This is title")
    @allure.description("Test description")
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_hotel_search(self, data):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range(data.check_in, data.check_out)
        search_hotel_page.set_travelers("2", "2")
        search_hotel_page.perform_search()
        results_page = SearchResultPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_price()

        assert hotel_names[0] == 'Jumeirah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert price_values[0] == '€20.24'
        assert price_values[1] == '€46'
        assert price_values[2] == '€73.60'
        assert price_values[3] == '€1'




