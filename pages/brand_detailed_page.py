from elements import BrandDetailedPageElements
from core import WebPage, WebElement, ManyWebElements


class BrandDetailedPage(WebPage):
    path = '/brands/blum-cosmetics/'
    page_title = WebElement(xpath=BrandDetailedPageElements.page_title)
    parent_breadcrumbs = WebElement(xpath=BrandDetailedPageElements.parent_breadcrumbs)
