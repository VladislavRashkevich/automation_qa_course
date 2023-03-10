import random
import time

from pages.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, SelectMenuPageLocators
from selenium.common import TimeoutException
from generator.generator import generated_color, generated_date, generate_select_menu_value


class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {
            'first':
                {'title': self.locators.TITLE_SECTION_FIRST,
                 'content': self.locators.CONTENT_SECTION_FIRST},
            'second':
                {'title': self.locators.TITLE_SECTION_SECOND,
                 'content': self.locators.CONTENT_SECTION_SECOND},
            'third':
                {'title': self.locators.TITLE_SECTION_THIRD,
                 'content': self.locators.CONTENT_SECTION_THIRD
                 }
        }

        section_title = self.element_is_present(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text

        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):

    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drug_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after



class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        tabs = {
            'what':
                {'title': self.locators.TABS_WHAT,
                 'content': self.locators.TABS_WHAT_CONTENT},
            'origin':
                {'title': self.locators.TABS_ORIGIN,
                 'content': self.locators.TABS_ORIGIN_CONTENT},
            'use':
                {'title': self.locators.TABS_USE,
                 'content': self.locators.TABS_USE_CONTENT
                 },
            'more':
                {'title': self.locators.TABS_MORE,
                 'content': self.locators.TABS_MORE_CONTENT
                 }
        }

        tabs_button = self.element_is_visible(tabs[name_tab]['title'])
        tabs_button.click()
        tabs_content = self.element_is_visible(tabs[name_tab]['content']).text
        return tabs_button.text, len(tabs_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK, self.locators.TOOL_TIP_CONTRARY_LINK)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION_LINK)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section
    

class MenuPage(BasePage):

    locators = MenuPageLocators()

    def check_menu_title(self):
        menu_elements = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        menu_title_list = []
        for element in menu_elements:
            self.action_move_to_element(element)
            menu_title_list.append(element.text)
        return menu_title_list

class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def check_select_value(self):
        input_values = next(generate_select_menu_value()).list_values
        data = []
        for value in input_values:
            select_input = self.element_is_present(self.locators.SELECT_VALUE_FIELD_INPUT)
            select_input.send_keys(value)
            select_input.send_keys(Keys.ENTER)
            text_output = self.element_is_present(self.locators.SELECT_VALUE_FIELD_OUTPUT).text
            data.append(text_output)
        return input_values, data

    def check_select_one_menu(self):
        menu_val = random.choice(['Other', 'Prof.', 'Mrs.', 'Mr.', 'Mr.', 'Dr.'])

        input_field = self.element_is_present(self.locators.SELECT_ONE_MENU_INPUT)
        input_field.send_keys(menu_val)
        input_field.send_keys(Keys.ENTER)
        output_val = self.element_is_present(self.locators.SELECT_ONE_MENU_OUTPUT).text
        return [menu_val, output_val]

    def check_old_select_menu(self):
        elem = self.element_is_present(self.locators.OLD_SELECT_MENU)
        value_data_before = elem.get_attribute('value')
        select = Select(elem)
        select.select_by_value(str(random.randint(1, 10)))
        value_data_after = elem.get_attribute('value')
        return value_data_before, value_data_after


    def check_multiselect_drop_down(self):
        values = ["Green", "Blue", "Black", "Red"]
        colors = random.sample(values, k=random.randint(1, 3))
        for color in colors:
            input_field = self.element_is_visible(self.locators.MULTISELECT_INPUT)
            input_field.send_keys(color)
            input_field.send_keys(Keys.ENTER)

        checked_colors_list = self.elements_are_visible(self.locators.MULTISELECT_COLORS_CHECKED_LIST)
        data = []
        for elem in checked_colors_list:
            data.append(elem.text)
        return colors, data

    def check_delete_button_in_multiselect(self):
        values = ["Green", "Blue", "Black", "Red"]
        colors = random.sample(values, k=random.randint(1, 4))
        for color in colors:
            input_field = self.element_is_visible(self.locators.MULTISELECT_INPUT)
            input_field.send_keys(color)
            input_field.send_keys(Keys.ENTER)

        multiselect_container = self.elements_are_present(self.locators.CONTAINERS_FOR_SELECT)[2]
        delete_button = multiselect_container.find_elements(*self.locators.INDICATOR_FOR_TEARDOWN_LIST)[-2]
        delete_button.click()
        try:
            len_checked_colors_list_after = len(self.elements_are_invisible(self.locators.MULTISELECT_COLORS_CHECKED_LIST))
        except TimeoutException:
            return 0

        return len_checked_colors_list_after



    def check_standard_multi_select(self):
        elem = self.element_is_present(self.locators.STANDARD_MULTI_SELECT)
        value_data_before = elem.get_attribute('value')
        select = Select(elem)
        select.select_by_index(random.randint(0, 3))
        value_data_after = elem.get_attribute('value')
        return value_data_before, value_data_after


















