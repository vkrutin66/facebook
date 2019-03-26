import random
import platform
from threading import Timer

from selenium import webdriver
from page.FacebookPage import FacebookPage
from page.AddFriendsPage import AddFriendsPage
from page.GroupPage import GroupPage
from page.ImagePage import ImagePage
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
            if platform.system() == 'Windows':
                self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe", chrome_options=options)
            else:
                self.driver = webdriver.Chrome(executable_path="drivers/chromedriver_mac", chrome_options=options)

        print("Open browser ", browser)
        self.driver.maximize_window()

        self.facebookPage = FacebookPage(self.driver)
        self.addFriendsPage = AddFriendsPage(self.driver)
        self.userPage = UserPage(self.driver)
        self.userFriendsPage = UserFriendsPage(self.driver)
        self.groupPage = GroupPage(self.driver)
        self.imagePage = ImagePage(self.driver)

        self.end_of_test = False

    def open_page(self, page_url):
        print("Open page ", page_url)
        self.driver.get(page_url)

    def random_actions(self):
        print('Start Random Actions')
        self.clean_monitor()

        i = 0
        Timer(300.0, self.timer_over).start()
        while i < 16:
            i = random.randrange(15)
            i = 12
            if self.end_of_test:
                i = random.randrange(50)
            if i == 1:
                self.make_a_post()              # from video 2:55, from doc 1-7
            if i == 2:
                self.watch_user_page()          # from video 0.40, from doc 1-1
            if i == 3:
                self.add_comment()              # from video 0.57
            if i == 4:
                self.like_random_posts()        # from video 0.55
            if i == 5:
                self.go_to_random_friend()      # from video 2:30, from doc 1-6
            if i == 6:
                self.open_image()               # from video 1:05
            if i == 7:
                self.watch_stories()            # from video 3:15, from doc 1-8
            if i == 8:
                self.random_scroll()            # from video 1:20, from doc 1-2, 1-3
            if i == 9:
                self.go_to_link()               # from video 1:30, from doc 1-4
            if i == 10:
                self.watch_notifications()      # from video 3:40, from doc 1-10
            if i == 11:
                self.watch_chats()              # from video 3:30, from doc 1-9
            if i == 12:
                self.add_post_in_group()        # from video 5:30, from doc 5, 6
            if i == 13:
                self.check_group_inbox()        # from video 4:40
            if i == 14:
                self.check_group_notifications()  # from video 4:45
            if i == 15:
                self.like_group_post()          # from video 4:38

        print('Finish Random Actions')

    def timer_over(self):
        self.end_of_test = True

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
        self.userPage.scroll(random.randrange(10000))
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
