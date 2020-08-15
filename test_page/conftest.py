import pytest
from utilities.webdriver_fac import webdriverfactory

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request,browser):
    wd=webdriverfactory()
    driver=wd.webdriver_instance(browser)
    if request.cls is not None:
        request.cls.driver=driver
    yield driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
