import random
import time

from locator.Locator import Locator
from page.Page import Page


class UserPage(Page):

    go_to_friends_loc = Locator("CSS", "._6_7 li:nth-child(3) a")

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, " + str(random.randrange(10000)) + ");")
        time.sleep(1)

    def go_to_friends_page(self):
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.get_element(self.go_to_friends_loc))
        time.sleep(1)
