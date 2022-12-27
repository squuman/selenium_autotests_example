from dataclasses import dataclass


@dataclass
class MainPageElements:
    all_features_button = '//a[@class="btn-white font-museo weight-300 transform-uppercase size-md-tiny' \
                          ' size-small features-benefits__element-link"]'
    all_about_company_button = '//a[@class="company-info__more a-light d-block font-museo size-md-tiny size-small ' \
                               'weight-700 transform-uppercase"]'

    # mailing_form
    mailing_form = '//form[@id="mailingForm"]'
    mailing_form_name_input = '//input[@id="mailingFormName"]'
    mailing_form_email_input = '//input[@id="mailingFormEmail"]'
    mailing_form_phone_input = '//input[@id="mailingFormPhone"]'
    mailing_form_sms_mailing_checkbox = '//label[@class="mailing-form__label ' \
                                        'mailing-form__consent mailing-form__consent-sms jsMailingConsent"]'
    mailing_form_email_mailing_checkbox = '//label[@class="mailing-form__label mailing-form__consent ' \
                                          'mailing-form__consent-email jsMailingConsent"]'
    mailing_form_privacy_checkbox = '//label[@class="mailing-form__label' \
                                    ' mailing-form__consent mailing-form__consent-agreement jsMailingConsent"]'
    mailing_form_send_button = '//button[@class="mailing-form__submit btn-default-white"]'

    mailing_form_error_name = '//label[@id="mailingFormName-error"]'
    mailing_form_error_email = '//label[@id="mailingFormEmail-error"]'
    mailing_form_error_phone = '//label[@id="mailingFormPhone-error"]'
    mailing_form_error_sms_mailing = '//input[@class="jsMailingFormPhoneAgreement' \
                                     ' mailing-form__consent__checkbox error_input"]'
    mailing_form_error_email_mailing = '//input[@class="jsMailingFormEmailAgreement' \
                                       ' mailing-form__consent__checkbox error_input"]'
    mailing_form_error_privacy = '//input[@class="jsMailingFormAgreement mailing-form__consent__checkbox error_input"]'

    # best offers
    best_offers_block = '//section[@class="best-offers"]'
    all_best_offers_button = '//a[@class="best-offers__content__link btn-bege font-museo size-small weight-300' \
                             'transform-uppercase"]'
    show_hits_button = '//label[@for="hit-radio"]'
    show_news_button = '//label[@for="new-radio"]'
    show_sales_button = '//label[@for="sale-radio"]'

    # reg info
    register_info_block = '//div[@class="container reg-info__container"]'
    register_info_button = '//a[@class="btn-light font-museo size-small weight-300 transform-uppercase reg-info__link"]'

    # popular categories
    all_categories_button = '//a[@class="btn-white font-museo size-small weight-300' \
                            ' transform-uppercase popular-categories__link-more"]'
    popular_categories_section = '//section[@class="popular-categories"]'

    # main slider
    right_button = '//div[@class="swiper-button-next slider-buttons__next d-md-none"]'
    left_button = '//div[@class="swiper-button-prev slider-buttons__prev d-md-none"]'

    # mobile menu
    mobile_sidebar_menu = '//nav[@class="header-menu__container header-menu__container-mobile container color-white ' \
                          'jsHeaderMobileMenu"]'
    mobile_city_open_button = '//button[@id="headerMobileMenuLevelBut-0"]'
    mobile_menu_cities_block = '//div[@id="headerMobileSubmenuContainer-0"]'
    mobile_catalog_open_button = '//button[@id="headerMobileMenuLevelBut-1"]'
    mobile_menu_catalog_block = '//div[@id="headerMobileSubmenuContainer-1"]'
    mobile_login_form_open_button = '//button[@id="headerMobileMenuLevelBut-2"]'
    mobile_login_form = '//form[@id="auth-mobile-form"]'
