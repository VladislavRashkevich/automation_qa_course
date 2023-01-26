import time
from pages.alerts_frames_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFramesWindows:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_new = new_tab_page.check_opened_new_tab_window('new_tab')
            assert text_new == "This is a sample page", "New tap did not open"

        def test_window(self, driver):
            new_window = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window.open()
            text_new = new_window.check_opened_new_tab_window('new_window')
            assert text_new == "This is a sample page", "New tap did not open"


    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_is_open()
            assert alert_text == 'You clicked a button', "Alert did not open"

        def test_alert_appear_after_five_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_appear_alert_open_after_five_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Alert did not appear after 5 second"

        def test_confirm_alert_appeared(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_result, action = alert_page.check_confirm_box_alert()
            assert text_result == f'You selected {action}'

        def test_prompt_alert_box_appeared(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_result, input_string = alert_page.check_prompt_box_alert()
            assert text_result == f"You entered {input_string}"






# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestBrowserWindows::test_new_tab
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestBrowserWindows::test_window
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestAlertsPage::test_see_alert
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestAlertsPage::test_alert_appear_after_five_sec
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestAlertsPage::test_confirm_alert_appeared
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestAlertsPage::test_prompt_alert_box_appeared