from core import WebPage, WebElement
from elements import NewsDetailedPageElements


class NewsDetailedPage(WebPage):
    title = 'USBC - блог деталка'
    path = '/local/layouts/news-detail.php#'

    go_to_catalog_button = WebElement(xpath=NewsDetailedPageElements.go_to_catalog_button)
    arrow_left_button = WebElement(xpath=NewsDetailedPageElements.arrow_left_button)
    arrow_right_button = WebElement(xpath=NewsDetailedPageElements.arrow_right_button)
    back_to_blog_button = WebElement(xpath=NewsDetailedPageElements.back_to_blog_button)

    current_slider = WebElement(xpath=NewsDetailedPageElements.current_slider)
    active_slider = WebElement(xpath=NewsDetailedPageElements.active_slider)
    next_slide = WebElement(xpath=NewsDetailedPageElements.next_slide)
    prev_slide = WebElement(xpath=NewsDetailedPageElements.prev_slide)
