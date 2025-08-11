import inspect
import pytest
from pytest_check import check
from pages.LoginPage import LoginPage
from testcases.conftest import rp_logger


class Test_LoginPage:
    @pytest.mark.smoke
    def test_goto_test_login_page(self, page, rp_logger):
        try:
            login = LoginPage(page)
            rp_logger.info("Login Test Case Started")
            #page.pause()    # The below pause is used to pause the test execution in Playwright Inspector
            title = login.navigate_to_test_login_page()
            expected_title = "Test Login Page for Automation Testing Practice"
            check.equal(title, expected_title, f"Expected title '{expected_title}' but got '{title}'")
            # expect(title).to_contain("Test Login Page for Automation Testing Practice")
            rp_logger.info("Login Test Case Completed Successfully")
        except:
            # Get the name of the currently executing function (useful for logging test name)
            test_name = inspect.currentframe().f_code.co_name
            rp_logger.error(f"Test Case {test_name} failed with exception")
            check.fail(f"Test Case {test_name} failed with exception")