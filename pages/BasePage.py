from utilities import ConfigReader


class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(ConfigReader.read_config("locators",locator)).click()

    def type(self, locator, value):
        self.page.locator(ConfigReader.read_config("locators",locator)).fill(value)

    def move_to(self, locator):
        self.page.locator(ConfigReader.read_config("locators",locator)).hover()

