from screens.base_screen import BaseScreen
from utils.image_matcher import get_match_coordinates


class EnterNameScreen(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

    def is_enter_name_modal_displayed(self):
        max_loc = get_match_coordinates(self.driver, 'enter_name_template.png')
        return len(max_loc) != 0
