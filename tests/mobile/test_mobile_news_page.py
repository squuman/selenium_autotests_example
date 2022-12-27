import time
import pytest
import allure
from pages import NewsPage


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка открытия страницы новостей")
def test_open_news_page(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsPage(web_browser, url + NewsPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась нужная страница"):
        assert NewsPage.title == web_browser.title


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка, что при клике на тег он меняет свой цвет при клике")
def test_tag_change_color(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsPage(web_browser, url + NewsPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на тег"):
        page.tag_1.click()
    with allure.step("Проверяем, что тег сменил стиль"):
        assert page.active_tag.is_visible()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка, что при клике на тег он меняет свой цвет при повторном клике")
def test_tag_change_color_after_repeat_click(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsPage(web_browser, url + NewsPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на тег"):
        page.tag_1.click()
    with allure.step("Повторно нажимаем на тег"):
        page.tag_1.click()
    with allure.step("Проверяем, что кнопка находится в исходном состоянии"):
        assert page.disable_tag.is_visible()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка, что при клике на тег он меняет свой цвет при повторном клике")
def test_clickable_pagination_show_more(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsPage(web_browser, url + NewsPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к кнопке"):
        page.pagination_show_more_button.scroll_to_element()
    with allure.step("Проверяем кликабельность кнопки"):
        assert page.pagination_show_more_button.is_clickable()
