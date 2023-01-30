from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.alerts_frames_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, NestedFramesPageLocators


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab_window(self, check_tab_window='new_tab'):
        """Select arg new_tab or new_window"""

        select_window = {
            'new_tab': self.locators.NEW_TAB_BUTTON,
            'new_window': self.locators.NEW_WINDOW_BUTTON
        }
        self.element_is_visible(select_window[check_tab_window]).click()
        self.go_to_new_windows()
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    # def check_opened_new_window(self):
    #     self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
    #     self.go_to_new_windows()
    #     text_title = self.element_is_present(self.locators.TITLE_NEW).text
    #     return text_title

class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def check_alert_is_open(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        # alert = self.driver.switch_to.alert
        alert = self.go_to_alert()
        alert_text = alert.text
        alert.accept()
        return alert_text

    def check_appear_alert_open_after_five_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        # alert = self.driver.switch_to.alert
        try:
            alert = self.alert_is_present(timeout=5.5)
        except TimeoutException:
            return False
        alert_text = alert.text
        alert.accept()
        return alert_text

    def check_confirm_box_alert(self, action="Ok"):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert = self.alert_is_present()
        if action == "Ok":
            alert.accept()
        else:
            alert.dismiss()
            action = "Cancel"
        result = self.element_is_visible(self.locators.ALERT_CONFIRM_RESULT).text
        return result, action

    def check_prompt_box_alert(self, string_to_input="John", action="Ok"):
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert = self.alert_is_present()
        if action == "Ok":
            alert.send_keys(string_to_input)
            alert.accept()
            text_result = self.element_is_visible(self.locators.ALERT_PROMPT_RESULT).text
            return text_result, string_to_input
        else:
            alert.dismiss()
            return False

class FramesPage(BasePage):

    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            return [text, width, height]

class NestedFramesPage(BasePage):

    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text




















