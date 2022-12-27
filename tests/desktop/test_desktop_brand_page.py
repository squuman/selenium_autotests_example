import time
import pytest
import allure
from pages import BrandPage, MainPage, BrandDetailedPage


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/102615/")
@allure.suite("Проверка открытия разводящей страницы брендов")
def test_open_brands_page(web_browser, url):
    with allure.step("Открытие странице брендов"):
        page = BrandPage(web_browser, url + BrandPage.path)
    with allure.step("Ждем открытия страницы"):
        page.wait_page_loaded()
    with allure.step("Сравниваем заголовки"):
        assert BrandPage.title == web_browser.title


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/102615/")
@allure.suite("Проверка перехода на главную страницу при клике на хлебные крошки")
def test_open_main_page_by_click_on_breadcrumbs(web_browser, url):
    with allure.step("Открытие странице брендов"):
        page = BrandPage(web_browser, url + BrandPage.path)
    with allure.step("Ждем открытия страницы"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на родительский элемент в крошках"):
        page.breadcrumbs_parent.click()
    with allure.step("Ожидаем загрузки"):
        page.wait_page_loaded()
    with allure.step("Сравниваем заголовки"):
        assert MainPage.title == web_browser.title


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/102615/")
@allure.suite("Проверка вывода всего списка брендов при клике на «Все»")
def test_output_brand_list_by_click_all(web_browser, url):
    with allure.step("Открытие странице брендов"):
        page = BrandPage(web_browser, url + BrandPage.path)
    with allure.step("Ждем открытия страницы"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на  \"Все\""):
        pass
    with allure.step("Проверяем кол-во блоков брендов"):
        assert page.brands_list_block.count() > 1


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/102615/")
@allure.suite("Вывод брендов одной буквенной категории")
def test_output_brands_one_letter(web_browser, url):
    with allure.step("Открытие странице брендов"):
        page = BrandPage(web_browser, url + BrandPage.path)
    with allure.step("Ждем открытия страницы"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на  \"B\""):
        page.alphabet_letter_B.click()
    with allure.step("Проверяем букву выведенного блока"):
        assert 'B' == page.big_letter.get_text()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/102615/")
@allure.suite("Переход на страницу бренда путем клика на его заголовок")
def test_open_brand_page_by_click_on_brand_title(web_browser, url):
    with allure.step("Открытие странице брендов"):
        page = BrandPage(web_browser, url + BrandPage.path)
    with allure.step("Ждем открытия страницы"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на название бренда"):
        page.blum_cosmetics_url.click()
        excepted_result = page.blum_cosmetics_url.get_text()
    with allure.step("Ждем открытия страницы"):
        page.wait_page_loaded()
    with allure.step("Сравниваем название в разводящей и детальной"):
        assert excepted_result == web_browser.title
