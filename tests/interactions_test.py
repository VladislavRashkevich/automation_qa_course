from pages.interactions_page import SortablePage, SelectablePage, ResizablePage

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






# pytest -s -v tests/interactions_test.py::TestInteractions::TestSortablePage::test_sortable_page
# pytest -s -v tests/interactions_test.py::TestInteractions::TestSelectablePage::test_selectable_page
# pytest -s -v tests/interactions_test.py::TestInteractions::TestResizablePage::test_resizable_page