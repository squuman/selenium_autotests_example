from dataclasses import dataclass


@dataclass
class NewsDetailedPageElements:
    go_to_catalog_button = '//a[@id="newsHeaderContentLink"]'
    arrow_left_button = '//div[@id="productSliderNavPrev"]'
    arrow_right_button = '//div[@id="productSliderNavNext"]'
    back_to_blog_button = '//div[@id="newsDetailLinkBack"]'

    current_slider = '//li[@id="productSliderItem-0"]'
    active_slider = '//li[@class="products-slider__item swiper-slide color-text letter-spacing-normal' \
                    ' swiper-slide-active"]'
    next_slide = '//li[@class="products-slider__item swiper-slide color-text letter-spacing-normal swiper-slide-next"]'
    prev_slide = '//li[@class="products-slider__item swiper-slide color-text letter-spacing-normal' \
                 ' swiper-slide-duplicate swiper-slide-prev"]'
