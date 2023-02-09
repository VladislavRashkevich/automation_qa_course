import random
import time

from pages.base_page import BasePage
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, DroppablePageLocators, DraggablePageLocators


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drug_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drug_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def _click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self._click_selectable_item(self.locators.LIST_ITEMS)
        active_element = self.element_is_visible(self.locators.LIST_ITEMS_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self._click_selectable_item(self.locators.GRID_ITEMS)
        active_element = self.element_is_visible(self.locators.GRID_ITEMS_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):

        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height


    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 300, 100)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE), random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE), random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drug_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drug_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drug_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_not_accept, drop_text_accept

    def drop_prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drug_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drug_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box


    def drop_revert_draggable(self):
        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        will_revert = self.element_is_visible(self.locators.WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drug_and_drop_to_element(will_revert, drop_div)
        position_after_move = will_revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert.get_attribute('style')
        return position_after_move, position_after_revert

    def drop_not_revert_draggable(self):
        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        not_revert = self.element_is_visible(self.locators.NOT_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drug_and_drop_to_element(not_revert, drop_div)
        position_after_move = not_revert.get_attribute('style')
        time.sleep(1)
        last_position = not_revert.get_attribute('style')
        return position_after_move, last_position


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    def _action_drug_and_drop_by_random_offset(self, element, max_pixel_to_move=300):
        x_coords = random.randint(1, max_pixel_to_move)
        y_coords = random.randint(1, max_pixel_to_move)
        self.action_drug_and_drop_by_offset(element, x_coords, y_coords)

    def _get_x_and_y_cord_in_px(self, element):
        coords = element.get_attribute('style')
        if len(coords.split(";")) <= 2:
            x_cor = "0px"
            y_cor = "0px"
        else:
            x_cor = coords.replace(" ", "").split(";")[1].split(":")[1]
            y_cor = coords.replace(" ", "").split(";")[2].split(":")[1]
        return x_cor, y_cor


    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_element = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        first_position = drag_element.get_attribute('style')
        self._action_drug_and_drop_by_random_offset(drag_element)
        last_position = drag_element.get_attribute('style')
        return first_position, last_position

    def drop_axis_restricted(self, x_or_y="x"):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()

        element_x_or_y = {
            "x": self.locators.ONLY_X,
            "y": self.locators.ONLY_Y
        }
        elem_axis = self.element_is_visible(element_x_or_y[x_or_y.lower()])
        first_left, first_top = self._get_x_and_y_cord_in_px(elem_axis)
        self._action_drug_and_drop_by_random_offset(elem_axis)
        last_left, last_top = self._get_x_and_y_cord_in_px(elem_axis)
        return first_left, first_top, last_left, last_top

    def dragging_container_within_container(self):
        self.element_is_visible(self.locators.CONTAINER_RESTRICTED_TAB).click()
        box_in_container = self.element_is_clickable(self.locators.ELEMENT_CONTAINED_BOX)
        self.action_drug_and_drop_by_offset(box_in_container, 450, 115)
        x_coor_max, y_coor_max = self._get_x_and_y_cord_in_px(box_in_container)
        self.action_drug_and_drop_by_offset(box_in_container, -450, -150)
        x_coor_min, y_coor_min = self._get_x_and_y_cord_in_px(box_in_container)
        return x_coor_max, y_coor_max, x_coor_min, y_coor_min

    def dragging_element_withing_parent(self):
        element_in_parent = self.element_is_visible(self.locators.ELEMENT_CONTAINED_PARENT)
        self.action_drug_and_drop_by_offset(element_in_parent, 50, 115)
        elem_x_coor_max, elem_y_coor_max = self._get_x_and_y_cord_in_px(element_in_parent)
        self.action_drug_and_drop_by_offset(element_in_parent, -100, -100)
        elem_x_coor_min, elem_y_coor_min = self._get_x_and_y_cord_in_px(element_in_parent)
        return elem_x_coor_max, elem_y_coor_max, elem_x_coor_min, elem_y_coor_min










