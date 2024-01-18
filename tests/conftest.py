import pytest

from utils.appium_utils import initialize_appium_driver


@pytest.fixture(scope="class")
def appium_driver(request):
    driver = initialize_appium_driver()

    def tear_down():
        driver.quit()

    request.addfinalizer(tear_down)
    return driver
