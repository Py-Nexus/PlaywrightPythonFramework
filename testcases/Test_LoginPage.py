from pages.LoginPage import LoginPage


class Test_LoginPage():


    def test_goto_test_login_page(self, page):
        print("I'm in Test_LoginPage")
        login = LoginPage(page)
        login.navigate_to_test_login_page()