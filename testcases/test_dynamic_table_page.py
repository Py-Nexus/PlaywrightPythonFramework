import inspect
from pytest_check import check
from testcases.conftest import rp_logger
from pages.DynamicTablePage import DynamicTablePage

class Test_DynamicTablePage:

    def test_dynamic_table_page(self, page, rp_logger):
        try:
            rp_logger.info("Navigating to Dynamic Table Page")
            dynamic_table_page = DynamicTablePage(page)
            title = dynamic_table_page.navigate_to_dynamic_table_page()
            check.equal(title, "Dynamic Tables page for Automation Testing Practice",
                        f"Expected title to be empty but got '{title}'")
            rp_logger.info("Dynamic Table Page navigation successful")
            dynamic_table_page.validate_table_is_visible()
            cpu_value_from_table = dynamic_table_page.get_value_of_Chrome_CPU_load_from_table()
            cpu_value_from_yellow_section = dynamic_table_page.get_value_of_Chrome_CPU_load_from_yellow_row()
            check.equal(cpu_value_from_table, cpu_value_from_yellow_section,
                        f"Expected CPU value from table '{cpu_value_from_table}' to match yellow section value '{cpu_value_from_yellow_section}'")
            rp_logger.info("CPU values matched successfully")
        except Exception as e:
            # Get the name of the currently executing function (useful for logging test name)
            test_name = inspect.currentframe().f_code.co_name
            rp_logger.error(f"Test Case {test_name} failed with exception: {e}")
            check.fail(f"Test Case {test_name} failed with exception: {e}")




