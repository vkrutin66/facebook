import random

from locator.Locator import Locator
from page.Page import Page


class UserFriendsPage(Page):

    friends = Locator("CSS", "._698 a")

    def go_to_random_friend(self):
        i = random.randrange(len(self.get_elements(self.friends)) - 1)
        self.get_elements(self.friends)[i].click()
