from selenium.webdriver.common.by import By


class AccordianPageLocators:

    TITLE_SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    CONTENT_SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    TITLE_SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    CONTENT_SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    TITLE_SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    CONTENT_SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:

    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')

class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TABS_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TABS_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')

class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_CONTRARY_LINK = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, "//*[.='1.10.32']")
    TOOL_TIP_SECTION_LINK = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')

class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


class SelectMenuPageLocators:
    SELECT_VALUE_FIELD_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-2-input"]')
    SELECT_VALUE_FIELD_OUTPUT = (By.CSS_SELECTOR, 'div[id="withOptGroup"] div[class=" css-1uccc91-singleValue"]')

    SELECT_ONE_MENU_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_ONE_MENU_OUTPUT = (By.CSS_SELECTOR, 'div[id="selectOne"] div[class=" css-1uccc91-singleValue"]')

    OLD_SELECT_MENU = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')

    MULTISELECT_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    MULTISELECT_COLORS_CHECKED_LIST = (By.CSS_SELECTOR, 'div[class = "css-1rhbuit-multiValue"]')
    CONTAINERS_FOR_SELECT = (By.CSS_SELECTOR, 'div[class=" css-2b097c-container"]')
    INDICATOR_FOR_TEARDOWN_LIST = (By.CSS_SELECTOR, 'svg[class="css-19bqh2r"]')

    STANDARD_MULTI_SELECT = (By.CSS_SELECTOR, 'select[id="cars"]')




