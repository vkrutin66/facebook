import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from locator.Locator import Locator
from page.Page import Page
import random


class FacebookPage(Page):

    logout_page_menu = Locator("CSS", ".loggedout_menubar")

    go_to_friends_but = Locator("XPATH", "//a[contains(@href,'https://www.facebook.com/find-friends/')]")
    go_to_user_but = Locator("XPATH", "//*[@id='userNav']//a[contains(@href,'https://www.facebook.com/')]")
    go_to_link_loc = Locator("XPATH", "//a[contains(@href, 'http') and not(contains(@href, 'facebook'))]")

    black_monitor = Locator("CSS", "._3ixn")

    post_textarea = Locator("XPATH", "//textarea[contains(@class,'navigationFocus')]")
    post_button = Locator("XPATH", "//div[@data-testid='status-attachment-mentions-input']")
    submit_post = Locator("XPATH", "//button[@data-testid='react-composer-post-button']")
    same_post_close = Locator("CSS", ".layerCancel")

    def get_posted_loc(self, text):
        return Locator("XPATH", "//p[contains(.,'" + text + "')]")

    comment_buttons = Locator("XPATH", "//a[@testid='UFI2CommentLink']")

    like_buttons = Locator("XPATH", "//a[@data-testid='UFI2ReactionLink']")

    image_link = Locator("XPATH", "//a[@data-render-location='newsstand']")
    image_div = Locator("XPATH", "//a[contains(@class,'snowliftPager next')]")
    image_close = Locator("XPATH", "//div[@id='pagelet_photo_viewer_init']/../a[@role='button']")

    stories_div = Locator("CSS", ".vertical-4pog")
    story_div = Locator("XPATH", "//div[contains(@class,'size-small-48') and not(contains(@class, 'no-border'))]")
    close_story = Locator("XPATH", "//div[@class='uiContextualLayerParent']/../a")

    watch_notifications_loc = Locator("XPATH", "//a[@name='notifications']")
    notifications_loc = Locator("XPATH", "//a[@data-testid='notif_list_item_link']")

    watch_chats_loc = Locator("XPATH", "//a[@name='mercurymessages']")

    logout_menu_loc = Locator("CSS", "#logoutMenu a")
    group_link = Locator("XPATH", "//a[contains(@data-gt,'menu_pages')]")

    def is_login_page(self):
        return self.exists(self.logout_page_menu)

    def clean_monitor(self):
        if self.exists(self.black_monitor):
            self.get_element(self.black_monitor).click()

    def make_a_post(self):
        time.sleep(1)
        text = {
            1: "What a great day",
            2: "Really enjoying this weather lately",
            3: "What are some of your favorite songs lately?",
            4: "Anyone have great recommendations for great food",
            5: "Looking for a new TV show to watch",
            6: "Recommendations for top new movies to check out"
        }.get(random.randrange(6), "What a great day")
        if self.exists(self.post_textarea):
            self.get_element(self.post_textarea).send_keys(text)
        else:
            self.get_element(self.post_button).click()
            ActionChains(self.driver).send_keys(text).perform()
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.get_element(self.submit_post))
        self.wait(self.get_posted_loc(text))
        time.sleep(1)
        if self.exists(self.same_post_close):
            self.driver.execute_script("arguments[0].click();", self.get_element(self.same_post_close))
            time.sleep(1)

    def random_scroll(self):
        for i in range(random.randrange(5)):
            self.scroll(random.randrange(10000))

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
            self.driver.execute_script("arguments[0].click();", self.get_element(self.story_div))
            time.sleep(1)
            try:
                self.wait_to_disappear(self.black_monitor)
            except TimeoutException:
                self.driver.execute_script("arguments[0].click();", self.get_element(self.close_story))

    def watch_notifications(self):
        print('Watch notifications')
        self.driver.execute_script("arguments[0].click();", self.get_element(self.watch_notifications_loc))
        time.sleep(1)
        i = random.randrange(len(self.get_elements(self.notifications_loc)))
        self.get_elements(self.notifications_loc)[i].click()
        time.sleep(2)
        if self.exists(self.black_monitor):
            self.driver.execute_script("arguments[0].click();", self.get_element(self.image_close))
        else:
            self.to_main()

    def watch_chats(self):
        print('Watch chats')
        self.get_element(self.watch_chats_loc).click()
        time.sleep(2)
        self.get_element(self.watch_chats_loc).click()
        time.sleep(1)

    def go_to_friends_page(self):
        if self.exists(self.go_to_friends_but):
            self.get_element(self.go_to_friends_but).click()
            return True
        else:
            return False

    def go_to_user_page(self):
        self.get_element(self.go_to_user_but).click()
        time.sleep(1)

    def go_to_link(self):
        self.scroll(random.randrange(10000))
        if self.exists(self.go_to_link_loc):
            print("Go to link")
            i = random.randrange(len(self.get_elements(self.go_to_link_loc)))
            self.driver.execute_script("arguments[0].click();", self.get_elements(self.go_to_link_loc)[i])
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            if 'facebook' in self.driver.current_url:
                self.driver.get("https://www.facebook.com/")
            else:
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)

    def go_to_group(self):
        self.get_element(self.logout_menu_loc).click()
        time.sleep(1)
        if self.exists(self.group_link):
            self.get_element(self.group_link).click()
            time.sleep(2)
            return True
        return False

    def go_to_image(self):
        self.driver.get("https://pixabay.com/")
