# -*- coding: utf-8 -*-

import os
import random
import time

from selenium.webdriver import ActionChains

from locator.Locator import Locator
from page.Page import Page


class GroupPage(Page):

    input_field = Locator("CSS", "._3nd0")
    submit_button = Locator("XPATH", "//button[@data-testid='react-composer-post-button']")
    add_photo_button = Locator("XPATH", "//a[@role='presentation']")
    add_image = Locator("XPATH", "//input[@type='file']")
    cancel_button = Locator("CSS", ".layerCancel")

    inbox_messages = Locator("XPATH", "//a[contains(@href,'messages') and @role='tab'] ")

    notifications_loc = Locator("XPATH", "//a[contains(@href,'notifications') and @role='tab'] ")

    like_buttons = Locator("XPATH", "//a[@data-testid='fb-ufi-likelink']")

    def post(self):
        self.wait(self.input_field)
        self.get_element(self.input_field).click()
        self.wait(self.add_photo_button)
        self.get_element(self.add_photo_button).click()
        time.sleep(1)
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path = my_path.split("page", 1)[0]
        path = os.path.join(my_path, "image/image.jpg")
        self.get_element(self.add_image).send_keys(path)

        text = {
            1: "Health and wellness is a process of achieving one’s personal best state of mental and physical being.",
            2: "All you need is love. But a little chocolate now and then doesn't hurt.",
            3: "Dieting is the only game where you win when you lose!",
            4: "Don't cry because it's over, smile because it happened.",
            5: "A fit, healthy body-- that is the best fashion statement."
        }.get(random.randrange(5), "A fit, healthy body-- that is the best fashion statement.")

        ActionChains(self.driver).send_keys(text).perform()
        self.get_element(self.submit_button).click()
        time.sleep(5)
        if self.exists(self.cancel_button):
            self.get_element(self.cancel_button).click()
            time.sleep(1)

    def check_group_inbox(self):
        time.sleep(1)
        self.get_element(self.inbox_messages).click()
        time.sleep(6)

    def check_group_notifications(self):
        time.sleep(1)
        self.get_element(self.notifications_loc).click()
        time.sleep(3)

    def like_group_posts(self):
        self.scroll(random.randrange(10000))
        if self.exists(self.like_buttons):
            for i in range(random.randrange(5)):
                range_num = len(self.get_elements(self.like_buttons))
                x = random.randrange(range_num)
                self.driver.execute_script("arguments[0].click();", self.get_elements(self.like_buttons)[x])
