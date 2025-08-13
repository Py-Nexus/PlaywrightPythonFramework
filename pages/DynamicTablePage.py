from pages.BasePage import BasePage


class DynamicTablePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_dynamic_table_page(self):
        self.click("tryout_dynamic_table_XPATH")
        title = self.page.title()
        return title

    def validate_table_is_visible(self):
        assert self.is_visible("dynamic_table_className"), "Dynamic table is not visible on the page"

    def get_value_of_Chrome_CPU_load_from_table(self):
        _cpu_value_from_table = self.get_text("dynamic_chrome_CPU_table_row_XPATH").strip()
        return _cpu_value_from_table

    def get_value_of_Chrome_CPU_load_from_yellow_row(self):
        label_text = self.get_text("Chrome_CPU_value_XPATH")
        _cpu_value_from_yellow_row = label_text.split(":")[1].strip()
        return _cpu_value_from_yellow_row

    def validate_if_yellow_row_is_visible(self):
        assert self.is_visible("Chrome_CPU_value_XPATH"), "Yellow row is not visible on the page"

