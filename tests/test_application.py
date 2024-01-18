import pytest

from screens.play_store_modal import PlayStoreModal


@pytest.mark.usefixtures("appium_driver")
class TestApplication:

    def test_app(self, appium_driver):
        play_store_modal = PlayStoreModal(appium_driver)
        is_modal_displayed = (play_store_modal
                              .decline_play_store_installation()
                              .click_play_button()
                              .is_enter_name_modal_displayed())

        assert is_modal_displayed, "Enter your name modal should be displayed"
