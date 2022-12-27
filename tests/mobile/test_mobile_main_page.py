import time
import pytest
import allure
from pages import MainPage

url = 'http://usbc-dev.onpeak.su/'


@allure.suite("Проверка открытия главной страницы")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_open_main_page(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Сравниваем заголовки страницы"):
        assert MainPage.title == web_browser.title


@allure.suite("Проверка, что кнопка открытия меню нажимается")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_is_clickable_menu_button(web_browser):
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
def test_open_menu(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Ищем кнопку меню"):
        assert page.menu_show_button.is_visible()
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ждем, пока откроется блок меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Проверяем, что меню открылось"):
        assert page.mobile_sidebar_menu.is_visible()


@allure.suite("Проверка открытия каталога, если хедер статичный")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_open_menu_after_scroll(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся вниз страницы"):
        page.mailing_form.scroll_to_element()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ждем, пока откроется блок меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Проверяем, что меню открылось"):
        assert page.mobile_sidebar_menu.is_visible()


@allure.suite("Проверка закрытия меню после скроллинга")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_close_menu_after_scrolling(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Спускаемся вниз страницы"):
        page.mailing_form.scroll_to_element()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ждем, пока откроется блок меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Нажимаем на крестик"):
        page.menu_close_button.click()
    with allure.step("Проверяем, что меню закрылось"):
        time.sleep(0.3)
        assert False == page.mobile_sidebar_menu.is_visible()


@allure.suite("Проверка закрытия меня")
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
def test_close_menu(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на \"Меню\""):
        page.menu_show_button.click()
    with allure.step("Ждем, пока откроется блок меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Нажимаем на крестик"):
        page.menu_close_button.click()
    with allure.step("Проверяем, что меню закрылось"):
        time.sleep(0.3)
        assert False == page.mobile_sidebar_menu.is_visible()


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
def test_output_errors_mailing_form(web_browser, name, email, phone, sms_mailing, email_mailing, privacy,
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
@allure.suite("Проверка кликабельности кнопки для открытия списка городов")
def test_clickable_button_for_open_city_list(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ожидаем появления блока меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Проверяем кликабельность кнопки"):
        assert page.mobile_city_open_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка открытия списка городов")
def test_open_city_list(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ожидаем появления блока меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Нажимаем на кнопку геолокации"):
        page.mobile_city_open_button.click()
    with allure.step("Ожидаем появления блока с городами"):
        page.mobile_menu_block_content.wait_until_not_visible()
    with allure.step("Проверяем: открылся ли блок с городами"):
        assert page.mobile_menu_block_content.is_visible()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки для открытия каталога")
def test_clickable_button_for_open_catalog(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ожидаем появления блока меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Нажимаем на кнопку каталога"):
        assert page.mobile_catalog_open_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка открытия каталога")
def test_open_catalog(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ожидаем появления блока меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Нажимаем на кнопку каталога"):
        page.mobile_catalog_open_button.click()
    with allure.step("Ожидаем открытия блока каталога"):
        page.mobile_menu_catalog_block.wait_until_not_visible()
    with allure.step("Проверяем, что блок категорий открылся"):
        assert page.mobile_menu_catalog_block.is_visible()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка кликабельности кнопки для вызова формы авторизации")
def test_clickable_login_form(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ожидаем появления блока меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Проверяем кликабельность кнопки вызова формы"):
        assert page.mobile_login_form_open_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/100862/",
              "Разработка автотестов для главной страницы")
@allure.suite("Проверка вызова формы авторизации")
def test_open_login_form(web_browser):
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, url)
    with allure.step("Нажимаем на кнопку открытия меню"):
        page.menu_show_button.click()
    with allure.step("Ожидаем появления блока меню"):
        page.mobile_sidebar_menu.wait_until_not_visible()
    with allure.step("Нажимаем на кнопку для вызова формы авторизации"):
        page.mobile_login_form_open_button.click()
    with allure.step("Ожидаем появляения формы авторизации"):
        page.mobile_login_form.wait_until_not_visible()
    with allure.step("Проверяем наличие формы авторизации"):
        assert page.mobile_login_form.is_visible()
