from core import WebPage, WebElement
from elements import NewsPageElements


class NewsPage(WebPage):
    title = 'USBC - блог'
    path = '/local/layouts/news.php#'

    tag_0 = WebElement(xpath=NewsPageElements.tag_0)
    tag_1 = WebElement(xpath=NewsPageElements.tag_1)
    tag_2 = WebElement(xpath=NewsPageElements.tag_2)
    tag_3 = WebElement(xpath=NewsPageElements.tag_3)
    tag_4 = WebElement(xpath=NewsPageElements.tag_4)
    tag_5 = WebElement(xpath=NewsPageElements.tag_5)
    tag_6 = WebElement(xpath=NewsPageElements.tag_6)

    active_tag = WebElement(xpath=NewsPageElements.active_tag)
    disable_tag = WebElement(xpath=NewsPageElements.disable_tag)

    pagination_show_more_button = WebElement(xpath=NewsPageElements.pagination_show_more_button)
