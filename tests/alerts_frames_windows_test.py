import time
from pages.alerts_frames_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, ModalDialogsPage


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

    class TestFramePage:

        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame does not exist"

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame"
            assert child_text == "Child Iframe"

    class TestModalDialogsPage:

        def test_modal_small_dialog(self, driver):
            modal_dialog = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog.open()
            title_res, text_res = modal_dialog.check_modal_small_dialog()
            assert title_res == "Small Modal"
            assert text_res == "This is a small modal. It has very less content"

        def test_modal_large_dialog(self, driver):
            modal_dialog = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog.open()
            title_res, len_text_res = modal_dialog.check_modal_large_dialog()
            assert title_res == "Large Modal"
            assert len_text_res == 574








# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestBrowserWindows::test_new_tab
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestBrowserWindows::test_window
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestAlertsPage::test_see_alert
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestAlertsPage::test_alert_appear_after_five_sec
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestAlertsPage::test_confirm_alert_appeared
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestAlertsPage::test_prompt_alert_box_appeared
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestFramePage::test_frames
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestNestedFramesPage::test_nested_frames
# pytest -s -v tests/alerts_frames_windows_test.py::TestAlertsFramesWindows::TestModalDialogsPage::test_modal_small_dialog