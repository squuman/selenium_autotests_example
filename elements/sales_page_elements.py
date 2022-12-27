from dataclasses import dataclass


@dataclass
class SalesPageElements:
    # slider
    left_arrow_button = '//div[@id="salesSliderButtonsPrev"]'
    right_arrow_button = '//div[@id="salesSliderButtonsNext"]'
    active_slide = '//div[@id="swiper-slide sales-slide swiper-slide-active"]'
    current_slide_number = '//span[@class="swiper-pagination-current"]'
    total_slide_number = '//span[@class="swiper-pagination-total"]'

    # pagination
    show_more_button = '//a[@id="paginationShowMore"]'
    next_page_button = '//li[@id="paginationButNext"]'
    second_page_button = '//li]@id="pagination-2"]'