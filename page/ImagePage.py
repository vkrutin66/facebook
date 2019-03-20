import random
import requests

from selenium.webdriver.common.keys import Keys

from locator.Locator import Locator
from page.Page import Page


class ImagePage(Page):

    image = Locator("CSS", "#media_container img")
    input = Locator("XPATH", "//input[@class='q']")
    image_link = Locator("CSS", ".search_results .item>a")

    def download_image(self):
        print("Download image")
        self.get_element(self.input).send_keys("Sunny Fitness")
        self.get_element(self.input).send_keys(Keys.ENTER)
        i = random.randrange(len(self.get_elements(self.image_link)))
        self.get_elements(self.image_link)[i].click()
        src = self.get_element(self.image).get_attribute('src')
        with open("./image/image.jpg", "wb") as f:
            f.write(requests.get(src).content)

    def to_facebook(self):
        self.driver.get("https://www.facebook.com/")
