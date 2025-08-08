from pages.LoginPage import LoginPage
from testcases.conftest import rp_logger


class Test_LoginPage:

    def test_goto_test_login_page(self, page, rp_logger):
        login = LoginPage(page)
        rp_logger.info("Login Test Case Started")
        #page.pause()    # The below pause is used to pause the test execution in Playwright Inspector
        title = login.navigate_to_test_login_page()
        assert title == "Test Login Page for Automation Testing Practice", f"Unexpected title {title}"