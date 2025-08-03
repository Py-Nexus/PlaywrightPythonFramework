import logging
import os
# import allure
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
# from allure_commons.types import AttachmentType
from utilities import ConfigReader
from reportportal_client import RPLogger

BASE_DIR = Path(__file__).resolve().parent.parent
VIDEO_DIR = BASE_DIR / "videos"
SCREENSHOT_DIR = BASE_DIR / "screenshot"
TRACE_PATH = BASE_DIR / "trace.zip"

# Ensure necessary directories exist
VIDEO_DIR.mkdir(exist_ok=True)
SCREENSHOT_DIR.mkdir(exist_ok=True)

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(params=["chrome"], scope="function")
def browser(playwright_instance, request):
    browser_type = request.param

    if browser_type == "chrome":
        browser = playwright_instance.chromium.launch(headless=True)
    elif browser_type == "firefox":
        browser = playwright_instance.firefox.launch(headless=True)
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")

    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(record_video_dir=str(VIDEO_DIR))
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path=str(TRACE_PATH))
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.close()

@pytest.fixture(autouse=True)
def navigate_to_base_url(page):
    base_url = ConfigReader.read_config("basic info", "testsiteurl")
    page.goto(base_url)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Generates test result data for the current test item
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# @pytest.fixture()
# def log_on_failure(request, page):
#     yield
#     if request.node.rep_call.failed:
#         screenshot_file = SCREENSHOT_DIR / f"{request.node.name}_failure.png"
#         page.screenshot(path=str(screenshot_file), full_page=True)
#         allure.attach.file(
#             str(screenshot_file),
#             name="Failure Screenshot",
#             attachment_type=AttachmentType.PNG
#         )

@pytest.fixture(scope='session')
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


@pytest.fixture(autouse=True)
def skip_by_mark(request):
    if request.node.get_closest_marker('fixture_skip'):
        pytest.skip('skip by fixture')


@pytest.fixture(scope='session')
def rp_launch_id(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.launch_uuid


@pytest.fixture(scope='session')
def rp_endpoint(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.endpoint


@pytest.fixture(scope='session')
def rp_project(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.project
