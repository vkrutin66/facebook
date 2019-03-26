import time

from locator.Locator import Locator
from page.Page import Page


class UserPage(Page):

    go_to_friends_loc = Locator("XPATH", "//a[@data-tab-key='friends']")

    def go_to_friends_page(self):
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.get_element(self.go_to_friends_loc))
        time.sleep(1)
