import time
import pytest
import allure
from pages import MainPage


@allure.suite("Проверка открытия главной страницы")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_open_main_page(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Сравниваем заголовки страницы"):
        assert MainPage.title == web_browser.title


@allure.suite("Проверка, что кнопка открытия меню нажимается")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_is_clickable_menu_button(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Ищем кнопку меню"):
        assert page.menu_show_button.is_visible()
    with allure.step("Проверяем, что кнопка нажимается"):
        assert page.menu_show_button.is_clickable()


@allure.suite("Проверка, что меню открывается при клике на кнопку его открытия")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_open_menu(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Ищем кнопку меню"):
        assert page.menu_show_button.is_visible()
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ждем, пока откроется блок меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Проверяем, что меню открылось"):
        assert page.menu_block.is_visible()


@allure.suite("Проверка открытия каталога, если хедер статичный")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_open_menu_if_scroll(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся вниз страницы"):
        page.mailing_form.scroll_to_element()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Проверяем, что меню открылось"):
        assert page.menu_block.is_visible()


@allure.suite("Проверка, что меню закрывается при повторном клике")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_close_menu_after_repeat_click(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Ищем кнопку меню"):
        assert page.menu_show_button.is_visible()
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ждем, пока откроется блок меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Проверяем, что меню открылось"):
        assert page.menu_block.is_visible()
    with allure.step("Нажимаем на кнопку меню"):
        page.menu_close_button.click()
    with allure.step("Ждем пока меню закроется"):
        time.sleep(1)
    with allure.step("Проверяем, что блок меню закрылся"):
        assert not page.menu_block.is_visible()


@pytest.mark.xfail
@allure.suite("Проверка, что при наведении на \"Каталог\" появляется блок с категориями товаров")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_hover_to_catalog_show_categories_block(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Ищем кнопку меню"):
        assert page.menu_show_button.is_visible()
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ждем, пока откроется блок меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Нажимаем на \"Каталог\""):
        page.menu_catalog_pos.move_to_element()
    with allure.step("Ждем появления списка категорий"):
        page.menu_catalog_categories_block.wait_until_not_visible()
    with allure.step("Проверяем, что блок со списком категорий появился"):
        time.sleep(3)
        assert page.menu_catalog_categories_block.is_visible()


@pytest.mark.parametrize("name, email, phone, sms_mailing, email_mailing, privacy, excepted_result", [
    ("Имя", "example@test.", "+7999999", True, True, True, True),
    ("123123", "example@test", "+7999999", False, True, False, True),
    ("123123", "123123123", "123123", False, True, True, True),
    ("!#$%^&*()_+-={},./<>?", "example@", "+7999999", True, True, False, True),
    ("!#$%^&*()_+-={},./<>?", "@", "+79999999999", True, True, True, True),
    ("!#$%^&*()_+-={},./<>?", "@.", "123123", False, False, False, True),
    ("!#$%^&*()_+-={},./<>?", "example@test.ru", "test", True, True, True, True),
    ("!#$%^&*()_+-={},./<>?", "example", "!#$%^&*()_+-=", False, False, True, True),
    ("Name", "example@test", "123123", True, False, True, True),
    ("Name", "example@test.", "test", False, True, False, True),
    ("Name", "123123123", "!#$%^&*()_+-=", True, False, True, True),
    ("Name", "!#$%^&*()_+", "+79999999999", False, True, True, True),
    ("Name", "@", "123123", True, False, False, True),
    ("Name", "@.", "test", False, True, True, True),
    ("Name", "example@test.ru", "!#$%^&*()_+-=", True, True, False, True),
    ("Name", "example", "+7999999", False, False, True, True),
    ("Name", "example@", "+79999999999", True, True, False, True),
    ("Имя", "example@test.", "!#$%^&*()_+-=", False, False, True, True),
    ("Имя", "123123123", "+79999999999", True, True, False, True),
    ("Имя", "!#$%^&*()_+", "123123", False, True, True, True),
    ("Имя", "@", "test", True, False, False, True),
    ("Имя", "@.", "!#$%^&*()_+-=", False, True, True, True),
    ("Имя", "example@test.ru", "+7999999", True, False, False, True),
    ("Имя", "example", "+79999999999", True, True, True, True),
    ("Имя", "example@", "123123", False, False, True, True),
    ("Имя", "example@test", "test", True, True, False, True),
    ("123123", "!#$%^&*()_+", "test", False, False, True, True),
    ("123123", "@", "!#$%^&*()_+-=", True, True, True, True),
    ("123123", "@.", "+7999999", True, False, False, True),
    ("123123", "example", "123123", True, False, False, True),
    ("123123", "example@", "test", False, True, True, True),
    ("123123", "example@test", "!#$%^&*()_+-=", True, True, False, True),
    ("123123", "example@test.", "+79999999999", False, False, True, True),
    ("!#$%^&*()_+-={},./<>?", "!#$%^&*()_+", "!#$%^&*()_+-=", True, True, False, True),
    ("!#$%^&*()_+-={},./<>?", "@", "+7999999", False, False, True, True),
    ("!#$%^&*()_+-={},./<>?", "@.", "+79999999999", True, True, False, True),
    ("!#$%^&*()_+-={},./<>?", "example@test.ru", "123123", False, True, True, True),
    ("!#$%^&*()_+-={},./<>?", "example", "test", True, False, False, True),
    ("!#$%^&*()_+-={},./<>?", "example@", "!#$%^&*()_+-=", False, True, True, True),
    ("!#$%^&*()_+-={},./<>?", "example@test", "+79999999999", True, False, True, True),
    ("!#$%^&*()_+-={},./<>?", "example@test.", "123123", False, True, False, True),
    ("!#$%^&*()_+-={},./<>?", "123123123", "test", True, False, True, True),
    ("Name", "@", "+79999999999", False, False, True, True),
    ("Name", "@.", "123123", True, True, True, True),
    ("Name", "example@test.ru", "test", False, False, False, True),
    ("Name", "example", "!#$%^&*()_+-=", True, True, True, True),
    ("Name", "example@", "+79999999999", False, False, False, True),
    ("Name", "example@test", "123123", True, True, True, True),
    ("Name", "example@test.", "test", True, False, False, True),
    ("Name", "123123123", "!#$%^&*()_+-=", False, True, True, True),
    ("Name", "!#$%^&*()_+", "+7999999", True, True, False, True),
    ("Имя", "@.", "test", True, False, True, True),
    ("Имя", "example@test.ru", "!#$%^&*()_+-=", False, True, False, True),
    ("Имя", "example", "+79999999999", True, False, True, True),
    ("Имя", "example@", "123123", True, True, False, True),
    ("Имя", "example@test", "test", False, True, True, True),
    ("Имя", "example@test.", "!#$%^&*()_+-=", True, False, True, True),
    ("Имя", "123123123", "+7999999", False, True, False, True),
    ("Имя", "!#$%^&*()_+", "+79999999999", True, False, True, True),
    ("Имя", "@", "123123", False, True, False, True),
    ("123123", "example@test.ru", "+79999999999", False, True, True, False),
])
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка отправки формы подписки на рассылку")
def test_output_errors_mailing_form(web_browser, url, name, email, phone, sms_mailing, email_mailing, privacy,
                                    excepted_result):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Переходим к форме подписки на рассылку"):
        page.mailing_form.scroll_to_element()
    with allure.step("Заполнеяем поле Имя"):
        page.mailing_form_name_input.send_keys(name)
    with allure.step("Заполнеяем поле Почта"):
        page.mailing_form_email_input.send_keys(email)
    with allure.step("Заполнеяем поле Телефон"):
        page.mailing_form_phone_input.send_keys(phone)
    with allure.step("Заполнеяем поле \"Хчоу получать рассылку по sms\""):
        if sms_mailing:
            page.mailing_form_sms_mailing_checkbox.click()
    with allure.step("Заполнеяем поле Имя \"Хочу получать рассылку по e-mail\""):
        if email_mailing:
            page.mailing_form_email_mailing_checkbox.click()
    with allure.step("Заполнеяем поле \"Даю согласие на обработку персональных данных"
                     " в соответствии с Политикой конфиденциальности\""):
        if privacy:
            page.mailing_form_privacy_checkbox.click()
    with allure.step("Нажммаем на кнопку отправки"):
        page.mailing_form_send_button.click()
    with allure.step("Проверяем наличие ошибок"):
        mailing_form_error_name = page.mailing_form_error_name.is_find()
        mailing_form_error_email = page.mailing_form_error_email.is_find()
        mailing_form_error_phone = page.mailing_form_error_phone.is_find()
        mailing_form_error_sms_mailing = page.mailing_form_error_sms_mailing.is_find()
        mailing_form_error_email_mailing = page.mailing_form_error_email_mailing.is_find()
        mailing_form_error_privacy = page.mailing_form_error_privacy.is_find()

        # проверяем наличие ошибок
        real_result = mailing_form_error_name or mailing_form_error_email or mailing_form_error_phone or \
                      mailing_form_error_sms_mailing or mailing_form_error_email_mailing or mailing_form_error_privacy

        assert excepted_result == real_result


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Смотреть все\" в разделе \"Лучшие предложения\"")
def test_show_more_button_is_clickable_in_best_features(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к блоку \"Лучшие предложения\""):
        page.best_offers_block.scroll_to_element()
    with allure.step("Проверяем, что кнопка \"Смотреть больше\" кликабельная"):
        assert page.all_best_offers_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Зарегистрироваться\" в разделе \"Зарегистрируйтесь на портале\"")
def test_register_button_is_clickable_in_register_section(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к блоку \"Лучшие предложения\""):
        page.register_info_block.scroll_to_element()
    with allure.step("Проверяем, что кнопка \"Смотреть больше\" кликабельная"):
        assert page.register_info_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Смотреть все\" в разделе \"Популярные категории\"")
def test_show_all_button_is_clickable_in_popular_categories_section(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к блоку \"Лучшие предложения\""):
        page.popular_categories_section.scroll_to_element()
    with allure.step("Проверяем, что кнопка \"Смотреть больше\" кликабельная"):
        assert page.all_categories_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Хит\" в разделе \"Лучшие предложения\"")
def test_show_hits_button_is_clickable_in_best_offers_section(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к блоку \"Лучшие предложения\""):
        page.best_offers_block.scroll_to_element()
    with allure.step("Проверяем, что кнопка \"Хит\" кликабельная"):
        assert page.show_hits_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Новинка\" в разделе \"Лучшие предложения\"")
