import time
from pages.form_page import FormPage


class TestForm:

    class TestFormPage:
        def test_form(self, driver):
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            form_page.fill_form_fields()
            time.sleep(5)


# pytest -s -v tests/form_test.py::TestForm::TestFormPage::test_form