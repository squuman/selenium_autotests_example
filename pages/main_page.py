from core import WebPage, WebElement, ManyWebElements
from elements import MainPageElements, HeaderElements


class MainPage(WebPage):
    title = 'Главная страница'
    path = ''

    # header

    logo = WebElement(xpath=HeaderElements.logo)
    menu_show_button = WebElement(xpath=HeaderElements.menu_show_button_enable)
    menu_close_button = WebElement(xpath=HeaderElements.menu_show_button_disable)
    geo_show_button = WebElement(xpath=HeaderElements.geo_show_button)
    personal_go_button = WebElement(xpath=HeaderElements.personal_go_button)
    favorite_go_button = WebElement(xpath=HeaderElements.favorite_go_button)
    cart_show_button = WebElement(xpath=HeaderElements.cart_show_button)

    menu_block = WebElement(xpath=HeaderElements.menu_block)
    menu_positions = ManyWebElements(xpath=HeaderElements.menu_pos)
    menu_catalog_pos = WebElement(xpath=HeaderElements.menu_catalog_pos)
    menu_catalog_categories_block = WebElement(xpath=HeaderElements.menu_catalog_categories_block)
    menu_about_company_pos = WebElement(xpath=HeaderElements.menu_about_company_pos)
    menu_about_company_block = WebElement(xpath=HeaderElements.menu_about_company_block)
    menu_sales_pos = WebElement(xpath=HeaderElements.menu_sales_pos)
    menu_cooperation_pos = WebElement(xpath=HeaderElements.menu_cooperation_pos)
    menu_contacts_pos = WebElement(xpath=HeaderElements.menu_contacts_pos)

    # main page content

    all_features_button = WebElement(xpath=MainPageElements.all_features_button)
    all_about_company_button = WebElement(xpath=MainPageElements.all_about_company_button)

    # mailing_form
    mailing_form = WebElement(xpath=MainPageElements.mailing_form)
    mailing_form_name_input = WebElement(xpath=MainPageElements.mailing_form_name_input)
    mailing_form_email_input = WebElement(xpath=MainPageElements.mailing_form_email_input)
    mailing_form_phone_input = WebElement(xpath=MainPageElements.mailing_form_phone_input)
    mailing_form_sms_mailing_checkbox = WebElement(xpath=MainPageElements.mailing_form_sms_mailing_checkbox)
    mailing_form_email_mailing_checkbox = WebElement(xpath=MainPageElements.mailing_form_email_mailing_checkbox)
    mailing_form_privacy_checkbox = WebElement(xpath=MainPageElements.mailing_form_privacy_checkbox)
    mailing_form_send_button = WebElement(xpath=MainPageElements.mailing_form_send_button)

    mailing_form_error_name = WebElement(xpath=MainPageElements.mailing_form_error_name)
    mailing_form_error_email = WebElement(xpath=MainPageElements.mailing_form_error_email)
    mailing_form_error_phone = WebElement(xpath=MainPageElements.mailing_form_error_phone)
    mailing_form_error_sms_mailing = WebElement(xpath=MainPageElements.mailing_form_error_sms_mailing)
    mailing_form_error_email_mailing = WebElement(xpath=MainPageElements.mailing_form_error_email_mailing)
    mailing_form_error_privacy = WebElement(xpath=MainPageElements.mailing_form_error_privacy)

    # best offers
    best_offers_block = WebElement(xpath=MainPageElements.best_offers_block)
    all_best_offers_button = WebElement(xpath=MainPageElements.all_best_offers_button)
    show_hits_button = WebElement(xpath=MainPageElements.show_hits_button)
    show_new_button = WebElement(xpath=MainPageElements.show_news_button)
    show_sale_button = WebElement(xpath=MainPageElements.show_sales_button)

    # reg info
    register_info_block = WebElement(xpath=MainPageElements.register_info_block)
    register_info_button = WebElement(xpath=MainPageElements.register_info_button)

    # popular categories
    popular_categories_section = WebElement(xpath=MainPageElements.popular_categories_section)
    all_categories_button = WebElement(xpath=MainPageElements.all_categories_button)

    # main slider
    left_button = WebElement(xpath=MainPageElements.left_button)
    right_button = WebElement(xpath=MainPageElements.right_button)

    # search
    search_show_button = WebElement(xpath=HeaderElements.search_show_button)
    search_field = WebElement(xpath=HeaderElements.search_field)
    start_search_button = WebElement(xpath=HeaderElements.start_search_button)

    # mobile
    mobile_sidebar_menu = WebElement(xpath=MainPageElements.mobile_sidebar_menu)
    mobile_city_open_button = WebElement(xpath=MainPageElements.mobile_city_open_button)
    mobile_menu_block_content = WebElement(xpath=MainPageElements.mobile_menu_cities_block)
    mobile_catalog_open_button = WebElement(xpath=MainPageElements.mobile_catalog_open_button)
    mobile_menu_catalog_block = WebElement(xpath=MainPageElements.mobile_menu_catalog_block)
    mobile_login_form_open_button = WebElement(xpath=MainPageElements.mobile_login_form_open_button)
    mobile_login_form = WebElement(xpath=MainPageElements.mobile_login_form)