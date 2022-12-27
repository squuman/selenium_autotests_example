from elements import BrandPageElements
from core import WebPage, WebElement, ManyWebElements


class BrandPage(WebPage):
    path = '/brands/'
    title = 'Бренды'

    breadcrumbs_parent = WebElement(xpath=BrandPageElements.breadcrumbs_parent)
    big_letter = WebElement(xpath=BrandPageElements.big_letter)
    alphabet_letter_B = WebElement(xpath=BrandPageElements.alphabet_letter_B)
    alphabet_letter_M = WebElement(xpath=BrandPageElements.alphabet_letter_M)
    alphabet_letter_N = WebElement(xpath=BrandPageElements.alphabet_letter_N)
    alphabet_letter_symbol = WebElement(xpath=BrandPageElements.alphabet_letter_symbol)

    brands_list_block = ManyWebElements(xpath=BrandPageElements.brands_list_block)

    blum_cosmetics_url = WebElement(xpath=BrandPageElements.blum_cosmetics_url)
