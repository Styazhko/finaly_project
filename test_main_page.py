import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:

    '''
    Открыть главную страницу;
    Перейти на страницу входа/регистрации;
    Проверить, что данная страница является страницой входа/регистрации пользователя.
    '''            
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) 
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    '''
    Открыть главную страницу;
    Проверяем, что есть ссылка для перехода на страницу входа/регистрации.
    '''
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) 
        page.open()
        page.should_be_login_link()

'''
Открыть главную страницу;
Перейти в корзину;
Проверяем, что продукты в корзине отсутствуют.
'''
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()