from testcases.conftest import rp_logger
from pages.DynamicTablePage import DynamicTablePage

class Test_DynamicTablePage:

    def test_dynamic_table_page(self, page, rp_logger):
        rp_logger.info("Navigating to Dynamic Table Page")
        dynamic_table_page = DynamicTablePage(page)
        dynamic_table_page.navigate_to_dynamic_table_page()
        rp_logger.info("Dynamic Table Page navigation successful")
        rp_logger.info("Retrieving Chrome CPU load from the table")
        if dynamic_table_page.validate_table_is_visible():
            cpu_value_from_table = dynamic_table_page.get_value_of_Chrome_CPU_load_from_table()
            rp_logger.info("Chrome CPU load retrieved from the table")
            cpu_value_from_yellow_section = dynamic_table_page.get_value_of_Chrome_CPU_load_from_yellow_row()
            rp_logger.info("Chrome CPU load retrieved from the yellow row")
            rp_logger.info("Validating CPU load values")
            assert cpu_value_from_table == cpu_value_from_yellow_section,f"Mismatch! Table: {cpu_value_from_table}, Label: {cpu_value_from_yellow_section}"
            rp_logger.info("CPU load values match successfully")
        else:
            rp_logger.error("Dynamic table is not visible on the page, test failed")
            assert False, "Dynamic table is not visible on the page"



