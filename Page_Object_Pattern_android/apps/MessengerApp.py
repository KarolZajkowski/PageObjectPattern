import datetime
from page_object_pattern.locators.locators import *
import os

"""App name - it's used for create new file"""
fileName = 'MessengerApp'


def timeNow():
    """Hours difference."""
    return datetime.datetime.now()


class SearchDataMessenger:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.timeNow = timeNow().strftime("hh%H_mm%M_ss%S")
        self.path = '\\' + fileName + str(self.timeNow)

    @staticmethod
    def performPopen(command):
        return os.popen(command)

    def call(self):
        self.driver.find_element_by_xpath(MessengerApp.search).click()#send_keys("Text Text")
        self.driver.find_element_by_xpath(MessengerApp.search2).send_keys("Text Text")
        # SearchDataMessenger.performPopen(KeysInput.NotificationBar)
        # time.sleep(2)

        # try:
        #     self.driver.find_element_by_id(MessengerApp.locatorFrame).click()
        #
        #     # self.driver.find_element_by_xpath(MessengerApp.clickText).click()
        #     # self.driver.find_element_by_xpath(MessengerApp.clickenterText).send_keys("test")
        #     # phone_number = str(int(dataNumber))
        #
        #     # for i in phone_number:
        #     #     self.driver.find_element_by_xpath(PhoneAppLocators.phone_ADDnumber.format(i)).click()
        #     #
        #     # self.driver.find_element_by_id(PhoneAppLocators.call).click()
        #
        #     global logs
        #     logs = self.driver.get_log('logcat')
        #
        #     # self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, PhoneAppLocators.mute)))
        #     # time.sleep(10)
        #
        #
        #
        # except:
        #     pass

        # if os.path.exists("..\\reports\\{}".format(fileName)):
        #     self.driver.save_screenshot("..\\reports\\{}\\{}.png".format(fileName, self.timeNow))
        #     os.system('Getlog.bat ..\\reports\\{}\\{}'.format(fileName, self.timeNow))
        #     with open("..\\reports\\{}\\{}.log".format(fileName, self.path), 'w', encoding='utf-8') as f:
        #         for log in logs:
        #             f.writelines(str(log) + '\n')
        #     time.sleep(2)
        #     assert True != True
        #
        # else:
        #     os.makedirs("..\\reports\\{}".format(fileName))
        #     self.driver.save_screenshot("..\\reports\\{}\\{}.png".format(fileName, self.timeNow))
        #     os.system('Getlog.bat ..\\reports\\{}\\{}'.format(fileName, self.timeNow))
        #     with open("..\\reports\\{}\\{}.log".format(fileName, self.path), 'w', encoding='utf-8') as f:
        #         for log in logs:
        #             f.writelines(str(log) + '\n')
        #     time.sleep(2)
        #     assert True != True

        # else:
        #     self.driver.find_element_by_xpath(PhoneAppLocators.callEnd).click()


