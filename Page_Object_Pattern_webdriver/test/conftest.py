import allure
import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType
from Page_Object_Pattern.utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = DriverFactory.get_driver("chrome")
    # driver = DriverFactory.get_driver("firefox")
    driver.implicitly_wait(10)
    # driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name = "Test failed", attachment_type = AttachmentType.PNG)

    driver.quit()