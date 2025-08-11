from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_test_login_page(self):
        self.click("tryout_XPATH")
        title = self.page.title()
        return title
