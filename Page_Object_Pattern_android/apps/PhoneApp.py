import datetime
import time
from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import *
from selenium.webdriver.support import expected_conditions
import os
# from selenium.common.exceptions import TimeoutException, NoSuchElementException


"""App name - it's used for create new file"""
fileName = 'PhoneApp'


def timeNow():
    """Hours difference."""
    return datetime.datetime.now()


class SearchData:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.timeNow = timeNow().strftime("hh%H_mm%M_ss%S")
        self.path = '\\'+fileName+str(self.timeNow)

    def call(self, dataNumber):

        self.driver.find_element_by_xpath(PhoneAppLocators.phone_tab).click()
        phone_number = str(int(dataNumber))

        try:

            global logs
            logs = self.driver.get_log('logcat')

            for i in phone_number:
                self.driver.find_element_by_xpath(PhoneAppLocators.phone_ADDnumber.format(i)).click()

            self.driver.find_element_by_id(PhoneAppLocators.call).click()

            self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, PhoneAppLocators.mute)))
            time.sleep(10)

        except:

            if os.path.exists("..\\reports\\{}".format(fileName)):
                self.driver.save_screenshot("..\\reports\\{}\\{}.png".format(fileName, self.timeNow))
                os.system('Getlog.bat ..\\reports\\{}\\{}'.format(fileName, self.timeNow))
                with open("..\\reports\\{}\\{}.log".format(fileName, self.path), 'w', encoding='utf-8') as f:
                    for log in logs:
                        f.writelines(str(log) + '\n')
                # self.driver.save_screenshot("..\\reports\\{}\\{}.png".format(fileName, self.timeNow))
                time.sleep(2)
                # print("\nTimeout expired. You must be faster!\nThe call should be answered faster\n", sys.exc_info())
                # self.driver.find_element_by_xpath(PhoneAppLocators.callEnd).click()
                assert True != True

            else:
                os.makedirs("..\\reports\\{}".format(fileName))
                self.driver.save_screenshot("..\\reports\\{}\\{}.png".format(fileName, self.timeNow))
                os.system('Getlog.bat ..\\reports\\{}\\{}'.format(fileName, self.timeNow))
                with open("..\\reports\\{}\\{}.log".format(fileName, self.path), 'w', encoding='utf-8') as f:
                    for log in logs:
                        f.writelines(str(log) + '\n')
                time.sleep(2)
                # print("\nTimeout expired. You must be faster!\nThe call should be answered faster\n", sys.exc_info())
                assert True != True

        else:
            self.driver.find_element_by_xpath(PhoneAppLocators.callEnd).click()

        # finally:
        #     logging.info('Finished')


