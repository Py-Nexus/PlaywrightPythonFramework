from pages.BasePage import BasePage

class ForgotPasswordPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_forgot_password_page(self):
        self.click("tryout_forgot_password_form_XPATH")
        title = self.page.title()
        assert title == "Forgot Password form page for Automation Testing Practice", f"Unexpected title {title}"

    def enter_email(self, email):
        self.type("email_input_id", email)

    def click_retrieve_password(self):
        self.click("retrieve_password_button_XPATH")