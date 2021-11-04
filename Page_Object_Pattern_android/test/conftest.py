from selenium.webdriver.support.wait import WebDriverWait
from page_object_pattern.utils.driver_factor import DriverFactor
from page_object_pattern.utils.driver_factor import Apps_under_testing
import pytest

# """appsList form DriverFactory Allow us to Set order in testing method, To develop the application"""
# appsList = DriverFactor.get_data()

@pytest.fixture(params=Apps_under_testing)
def setup(request):
    driver = DriverFactor.get_driver(request.param)
    driver.implicitly_wait(5)
    request.cls.driver = driver

    wait = WebDriverWait(driver, 10, 0.5)
    request.cls.wait = wait
    request.cls.param = request.param

    yield
    driver.quit()
