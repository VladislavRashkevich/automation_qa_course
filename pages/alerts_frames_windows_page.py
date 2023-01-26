from pages.base_page import BasePage
from locators.alerts_frames_windows_page_locators import BrowserWindowsPageLocators


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.go_to_new_windows()
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.go_to_new_windows()
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

