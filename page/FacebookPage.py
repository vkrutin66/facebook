import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from locator.Locator import Locator
from page.Page import Page
import random


class FacebookPage(Page):

    go_to_friends_but = Locator("XPATH", '//*[@id="pagelet_ego_pane"]/div[1]/div/div/div/div[1]/a')
    go_to_user_but = Locator("XPATH", "//*[@id='userNav']//a[contains(@href,'https://www.facebook.com/')]")
    go_to_advertising = Locator("CSS", ".r_c4r-nm7cl a")
    go_to_link_loc = Locator("CSS", "._6ks a")

    black_monitor = Locator("CSS", "._3ixn")

    post_textarea = Locator("XPATH", "//textarea[contains(@class,'navigationFocus')]")
    post_button = Locator("CSS", "._1mf")
    submit_post = Locator("CSS", "._6c0o button")
    post_overlay = Locator("CSS", "._3u15")

    def get_posted_loc(self, text):
        return Locator("XPATH", "//p[contains(.,'" + text + "')]")

    comment_buttons = Locator("CSS", "._666h")

    like_buttons = Locator("CSS", "._3l2t")

    image_link = Locator("XPATH", "//a[contains(@class,'_4-eo _2t9n')]")
    image_div = Locator("CSS", ".stageWrapper")
    image_close = Locator("XPATH", "//a[@class='_xlt _418x']")

    stories_div = Locator("CSS", ".vertical-4pog")
    story_div = Locator("XPATH", "//div[contains(@class,'size-small-48') and not(contains(@class, 'no-border'))]")
    close_story = Locator("XPATH", "//a[@class='_4-o9 _50-m _51an _5wx4 _2chv']")

    def clean_monitor(self):
        if self.exists(self.black_monitor):
            self.get_element(self.black_monitor).click()

    def make_a_post(self):
        time.sleep(1)
        text = 'Post' + str(random.randrange(100000))
        if self.exists(self.post_textarea):
            self.get_element(self.post_textarea).send_keys(text)
        else:
            self.get_element(self.post_button).click()
            ActionChains(self.driver).send_keys(text).perform()
        time.sleep(1)
        self.get_element(self.submit_post).click()
        self.wait(self.get_posted_loc(text))

    def add_comment(self):
        time.sleep(1)
        i = random.randrange(len(self.get_elements(self.comment_buttons)))
        self.driver.execute_script("arguments[0].click();", self.get_elements(self.comment_buttons)[i])
        ActionChains(self.driver).send_keys('Cool!!').send_keys(Keys.ENTER).perform()

    def like_random_posts(self):
        if self.exists(self.like_buttons):
            for i in range(random.randrange(10)):
                range_num = len(self.get_elements(self.like_buttons))
                x = random.randrange(range_num)
                time.sleep(1)
                self.driver.execute_script("arguments[0].click();", self.get_elements(self.like_buttons)[x])

    def open_image(self):
        if self.exists(self.image_link):
            print('Open Image')
            i = random.randrange(len(self.get_elements(self.image_link)))
            self.driver.execute_script("arguments[0].click();", self.get_elements(self.image_link)[i])
            time.sleep(1)
            for x in range(random.randrange(10)):
                ActionChains(self.driver).move_to_element(self.get_element(self.image_div)).click().perform()
                time.sleep(1)
            self.driver.execute_script("arguments[0].click();", self.get_element(self.image_close))
            time.sleep(1)

    def watch_stories(self):
        if self.exists(self.story_div):
            print('Watch stories')
            self.get_element(self.story_div).click()
            time.sleep(1)
            try:
                self.wait_to_disappear(self.black_monitor)
            except TimeoutException:
                self.driver.execute_script("arguments[0].click();", self.get_element(self.close_story))

    def go_to_friends_page(self):
        if self.exists(self.go_to_friends_but):
            self.get_element(self.go_to_friends_but).click()
            return True
        else:
            return False

    def go_to_user_page(self):
        self.get_element(self.go_to_user_but).click()

    def go_to_advertising_page(self):
        if self.exists(self.go_to_advertising):
            self.get_element(self.go_to_advertising).click()
            time.sleep(10)

    def go_to_link(self):
        if self.exists(self.go_to_link_loc):
            print("Go to link")
            i = random.randrange(len(self.get_elements(self.go_to_link_loc)))
            self.driver.execute_script("arguments[0].click();", self.get_elements(self.go_to_link_loc)[i])
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
