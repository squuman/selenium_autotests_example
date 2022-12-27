from dataclasses import dataclass

@dataclass
class BrandDetailedPageElements:
    page_title = '//h1[@id="brandHeaderTitle"]'
    parent_breadcrumbs = '//a[@id="breadcrumbs-link-0"]'
