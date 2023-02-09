from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage

class TestInteractions:
    class TestSortablePage:
        def test_sortable_page(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after
            assert grid_before != grid_after

    class TestSelectablePage:
        def test_selectable_page(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0
            assert len(item_grid) > 0

    class TestResizablePage:
        def test_resizable_page(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box
            assert ('150px', '150px') == min_box
            assert min_resize != max_resize


    class TestDroppablePage:
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "The element has not dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept_text, accept_text = droppable_page.drop_accept()
            assert not_accept_text == 'Drop here', "the dropped element has been accepted"
            assert accept_text == 'Dropped!', "The dropped element has not been dropped"


        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == "Dropped!", "The elements text has not been changed"
            assert not_greedy_inner == "Dropped!", "The elements text has not been changed"
            assert greedy == "Outer droppable", "The elements text has been changed"
            assert greedy_inner == "Dropped!", "The elements text has not been changed"


        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable()
            after_move, last_position = droppable_page.drop_not_revert_draggable()
            assert will_after_move != will_after_revert, "Element has not reverted"
            assert after_move == last_position, "Element has not fixed"







# pytest -s -v tests/interactions_test.py::TestInteractions::TestSortablePage::test_sortable_page
# pytest -s -v tests/interactions_test.py::TestInteractions::TestSelectablePage::test_selectable_page
# pytest -s -v tests/interactions_test.py::TestInteractions::TestResizablePage::test_resizable_page
# pytest -s -v tests/interactions_test.py::TestInteractions::TestDroppablePage