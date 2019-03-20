import random

from selenium import webdriver
from page.FacebookPage import FacebookPage
from page.AddFriendsPage import AddFriendsPage
from page.GroupPage import GroupPage
from page.ImagePage import ImagePage
from page.LoginPage import LoginPage
from page.UserFriendsPage import UserFriendsPage
from page.UserPage import UserPage
from pathlib import Path


class Actions:

    def __init__(self, browser):
        if browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r'drivers/geckodriver.exe')
        if browser == "Chrome":
            options = webdriver.ChromeOptions()
            home = str(Path.home())
            options.add_argument("user-data-dir=" + home + "/AppData/Local/Google/Chrome/User Data")
            self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe", chrome_options=options)
        print("Open browser ", browser)
        self.driver.maximize_window()

        self.loginPage = LoginPage(self.driver)
        self.facebookPage = FacebookPage(self.driver)
        self.addFriendsPage = AddFriendsPage(self.driver)
        self.userPage = UserPage(self.driver)
        self.userFriendsPage = UserFriendsPage(self.driver)
        self.groupPage = GroupPage(self.driver)
        self.imagePage = ImagePage(self.driver)

    def open_page(self, page_url):
        print("Open page ", page_url)
        self.driver.get(page_url)

    def login(self, user, password):
        pass
        # if not self.loginPage.is_it_login_page():
        #    file = open("./cookies/cookies.pkl", "rb")
        #     cookies = pickle.load(file)
        #     file.close()
        #     print("Get cookies")
        #     for cookie in cookies:
        #         self.driver.add_cookie(cookie)
        #     time.sleep(1)
        #     self.driver.refresh()
        #     if self.loginPage.is_it_login_page():
        #         print("Login")
        #         self.loginPage.login(user, password)
        #     file = open("./cookies/cookies.pkl", "wb")
        #     pickle.dump(self.driver.get_cookies(), file)
        #     file.close()

    def random_actions(self):
        print('Start Random Actions')
        self.clean_monitor()

        i = 0
        while i < 17:
            i = random.randrange(19)
            if i == 1:
                self.add_random_friends()
            if i == 2:
                self.make_a_post()
            if i == 3:
                self.watch_user_page()
            if i == 4:
                self.add_comment()
            if i == 5:
                self.like_random_posts()
            if i == 6:
                self.go_to_random_friend()
            if i == 7:
                self.open_image()
            if i == 8:
                self.watch_stories()
            if i == 9:
                self.random_scroll()
            if i == 10:
                self.go_to_link()
            if i == 11:
                self.watch_notifications()
            if i == 12:
                self.watch_chats()
            if i == 13:
                self.add_post_in_group()
            if i == 14:
                self.check_group_inbox()
            if i == 15:
                self.check_group_notifications()
            if i == 16:
                self.like_group_post()

        print('Finish Random Actions')

    def clean_monitor(self):
        self.facebookPage.clean_monitor()

    def add_random_friends(self):
        if self.facebookPage.go_to_friends_page():
            print("Add random friends")
            self.addFriendsPage.add_random_friends()
            self.addFriendsPage.to_main()

    def make_a_post(self):
        print("Make a post")
        self.facebookPage.make_a_post()

    def watch_user_page(self):
        print("Watch user page")
        self.facebookPage.go_to_user_page()
        self.userPage.scroll()
        self.userPage.to_main()

    def add_comment(self):
        print("Add comment")
        self.facebookPage.add_comment()

    def like_random_posts(self):
        print("Like random posts")
        self.facebookPage.like_random_posts()

    def go_to_random_friend(self):
        print('Go to random friend')
        self.facebookPage.go_to_user_page()
        self.userPage.go_to_friends_page()
        self.userFriendsPage.go_to_random_friend()
        self.userFriendsPage.to_main()

    def open_image(self):
        self.facebookPage.open_image()

    def watch_stories(self):
        self.facebookPage.watch_stories()

    def go_to_advertising_page(self):
        self.facebookPage.go_to_advertising_page()

    def go_to_link(self):
        self.facebookPage.go_to_link()

    def watch_notifications(self):
        self.facebookPage.watch_notifications()

    def watch_chats(self):
        self.facebookPage.watch_chats()

    def random_scroll(self):
        print("Random scroll")
        self.facebookPage.random_scroll()

    def add_post_in_group(self):
        self.facebookPage.go_to_image()
        self.imagePage.download_image()
        self.imagePage.to_facebook()
        if self.facebookPage.go_to_group():
            print("Post in group")
            self.groupPage.post()
            self.groupPage.to_main()

    def check_group_inbox(self):
        if self.facebookPage.go_to_group():
            print("Check group income")
            self.groupPage.check_group_inbox()
            self.groupPage.to_main()

    def check_group_notifications(self):
        if self.facebookPage.go_to_group():
            print("Check group notifications")
            self.groupPage.check_group_notifications()
            self.groupPage.to_main()

    def like_group_post(self):
        if self.facebookPage.go_to_group():
            print("Like group posts")
            self.groupPage.like_group_posts()
            self.groupPage.to_main()

    def exit(self):
        print("Exit")
        self.driver.quit()
