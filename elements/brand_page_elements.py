from dataclasses import dataclass


@dataclass
class BrandPageElements:
    breadcrumbs_parent = '//a[@id="breadcrumbs-link-0"]'
    big_letter = '//div[@class="brands__big-item font-literata size-md-bigger-four size-biggest color-dark-bege bg-color-bege"]'
    alphabet_letter_B = '//div[@data-letter="B"]'
    alphabet_letter_M = '//div[@data-letter="M"]'
    alphabet_letter_N = '//div[@data-letter="N"]'
    alphabet_letter_symbol = '//div[@data-letter="#"]'

    brands_list_block = '//div[@class="brands__container__item"]'

    blum_cosmetics_url = '//a[@href="/brands/blum-cosmetics/"]'