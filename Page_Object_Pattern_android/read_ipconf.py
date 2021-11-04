import subprocess
import re
import os
import shutil
import json
import time
"""" Karol Zajkowski """


class Main(object):

    __hubPort = 4723 #4444
    __port = 4725
    devices = {}

    def __init__(self):
        self.__ipConf = None
        self.__sn = None
        super(Main, self).__init__()

    def get_devices(self):

        devices = os.popen('adb devices').read()
        d_list = str(devices).split("\n")

        sn = []
        for line in d_list:

            if "device" in line and "List" not in line:
                sn.append(line.split("\t")[0])

        self.__sn = sn
        print(sn)
        return self.__sn

    def get_dictionery(self):

        for serialNumber in self.__sn:

            device_json = {
                              "capabilities":
                                  [
                                    {
                                      "browserName": "Android",
                                      "version": "",
                                      "udid": "",
                                      "maxInstances": 1,
                                      "platform": "ANDROID",
                                      "deviceName": ""
                                    }
                                  ],
                              "configuration":
                              {
                                "cleanUpCycle":2000,
                                "timeout":30000,
                                "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
                                "maxSession": 1,
                                "register": True,
                                "registerCycle": 5000,
                                "hubPort": self.__hubPort,
                                "hubHost": "",
                                "hubProtocol": "http"
                              }
                            }

            proc_version = self.command_output("adb -s {} shell getprop ro.build.version.release".format(serialNumber))
            line1 = proc_version.stdout.read()
            line1 = str(line1.decode('utf-8')).strip()

            proc_marketing_name = self.command_output("adb -s {} shell getprop ro.config.marketing_name".format(serialNumber))
            line2 = proc_marketing_name.stdout.read()
            line2 = str(line2.decode('utf-8')).strip()

            device_json["capabilities"][0]["udid"] = serialNumber
            device_json["capabilities"][0]["version"] = line1
            device_json["capabilities"][0]["deviceName"] = line2
            device_json["configuration"]["hubHost"] = self.__ipConf

            self.add_data(serialNumber, device_json)

    @staticmethod
    def command_output(command):
        return subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                stdin=subprocess.PIPE, )

    @classmethod
    def add_data(cls, sn, json):
        cls.devices[sn] = json

    def countPort(self):
        self.__port += 2
        # print(self.__port)

    def Ipconf(self):
        IPv4 = []
        proces = self.command_output("ipconfig")

        for line in iter(proces.stdout.readline, b''):
            line = str(line.decode('utf-8'))

            formatedLine = re.search(r"IPv4 Address. . . . . . . . . . . :\D(\d+).(\d+).(\d+).(\d+)", line)

            if formatedLine is not None:
                # print(formatedLine)
                tupleInt = re.findall(r'(\d+).(\d+).(\d+).(\d+)', formatedLine.group())
                for intiger in tupleInt:
                    IPv4.append('.'.join(intiger))

        self.__ipConf = IPv4[-1]
        return self.__ipConf

    @staticmethod
    def runCMD(command):
        p = subprocess.Popen(["start", "cmd", "/k", command],
                             shell=True)
        p.wait()

    def write_json(self):
        path = "devicesUnderTest"

        if os.path.exists(path):
            shutil.rmtree(path)

        os.makedirs(path)

        for sn in self.devices.keys():
            with open(path+'\\{}.json'.format(sn), 'w') as json_file:
                json.dump(self.devices[sn], json_file)

    def main(self):
        self.get_devices()
        self.Ipconf()
        self.get_dictionery()
        self.write_json()

        path = os.getcwd()
        self.runCMD("java -jar selenium-server-standalone-3.141.59.jar -role hub -port {}".format(self.__hubPort))

        time.sleep(2)
        path_devices_under_test = path+"\\devicesUnderTest"
        dir_list = os.listdir(path_devices_under_test)
        for sn in dir_list:
            # print(sn)  # appium in environment variable or add here node
            self.runCMD("appium -p {} --nodeconfig {}\\{}".format(self.__port, path_devices_under_test, sn))
            self.countPort()


if __name__ == '__main__':
    underTest = Main()
    underTest.main()



