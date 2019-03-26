import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locator.Locator import Locator


class Page:

    logo = Locator("CSS", "._19eb")

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(locator.get_by(), locator.get_name())

    def get_elements(self, locator):
        return self.driver.find_elements(locator.get_by(), locator.get_name())

    def wait(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((locator.get_by(), locator.get_name())))

    def wait_to_be_click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((locator.get_by(), locator.get_name())))

    def wait_to_disappear(self, locator):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.invisibility_of_element((locator.get_by(), locator.get_name())))

    def exists(self, locator):
        try:
            self.get_element(locator)
        except NoSuchElementException:
            return False
        return True

    def scroll(self, length):
        scrolled = 0
        while scrolled < length:
            scrolled += 10
            self.driver.execute_script("window.scrollTo(0, " + str(scrolled) + ");")
            time.sleep(0.075)

    def to_main(self):
        self.get_element(self.logo).click()
        time.sleep(1)
