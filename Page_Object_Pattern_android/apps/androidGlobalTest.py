import random
from subprocess import Popen, PIPE, STDOUT
import datetime
import time
from appium.webdriver.common.touch_action import TouchAction
from page_object_pattern.locators.locators import *
import os
from page_object_pattern.utils.driver_factor import sn

"""App name - it's used for create new file"""
fileName = 'androidGlobalTest'


def timeNow():
    return datetime.datetime.now()


class SearchDataMulti_App:

    def __init__(self, driver):
        self.driver = driver
        self.timeNow = timeNow().strftime("hh%H_mm%M_ss%S")
        self.path = '\\' + fileName + str(self.timeNow)
        self.touch = TouchAction(self.driver)

    @staticmethod
    def activity_start(command):
        command = Popen(f'adb -s {sn[0]} shell am start -W {command}', shell=True, stdin=PIPE, stdout=PIPE,
                        stderr=STDOUT)
        output = command.stdout.read()
        output = output.decode('utf-8')

        if os.path.exists("..\\reports\\{}".format(fileName)):
            pass
        else:
            os.makedirs("..\\reports\\{}".format(fileName))

        with open('..\\reports\\{}\\app_start.txt'.format(fileName), 'a') as f:
            f.write(output)
            f.write("\n")

    @staticmethod
    def performPopen(command):
        return os.popen(command)

    def startApps(self):
        """ Apps to test """
        # test_app = [App.youtube, App.messenger, App.Gmail, App.Music, App.Maps, App.Chrome]
        test_app = []
        dir_apk = 'AppList.param'
        with open(dir_apk) as f:
            lines = [line.rstrip() for line in f]

            test_app.extend(lines)

        for app in test_app:
            try:
                global logs
                logs = self.driver.get_log('logcat')
                time.sleep(2)

                """ Swipe """
                SearchDataMulti_App.activity_start(app)
                time.sleep(5)
                for i in range(3):
                    SearchDataMulti_App.performPopen(KeysInput.swipe)
                    time.sleep(2)

                """ Tap """
                for i in range(2):
                    rand = int(random.randint(1300, 1600))
                    self.touch.tap(x=520, y=rand).perform()
                    time.sleep(5)

                SearchDataMulti_App.performPopen(KeysInput.home.format(sn[0]))
                """ App terminated """
                SearchDataMulti_App.performPopen(KeysInput.terminate_app.format(sn[0], app.split("/")[0]))
                time.sleep(2)

            except Exception as e:
                print(e)
                if os.path.exists("..\\reports\\{}".format(fileName)):
                    self.driver.save_screenshot("..\\reports\\{}\\{}.png".format(fileName, self.timeNow))
                    os.system('Getlog.bat ..\\reports\\{}\\{}'.format(fileName, self.timeNow))
                    with open("..\\reports\\{}\\{}.log".format(fileName, self.timeNow), 'w', encoding='utf-8') as f:
                        for log in logs:
                            f.writelines(str(log) + '\n')
                    time.sleep(2)
                    assert True != True

                else:
                    os.makedirs("..\\reports\\{}".format(fileName))
                    self.driver.save_screenshot("..\\reports\\{}\\{}.png".format(fileName, self.timeNow))
                    os.system('Getlog.bat ..\\reports\\{}\\{}'.format(fileName, self.timeNow))
                    with open("..\\reports\\{}\\{}.log".format(fileName, self.timeNow), 'w', encoding='utf-8') as f:
                        for log in logs:
                            f.writelines(str(log) + '\n')
                    time.sleep(2)
                    assert True != True

            finally:
                SearchDataMulti_App.performPopen(KeysInput.home.format(sn[0]))

        # SearchDataMulti_App.performPopen(KeysInput.reboot.format(sn[0]))
        # time.sleep(60)
