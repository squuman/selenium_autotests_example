import allure
import pytest
from pages import BrandDetailedPage, MainPage

@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/102615/")
@allure.suite("Переход на главную страницу путем клика на родительский элемент в хлебных крошках")
def test_open_main_page_by_click_parent_in_breadcrumbs(web_browser, url):
    with allure.step("Открываем главную страницу"):
        page = BrandDetailedPage(web_browser, url + BrandDetailedPage.path)
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Нажимаем на родительский элемент в хлебных крошках"):
        page.parent_breadcrumbs.click()
    with allure.step("Ожидаем загрузки"):
        assert MainPage.title == web_browser.title