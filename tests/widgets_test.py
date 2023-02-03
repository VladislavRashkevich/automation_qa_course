

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, ToolTipsPage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian_page(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0


    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result


        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result


    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, "Date has not been change"

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, "Date and time has not been change"


    class TestSliderPage:

        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after


    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after


    class TestTabsPage:
        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            # more_button, more_content = tabs.check_tabs('more')
            assert what_button == "What", what_content > 0
            assert origin_button == "Origin", origin_content > 0
            assert use_button == "Use", use_content > 0


    class TestToolTipsPage:
        def test_tool_tips(self, driver):
            tool_tips = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips.open()
            button_text, field_text, contrary_text, section_text = tool_tips.check_tool_tips()




# pytest -s -v tests/widgets_test.py::TestWidgets::TestAccordianPage::test_accordian_page
# pytest -s -v tests/widgets_test.py::TestWidgets::TestAutoCompletePage::test_fill_multi_autocomplete
# pytest -s -v tests/widgets_test.py::TestWidgets::TestDatePickerPage::test_change_date
# pytest -s -v tests/widgets_test.py::TestWidgets::TestDatePickerPage::test_change_date_and_time
# pytest -s -v tests/widgets_test.py::TestWidgets::TestSliderPage::test_slider
# pytest -s -v tests/widgets_test.py::TestWidgets::TestProgressBarPage::test_progress_bar
# pytest -s -v tests/widgets_test.py::TestWidgets::TestTabsPage::test_tabs
# pytest -s -v tests/widgets_test.py::TestWidgets::TestToolTipsPage::test_tool_tips





