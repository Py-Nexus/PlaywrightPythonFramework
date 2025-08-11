import logging
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from utilities import ConfigReader

# ====== Paths ======
BASE_DIR = Path(__file__).resolve().parent.parent
VIDEO_DIR = BASE_DIR / "videos"
SCREENSHOT_DIR = BASE_DIR / "screenshot"
TRACE_PATH = BASE_DIR / "trace.zip"

# Ensure necessary directories exist
VIDEO_DIR.mkdir(exist_ok=True)
SCREENSHOT_DIR.mkdir(exist_ok=True)
TRACE_PATH.parent.mkdir(exist_ok=True)

# ====== Pytest Configuration ======
def pytest_addoption(parser):
    parser.addoption(
        "--my-browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "webkit"],
        help="Browser to run tests on"
    )
# ====== Playwright Fixtures ======
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

# ====== Browser, Context, and Page Fixtures ======
@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    browser_type = request.config.getoption("--my-browser")
    if browser_type == "chrome":
        browser = playwright_instance.chromium.launch(headless=True)
    elif browser_type == "firefox":
        browser = playwright_instance.firefox.launch(headless=True)
    elif browser_type == "webkit":
        browser = playwright_instance.webkit.launch(headless=True)
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

# ====== ReportPortal Logger Fixture ======
@pytest.fixture(scope='session')
def rp_logger():
    logger = logging.getLogger("reportportal")
    logger.setLevel(logging.INFO)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

# ====== Optional: Skip Tests by Mark ======
@pytest.fixture(autouse=True)
def skip_by_mark(request):
    if request.node.get_closest_marker('fixture_skip'):
        pytest.skip('skip by fixture')

# ====== ReportPortal Session Fixtures ======
@pytest.fixture(scope='session')
def rp_launch_id(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.launch_id


@pytest.fixture(scope='session')
def rp_endpoint(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.endpoint


@pytest.fixture(scope='session')
def rp_project(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.project

# ====== Pytest Hook: Screenshot on Failure (Uploads to RP) ======
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure and attach to ReportPortal."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == "call" and rep.failed:
        page_fixture = item.funcargs.get("page", None)
        rp_logger_fixture = item.funcargs.get("rp_logger", None)
        if page_fixture:
            screenshot_file = SCREENSHOT_DIR / f"{item.name}_failure.png"
            page_fixture.screenshot(path=str(screenshot_file), full_page=True)
            if rp_logger_fixture:
                rp_logger_fixture.info(f"RP_MESSAGE#FILE#{screenshot_file}#Failure Screenshot")
                # ✅ Attach to ReportPortal as binary
                if rp_logger_fixture:
                    try:
                        with open(screenshot_file, "rb") as image_file:
                            rp_logger_fixture.info(
                                "Failure Screenshot",
                                extra={
                                    "attachment": {
                                        "name": f"{item.name}_failure.png",
                                        "data": image_file.read(),
                                        "mime": "image/png"
                                    }
                                }
                            )
                    except Exception as e:
                        rp_logger_fixture.error(f"Failed to attach screenshot to RP: {e}")