def test_show_new_button_is_clickable_in_best_offers_section(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к блоку \"Лучшие предложения\""):
        page.best_offers_block.scroll_to_element()
    with allure.step("Проверяем, что кнопка \"Новинка\" кликабельная"):
        assert page.show_new_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Скидка\" в разделе \"Лучшие предложения\"")
def test_show_sale_button_is_clickable_in_best_offers_section(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к блоку \"Лучшие предложения\""):
        page.best_offers_block.scroll_to_element()
    with allure.step("Проверяем, что кнопка \"Скидка\" кликабельная"):
        assert page.show_sale_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Влево\" на главном слайдере")
def test_button_left_is_clickable_in_main_slider(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Проверяем, что кнопка \"Влево\" кликабельна"):
        assert page.left_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Вправо\" на главном слайдере")
def test_button_right_is_clickable_in_main_slider(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Проверяем, что кнопка \"Вправо\" кликабельна"):
        assert page.right_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка, что кнопка показа поля поиска кликабельная")
def test_search_button_is_clickable(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Проверяем, что кнопка \"Поиск\" кликабельна"):
        assert page.search_show_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка, что появляется строка поиска при клике на кнопку \"Лупа\"")
def test_show_search_filed_if_click_on_button(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на кнопку \"Поиск\""):
        page.search_show_button.click()
    with allure.step("Проверяем, что появилась строка поиска"):
        page.search_field.wait_until_not_visible()
        assert page.search_field.is_visible()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки старта поиска")
