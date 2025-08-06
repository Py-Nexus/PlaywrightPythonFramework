from pages.BasePage import BasePage
import re
class ForgotPasswordPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_forgot_password_page(self):
        self.click("tryout_forgot_password_form_XPATH")
        title = self.page.title()
        return title

    def enter_email(self, email):
        self.type("email_input_id", email)

    def click_retrieve_password(self):
        self.click("retrieve_password_button_XPATH")

    def get_retrieval_message(self):
        p_text = self.get_text_from_first_p_tag("password_retrieved_message_CSS")
        p_text=re.sub(r'\s+', ' ', p_text).strip()
        return p_text