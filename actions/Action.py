import random
import time

from selenium import webdriver
from page.FacebookPage import FacebookPage
from page.AddFriendsPage import AddFriendsPage
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
        self.user_page = UserPage(self.driver)
        self.user_friends_page = UserFriendsPage(self.driver)

    def open_page(self, page_url):
        print("Open page ", page_url)
        self.driver.get(page_url)

    def login(self, user, password):
        return
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
        self.facebookPage.clean_monitor()

        i = 0
        while i < 15:
            i = random.randrange(16)
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
            #if i == 9:
                #self.go_to_advertising_page()
            if i == 10:
                self.go_to_link()

        print('Finish Random Actions')

    def add_random_friends(self):
        if self.facebookPage.go_to_friends_page():
            print("Add random friends")
            time.sleep(1)
            self.addFriendsPage.add_random_friends()
            time.sleep(1)
            self.addFriendsPage.to_main()
            time.sleep(1)

    def make_a_post(self):
        print("Make a post")
        self.facebookPage.make_a_post()

    def watch_user_page(self):
        print("Watch user page")
        self.facebookPage.go_to_user_page()
        time.sleep(1)
        self.user_page.scroll()
        time.sleep(1)
        self.user_page.to_main()
        time.sleep(1)

    def add_comment(self):
        print("Add comment")
        self.facebookPage.add_comment()

    def like_random_posts(self):
        print("Like random posts")
        self.facebookPage.like_random_posts()

    def go_to_random_friend(self):
        print('Go to random friend')
        self.facebookPage.go_to_user_page()
        time.sleep(1)
        self.user_page.go_to_friends_page()
        time.sleep(1)
        self.user_friends_page.go_to_random_friend()
        time.sleep(1)
        self.user_friends_page.to_main()
        time.sleep(1)

    def open_image(self):
        self.facebookPage.open_image()

    def watch_stories(self):
        self.facebookPage.watch_stories()

    def go_to_advertising_page(self):
        self.facebookPage.go_to_advertising_page()

    def go_to_link(self):
        self.facebookPage.go_to_link()

    def exit(self):
        print("Exit")
        self.driver.quit()
