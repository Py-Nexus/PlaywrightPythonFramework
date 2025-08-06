import inspect

from pages.ForgotPasswordPage import ForgotPasswordPage
from testcases.conftest import rp_logger

class Test_ForgotPasswordForm:

    def test_forgot_password_form(self, page, rp_logger):
        try:
            rp_logger.info("Navigating to Forgot Password Form")
            forgot_password_page = ForgotPasswordPage(page)
            title = forgot_password_page.navigate_to_forgot_password_page()
            assert title == "Forgot Password form page for Automation Testing Practice", f"Unexpected title {title}"
            rp_logger.info("Forgot Password Form navigation successful")
            rp_logger.info("Entering email and retrieving password")
            forgot_password_page.enter_email("a@a.in")
            forgot_password_page.click_retrieve_password()
            rp_logger.info("Email entered and retrieve password clicked")
            rp_logger.info("Verifying retrieval message")
            p_text = forgot_password_page.get_retrieval_message()
            assert p_text == "An e-mail has been sent to you which explains how to reset your password.", f"Unexpected message: {p_text}"
            rp_logger.info("Retrieval message verified successfully")
        except Exception as e:
            # Get the name of the currently executing function (useful for logging test name)
            test_name = inspect.currentframe().f_code.co_name
            rp_logger.error(f"Test Case {test_name} failed with exception: {e}")
            assert False, f"Test Case {test_name} failed with exception: {e}"



