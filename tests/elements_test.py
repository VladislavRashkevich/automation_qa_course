import time

from pages.elements_page import TextBoxPage


def test_text_box(driver):
    text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
    text_box_page.open()
    full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
    output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
    assert full_name == output_name, "the full_name does not mathc"
    assert email == output_email, "the email does not mathc"
    assert current_address == output_cur_addr, "the current_url does not mathc"
    assert permanent_address == output_per_addr, "the permanent does not mathc"
