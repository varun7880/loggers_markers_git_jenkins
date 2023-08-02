import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options

# add arg --broswer
def pytest_addoption(parser):
    parser.addoption("--browser")


# passing the value to --browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# here we are passing actual value to --broswer
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome ")
    elif browser == 'firefox':
        options = Options()
        options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        driver = webdriver.Firefox(options=options)
        print("Launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("headlessmode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    return driver


def pytest_metadata(metadata):
    # To Add
    metadata["Class"] = "Credence"
    metadata["Batch"] = "CT#15"
    metadata["URL"] = "https://automation.credence.in"
    # To Remove
    metadata.pop("Platform", None)


# How to edit Summary in html report this is your today's task

# use parameter when you have small data set
@pytest.fixture(params=[
    ("Credencetest@test.com", "Credence@123"),
    ("Credencetest@test.com1", "Credence@123"),
    ("Credencetest@test.com", "Credence@1231"),
    ("Credencetest@test.com1", "Credence@1231")
])
def getDataforLogin(request):
    return request.param
