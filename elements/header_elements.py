from dataclasses import dataclass


@dataclass
class HeaderElements:
    logo = '//a[@class="header__logo"]'
    menu_show_button_enable = '//a[@class="header__icon burger hover-dark-bege jsBurgerMenu"]'
    menu_show_button_disable = '//a[@class="header__icon burger hover-dark-bege jsBurgerMenu disabled"]'
    geo_show_button = '//a[@class="header__icon map hover-dark-bege d-md-none"]'
    personal_go_button = '//a[@class="header__icon person  color-bege hover-dark-bege d-md-none"]'
    favorite_go_button = '//a[@class="header__icon favorites color-bege hover-dark-bege"]'
    cart_show_button = '//a[@class="header__icon basket color-bege hover-dark-bege jsSmallBasketTop"]'

    # menu
    menu_block = '//div[@class="header-menu__opacity-row"]'
    menu_pos = '//a[@class="header-menu__link hover-dark-bege size-small letter-spacing-normal"]'
    menu_catalog_pos = '//li[@id="headerMenuItem-0"]'
    menu_catalog_categories_block = '//ul[@id="headerMenuSubmenuList-0"]'
    menu_about_company_pos = '//li[@id="headerMenuLink-6"]'
    menu_about_company_block = '//ul[@id="headerMenuSubmenuList-1"]'
    menu_sales_pos = '//li[@id="headerMenuItem-2"]'
    menu_cooperation_pos = '//li[@id="headerMenuItem-3"]'
    menu_contacts_pos = '//li[@id="headerMenuItem-4"]'

    # search
    search_show_button = '//a[@class="header__icon search color-bege hover-dark-bege d-md-none jsSearchIcon"]'
    search_field = '//input[@id="headerSearchbarDesctop"]'
    start_search_button = '//button[@class="searchbar-desktop__submit"]'