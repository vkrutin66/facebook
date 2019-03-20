import time

from locator.Locator import Locator
from page.Page import Page
import random


class AddFriendsPage(Page):

    add_friend_button = Locator("XPATH", "//button[contains(@class,'FriendRequestAdd') and not(contains(@class,'hidden_elem'))]")
    confirm_friend = Locator("CSS", ".layerConfirm")
    cancel_check = Locator("CSS", ".layerCancel")

    def add_random_friends(self):
        time.sleep(1)
        for i in range(random.randrange(10)):
            if self.exists(self.add_friend_button):
                self.driver.execute_script("arguments[0].click();", self.get_element(self.add_friend_button))
                time.sleep(1)
                if self.exists(self.confirm_friend):
                    self.driver.execute_script("arguments[0].click();", self.get_element(self.confirm_friend))
                    time.sleep(1)
                if self.exists(self.cancel_check):
                    self.driver.execute_script("arguments[0].click();", self.get_element(self.cancel_check))
                    self.driver.execute_script("arguments[0].className += 'hidden_elem';", self.get_element(self.add_friend_button))
                    time.sleep(1)