def test_start_search_button_is_clickable(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на кнопку \"Поиск\""):
        page.search_show_button.click()
    with allure.step("Проверям, что кнопка старта поиска кликабельная"):
        assert page.start_search_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка вывода блока \"О компании\" при наведении на пункт меню \"О компании\"")
def test_show_about_company_block_if_move_to_menu_pos_about(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
        page.menu_block.wait_until_not_visible()
    with allure.step("Нажимаем/наводим на \"О компании\""):
        page.menu_about_company_pos.click()
    with allure.step("Проверяем, что появился блок с информацией о компании"):
        assert page.menu_about_company_block.is_visible()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite(
    "Проверка вывода блока \"О компании\" при наведении на пункт меню \"О компании\" после пролистывания страницы")
def test_show_about_company_block_if_move_to_menu_pos_about_after_scroll(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Пролистываем страницу вниз"):
        page.mailing_form.scroll_to_element()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ожидаем загрузки меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Нажимаем/наводим на \"О компании\""):
        page.menu_about_company_pos.click()
    with allure.step("Проверяем, что появился блок с информацией о компании"):
        assert page.menu_about_company_block.is_visible()


@pytest.mark.skip
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Акции\" в меню")
def test_sales_button_is_clickable_in_menu(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Пролистываем страницу вниз"):
        page.mailing_form.scroll_to_element()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ожидаем загрузки меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Проверяем кликабельность кнопки \"Акции\""):
        assert page.menu_sales_pos.is_clickable()


@pytest.mark.skip
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Акции\" в меню после пролистывания страницы")
def test_sales_button_is_clickable_in_menu_after_scroll(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Пролистываем страницу вниз"):
        page.mailing_form.scroll_to_element()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ожидаем загрузки меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Проверяем кликабельность кнопки \"Акции\""):
        assert page.menu_sales_pos.is_clickable()


@pytest.mark.skip
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Сотрудничество\" в меню")
def test_cooperation_button_is_clickable_in_menu(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ожидаем загрузки меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Проверяем кликабельность кнопки \"Сотрудничество\""):
        assert page.menu_cooperation_pos.is_clickable()


@pytest.mark.skip
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Сотрудничество\" в меню после пролистывания")
def test_cooperation_button_is_clickable_in_menu_after_scroll(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Пролистываем страницу вниз"):
        page.mailing_form.scroll_to_element()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ожидаем загрузки меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Проверяем кликабельность кнопки \"Сотрудничество\""):
        assert page.menu_cooperation_pos.is_clickable()


@pytest.mark.skip
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Контакты\" в меню")
def test_contacts_button_is_clickable_in_menu(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ожидаем загрузки меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Проверяем кликабельность кнопки \"Контакты\""):
        assert page.menu_contacts_pos.is_clickable()


@pytest.mark.skip
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки \"Контакты\" в меню после пролистывания")
def test_contacts_button_is_clickable_in_menu_after_scroll(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Пролистываем страницу вниз"):
        page.mailing_form.scroll_to_element()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ожидаем загрузки меню"):
        page.menu_block.wait_until_not_visible()
    with allure.step("Проверяем кликабельность кнопки \"Контакты\""):
        assert page.menu_contacts_pos.is_clickable()
