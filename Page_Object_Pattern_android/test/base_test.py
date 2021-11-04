import pytest
from page_object_pattern.utils.read_data import ExcelReader
from page_object_pattern.apps.PhoneApp import SearchData
from page_object_pattern.apps.MessengerApp import SearchDataMessenger
from page_object_pattern.apps.androidGlobalTest import SearchDataMulti_App
import os



@pytest.mark.usefixtures("setup")
class TestSearch:

    # @pytest.mark.parametrize("data", ExcelReader.get_data())
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_call(self, data):
        """Here set your testing steps with selected apps"""

        if self.param == "androidGlobalTest":
            test = SearchDataMulti_App(self.driver)
            test.startApps()

        elif self.param == "android3":
            test1 = SearchData(self.driver, self.wait)
            test1.call(str(int(data.phone_number)))

        elif self.param == "android2":
            test1 = SearchDataMessenger(self.driver, self.wait)
            test1.call()

        elif self.param == "HuaweiCamera":
            pass # under build

        else:
            pass

