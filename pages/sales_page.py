from elements import SalesPageElements
from core import WebPage, WebElement


class SalesPage(WebPage):
    left_arrow_button = WebElement(xpath=SalesPageElements.left_arrow_button)
    right_arrow_button = WebElement(xpath=SalesPageElements.right_arrow_button)
    active_slide = WebElement(xpath=SalesPageElements.active_slide)
    current_slide_number = WebElement(xpath=SalesPageElements.current_slide_number)
    total_slide_number = WebElement(xpath=SalesPageElements.total_slide_number)

    # pagination
    show_more_button = WebElement(xpath=SalesPageElements.show_more_button)
    next_page_button = WebElement(xpath=SalesPageElements.next_page_button)
    second_page_button = WebElement(xpath=SalesPageElements.second_page_button)
