import os
import platform

from selenium import webdriver
from pathlib import Path
from subprocess import Popen


class BaseAction:

    def __init__(self):
        options = webdriver.ChromeOptions()
        home = str(Path.home())

        if platform.system() == 'Windows':
            options.add_argument("user-data-dir=" + home + "/AppData/Local/Google/Chrome/User Data")
            Popen('taskkill /F /IM chrome.exe', shell=True)
            self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe", chrome_options=options)
        else:
            options.add_argument("user-data-dir=~/Library/Application Support/Google/Chrome")
            os.system("killall -9 'Google Chrome'")
            self.driver = webdriver.Chrome(executable_path="drivers/chromedriver_mac", chrome_options=options)
        print("Open browser Chrome")
        self.driver.maximize_window()
