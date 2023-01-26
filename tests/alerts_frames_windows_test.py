import time
from pages.alerts_frames_windows_page import BrowserWindowsPage


class TestAlertsFramesWindows:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_new = new_tab_page.check_opened_new_tab()
            assert text_new == "This is a sample page", "New tap did not open"

        def test_window(self, driver):
            new_window = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window.open()
            text_new = new_window.check_opened_new_window()
            assert text_new == "This is a sample page", "New tap did not open"



# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestBrowserWindows::test_new_tab
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestBrowserWindows::test_window