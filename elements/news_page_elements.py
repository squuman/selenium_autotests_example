from dataclasses import dataclass


@dataclass
class NewsPageElements:
    tag_0 = '//li[@id="tag-0"]'
    tag_1 = '//li[@id="tag-1"]'
    tag_2 = '//li[@id="tag-2"]'
    tag_3 = '//li[@id="tag-3"]'
    tag_4 = '//li[@id="tag-4"]'
    tag_5 = '//li[@id="tag-5"]'
    tag_6 = '//li[@id="tag-6"]'

    active_tag = '//li[@class="tags__item swiper-slide jsTagItem size-smaller size-md-tiny active"]'
    disable_tag = '//li[@class="tags__item swiper-slide jsTagItem size-smaller size-md-tiny"]'

    pagination_show_more_button = '//a[id="paginationShowMore"]'
