from playwright.sync_api import expect

from testcases.conftest import rp_logger
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

    def get_text(self, locator):
        return self.page.locator(ConfigReader.read_config("locators",locator)).inner_text()

    def get_text_from_first_p_tag(self, locator):
        return self.page.locator(ConfigReader.read_config("locators", locator)).first.inner_text()

    def is_visible(self, locator):
        locator = self.page.locator(ConfigReader.read_config("locators", locator))
        # locator.wait_for(state="visible", timeout=5000)
        expect(locator).to_be_visible(timeout=5000)
        return locator.is_visible()
