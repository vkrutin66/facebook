from selenium.webdriver.common.by import By


class Locator:
    def __init__(self, by_name, locator_name):
        self.by = {
            'XPATH': By.XPATH,
            'CLASS': By.CLASS_NAME,
            'CSS': By.CSS_SELECTOR,
            'ID': By.ID,
            'NAME': By.NAME
        }.get(by_name, By.ID)
        self.locator_name = locator_name

    def get_by(self):
        return self.by

    def get_name(self):
        return self.locator_name
