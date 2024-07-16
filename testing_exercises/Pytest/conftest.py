import pytest


@pytest.fixture(scope="session", autouse=True)
def tc_setup(browser):
    if browser == "chrome":
        print("Launch chrome")
    elif browser == "firefox":
        print("Launch firefox")
    else:
        print("Provide valid browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
