import pytest
import os
import logging
import shutil
from selenium import webdriver
from datetime import datetime
import allure

# Optional: browser service & options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# === Function: Clean old folders, keep latest N ===
def cleanup_old_folders(parent_dir, keep_latest=7):
    try:
        folders = [
            os.path.join(parent_dir, d)
            for d in os.listdir(parent_dir)
            if os.path.isdir(os.path.join(parent_dir, d))
        ]
        folders.sort(key=os.path.getmtime, reverse=True)
        for old_folder in folders[keep_latest:]:
            shutil.rmtree(old_folder)
            print(f"Deleted old folder: {old_folder}")
    except Exception as e:
        print(f"Error cleaning {parent_dir}: {str(e)}")

# === Function: Get timestamped screenshot name ===
def get_timestamped_name(test_name: str, status: str) -> str:
    now = datetime.now()
    return f"{test_name}_{status}_{now.strftime('%Y_%m_%d_%H_%M-%S')}"

# === Project Paths and Folder Creation ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

report_dir = os.path.join(BASE_DIR, 'reports', timestamp)
log_dir = os.path.join(BASE_DIR, 'logs', timestamp)
screenshot_dir = os.path.join(BASE_DIR, 'screenshots', timestamp)

# Clean old folders
cleanup_old_folders(os.path.join(BASE_DIR, 'reports'))
cleanup_old_folders(os.path.join(BASE_DIR, 'logs'))
cleanup_old_folders(os.path.join(BASE_DIR, 'screenshots'))

# Create new timestamped folders
for path in [report_dir, log_dir, screenshot_dir]:
    os.makedirs(path, exist_ok=True)

# Logging configuration
log_file = os.path.join(log_dir, 'test.log')
logging.basicConfig(
    filename=log_file,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# === PyTest Hook: Add CLI option for browser ===
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to use: chrome, firefox, edge"
    )

# === PyTest Hook: Capture test result pass/fail ===
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# === PyTest Fixture: Setup browser, teardown, attach logs/screenshots ===
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser").lower()
    logging.info(f"Selected browser: {browser_name}")

    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)

    else:
        raise Exception(f"Unsupported browser: {browser_name}")

    driver.get("https://automationexercise.com/")
    request.cls.driver = driver
    yield

    test_name = request.node.name
    status = "fail" if hasattr(request.node, "rep_call") and request.node.rep_call.failed else "pass"
    screenshot_name = get_timestamped_name(test_name, status) + ".png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)

    try:
        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved: {screenshot_path}")
        with open(screenshot_path, "rb") as img:
            allure.attach(img.read(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        logging.error(f"Screenshot or Allure attach failed: {e}")

    driver.quit()
    logging.info("Browser closed")
