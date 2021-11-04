from appium import webdriver
import json, os

"""Seating serial number here"""
sn = ['']


""" Application under testing. VARIABLES SHOULD BE INSIDE LIST! """
Apps_under_testing = ['androidGlobalTest', 'androidGlobalTest']



# class JsonReadData:
#
#     @staticmethod
#     def get_data():
#         data = {}
#         dirlist = os.listdir("..\\devicesUnderTest\\")
#         with open("..\\devicesUnderTest\\" + dirlist[-1]) as json_file:
#             data = json.load(json_file)
#
#         data = []
#         for i in range(1, sheet.nrows):
#             search_data = SearchData(sheet.cell(i, 0).value, sheet.cell(i, 1).value, sheet.cell(i, 2).value)
#             data.append(search_data)
#         return data


class DriverFactor:

    @staticmethod
    def get_driver(phone):

        # if phone == 'androidGlobalTest':
        #     """ Use for random test app - without chosen package before """
        #
        #     return webdriver.Remote(
        #         command_executor='http://localhost:4444/wd/hub',
        #         desired_capabilities={"browserName": "Android", "platform": "ANDROID",
        #                               "udid": "LHS7N18B29002444", 'javascriptEnabled': True})

        if phone == 'androidGlobalTest':
            """ Use for random test app - without chosen package before """

            device = {
                "platformName": "Android",
                "platformVersion": "10",
                "deviceName": sn[0],
                "noReset": True,
                "fullReset": False,
            }

            return webdriver.Remote('http://localhost:4723/wd/hub', device)

        elif phone == 'android1':
            device = {
                "platformName": "Android",
                "platformVersion": "10",
                "deviceName": sn[0],
                "noReset": True,
                "fullReset": False,
                "appPackage": "com.whatsapp",
                "appActivity": ".Main"
            }

            return webdriver.Remote('http://localhost:4723/wd/hub', device)

        elif phone == 'android2':
            """Messenger"""

            device = {
                "platformName": "Android",
                "platformVersion": "10",
                "deviceName": sn[0],
                "noReset": True,
                "fullReset": False,
                "appPackage": "com.facebook.orca",
                "appActivity": ".auth.StartScreenActivity"
            }

            return webdriver.Remote('http://localhost:4723/wd/hub', device)

        elif phone == 'android3':
            """Contacts GMS - compare with MateP20, """

            device = {
                "platformName": "Android",
                "platformVersion": "10",
                "deviceName": sn[0],
                "noReset": False,
                "appPackage": "com.android.contacts",
                "appActivity": ".activities.DialtactsActivity"
            }

            return webdriver.Remote('http://localhost:4723/wd/hub', device)

        elif phone == 'HuaweiCamera':
            """ camera Huawei"""

            device = {
                "platformName": "Android",
                "platformVersion": "10",
                "deviceName": sn[0],
                "noReset": True,
                "fullReset": False,
                "appPackage": "com.huawei.camera",
                "appActivity": "com.huawei.camera"
            }

            return webdriver.Remote('http://localhost:4723/wd/hub', device)

        raise Exception("Provide valid driver name")

    # @staticmethod
    # def get_data():
    #     """ Application under testing. VARIABLES SHOULD BE INSIDE LIST! """
    #     return ['androidGlobalTest', 'androidGlobalTest', 'androidGlobalTest', 'androidGlobalTest', 'androidGlobalTest', 'androidGlobalTest']

