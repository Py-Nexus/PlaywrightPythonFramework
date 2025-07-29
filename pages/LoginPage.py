from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_test_login_page(self):
        print("I'm in LoginPage")
        self.click("tryout_XPATH")
        title = self.page.title()
        assert title == "Automation Testing Practice Website for QA and Developers | UI and API",f"Unexpected title {title}"
