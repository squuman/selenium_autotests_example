import time
import pytest
import allure
from pages import NewsDetailedPage


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка открытия страницы новостей")
def test_open_news_page(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsDetailedPage(web_browser, url + NewsDetailedPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась нужная страница"):
        assert NewsDetailedPage.title == web_browser.title


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка, что кнопка \"Стрелочка вправо\" нажимается")
def test_clickable_right_arrow(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsDetailedPage(web_browser, url + NewsDetailedPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к слайдеру"):
        page.arrow_right_button.scroll_to_element()
    with allure.step("Проверяем, что кнопка нажимается"):
        assert page.arrow_right_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка, что кнопка \"Стрелочка влево\" нажимается")
def test_clickable_left_arrow(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsDetailedPage(web_browser, url + NewsDetailedPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к слайдеру"):
        page.arrow_left_button.scroll_to_element()
    with allure.step("Проверяем, что кнопка нажимается"):
        assert page.arrow_left_button.is_clickable()


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка, что слайды листаются при клике на кнопку \"Стрелочка вправо\"")
def test_clickable_scrolling_sliders_if_click_on_right_arrow(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsDetailedPage(web_browser, url + NewsDetailedPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к слайдеру"):
        page.arrow_right_button.scroll_to_element()
    with allure.step("Нажимаем на стрелочку"):
        current_slide_index = int(page.active_slider.get_attribute('data-swiper-slide-index'))
        page.arrow_right_button.click()
    with allure.step("Проверяем, что следующий слайд стал активным"):
        next_slide_index = int(page.active_slider.get_attribute('data-swiper-slide-index'))
        assert current_slide_index + 1 == next_slide_index


@pytest.mark.skip
@pytest.mark.xfail
@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка, что слайды листаются при клике на кнопку \"Стрелочка влево\"")
def test_clickable_scrolling_sliders_if_click_on_left_arrow(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsDetailedPage(web_browser, url + NewsDetailedPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к слайдеру"):
        page.arrow_left_button.scroll_to_element()
    with allure.step("Нажимаем на стрелочку"):
        page.arrow_left_button.click()
    with allure.step("Проверяем, что следующий слайд стал активным"):
        time.sleep(0.3)
        next_slide_index = int(page.active_slider.get_attribute('data-swiper-slide-index'))
        assert 3 == next_slide_index


@allure.issue("https://portal.onpeak.ru/company/personal/user/575/tasks/task/view/101118/",
              "Разработка автотестов для страницы новостей")
@allure.suite("Проверка, что кнопка \"Вернуться к блогу\" нажимается")
def test_clickable_return_to_blog_button(web_browser, url):
    with allure.step("Открываем страницу новостей"):
        page = NewsDetailedPage(web_browser, url + NewsDetailedPage.path)
    with allure.step("Ожидаем открытие страницы"):
        page.wait_page_loaded()
    with allure.step("Спускаемся к кнопке"):
        page.back_to_blog_button.scroll_to_element()
    with allure.step("Проверяе: нажимается ли кнопка"):
        assert page.back_to_blog_button.is_clickable()
