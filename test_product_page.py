import pytest
import faker

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.user
class TestUserAddToBasketFromProductPage:

    '''
    Открыть страницу регистрации;
    Зарегистрировать нового пользователя;
    Проверяем, что пользователь авторизирован.
    '''
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        self.login_page.open()
        self.login_page.register_new_user(faker.Faker().email(), faker.Faker().password())
        self.login_page.should_be_authorized_user()

    '''
    Открыть страницу с продуктом;
    Проверяем, что нет сообщения об успехе.
    '''
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link) 
        page.open()
        page.should_not_be_success_message()

    '''
    Открыть страницу с продуктом;
    Добавить продукт в корзину;
    Решить задачу в окне alert;
    Проверяем, что название товара в корзине соответствует названию добавленного товара;
    Проверяем, что цена товара в корзине соответствует цене добавленного товара.
    '''
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
                                   marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link) 
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_page()
        
'''
Открыть страницу с продуктом;
Добавить продукт в корзину;
Решить задачу в окне alert;
Проверяем, что название товара в корзине соответствует названию добавленного товара;
Проверяем, что цена товара в корзине соответствует цене добавленного товара.
'''
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
                                   marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_page()

'''
Открыть страницу с продуктом;
Перейти в корзину;
Решить задачу в окне alert;
Проверяем, что товар и цена отсутствуют;
'''
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()

'''
Открываем страницу товара 
Добавляем товар в корзину 
Решить задачу в окне alert
Проверяем, что нет сообщения об успехе с помощью is_not_element_present
'''
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

'''
Открываем страницу товара 
Проверяем, что нет сообщения об успехе с помощью is_not_element_present
'''
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()
    page.should_not_be_success_message()

'''
Открываем страницу товара
Добавляем товар в корзину
Проверяем, что нет сообщения об успехе с помощью is_disappeared
'''
@pytest.mark.newtest
# @pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappeared()

'''
Открыть страницу с продуктом;
Проверить, что есть ссылка для перехода на страницу входа/регистрации.
'''
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

'''
Открыть страницу с продуктом;
Перейти на страницу входа/регистрации.
'''
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    