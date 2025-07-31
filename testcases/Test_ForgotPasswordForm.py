from pages.ForgotPasswordPage import ForgotPasswordPage
from testcases.conftest import rp_logger

class Test_ForgotPasswordForm:

    def test_forgot_password_form(self, page, rp_logger):
        rp_logger.info("Navigating to Forgot Password Form")
        forgot_password_page = ForgotPasswordPage(page)
        forgot_password_page.navigate_to_forgot_password_page()
        rp_logger.info("Forgot Password Form navigation successful")
        rp_logger.info("Entering email and retrieving password")
        forgot_password_page.enter_email("a@a.in")
        forgot_password_page.click_retrieve_password()
        rp_logger.info("Email entered and retrieve password clicked")
        # rp_logger.info("Verifying retrieve password confirmation message")
        # confirmation_text = forgot_password_page.get_text("password_retrieved_message_XPATH")
        # assert "An e-mail has been sent to you which explains how to reset your password" in confirmation_text.strip(), \
        #     f"Unexpected confirmation message: {confirmation_text}"
        # rp_logger.info("Retrieve password confirmation verified successfully")


