import inspect
from testcases.conftest import rp_logger
from pages.DynamicTablePage import DynamicTablePage

class Test_DynamicTablePage:

    def test_dynamic_table_page(self, page, rp_logger):
        try:
            rp_logger.info("Navigating to Dynamic Table Page")
            dynamic_table_page = DynamicTablePage(page)
            title = dynamic_table_page.navigate_to_dynamic_table_page()
            assert title == "Dynamic Tables page for Automation Testing Practice", f"Unexpected title {title}"
            rp_logger.info("Dynamic Table Page navigation successful")
            rp_logger.info("Retrieving Chrome CPU load from the table")
            dynamic_table_page.validate_table_is_visible()
            cpu_value_from_table = dynamic_table_page.get_value_of_Chrome_CPU_load_from_table()
            rp_logger.info("Chrome CPU load retrieved from the table")
            cpu_value_from_yellow_section = dynamic_table_page.get_value_of_Chrome_CPU_load_from_yellow_row()
            rp_logger.info("Chrome CPU load retrieved from the yellow row")
            rp_logger.info("Validating CPU load values")
            assert cpu_value_from_table == cpu_value_from_yellow_section,f"Mismatch! Table: {cpu_value_from_table}, Label: {cpu_value_from_yellow_section}"
        except Exception as e:
            # Get the name of the currently executing function (useful for logging test name)
            test_name = inspect.currentframe().f_code.co_name
            rp_logger.error(f"Test Case {test_name} failed with exception: {e}")
            assert False, f"Test Case {test_name} failed with exception: {e}"




