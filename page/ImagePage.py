import os
import platform
import random
import requests

from selenium.webdriver.common.keys import Keys

from locator.Locator import Locator
from page.Page import Page


class ImagePage(Page):

    image = Locator("CSS", "#media_container img")
    input_field = Locator("XPATH", "//input[@class='q']")
    image_link = Locator("CSS", ".search_results .item>a")

    def download_image(self):
        print("Download image")
        self.get_element(self.input_field).send_keys("Sunny Fitness")
        self.get_element(self.input_field).send_keys(Keys.ENTER)
        i = random.randrange(len(self.get_elements(self.image_link)))
        self.driver.execute_script("arguments[0].click();", self.get_elements(self.image_link)[i])
        src = self.get_element(self.image).get_attribute('src')
        if platform.system() == 'Windows':
            with open("./image/image.jpg", "wb") as f:
                f.write(requests.get(src).content)
        else:
            my_path = os.path.abspath(os.path.dirname(__file__))
            my_path = my_path.split("page", 1)[0]
            path = os.path.join(my_path, "image/image.jpg")
            with open(path, "wb") as f:
                f.write(requests.get(src).content)

    def to_facebook(self):
        self.driver.get("https://www.facebook.com/")
