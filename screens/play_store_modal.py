from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from screens.base_screen import BaseScreen
from screens.home_screen import HomeScreen


class PlayStoreModal(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

    def decline_play_store_installation(self):
        cancel_button = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((AppiumBy.ID, "android:id/button2")))
        cancel_button.click()
        return HomeScreen(self.driver)
