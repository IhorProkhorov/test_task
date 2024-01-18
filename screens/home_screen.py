import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from screens.base_screen import BaseScreen
from screens.enter_name_screen import EnterNameScreen
from utils.image_matcher import get_match_coordinates


class HomeScreen(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

    def click_play_button(self):
        max_loc = get_match_coordinates(self.driver, 'play_button_template.png')

        term_of_service = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value="//android.widget.LinearLayout[@resource-id='com.playrix."
                                                         "manormatters:id/buttons']/ android.widget.Button[@text='OK']")
        term_of_service.click()

        click_x, click_y = max_loc
        time.sleep(5)
        TouchAction(self.driver).tap(x=click_x, y=click_y).perform()
        return EnterNameScreen(self.driver)
