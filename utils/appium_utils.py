from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.get_path import get_path


def initialize_appium_driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.udid = 'emulator-5554'
    options.app = f'{get_path()}/app/Manor Matters.apk'
    options.device_name = 'Pixel_6'
    options.automation_name = 'UiAutomator2'
    options.platformVersion = '13'

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    return driver
