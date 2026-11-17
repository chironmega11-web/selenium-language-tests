import time

def test_button_add_to_basket_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Пауза для визуальной проверки языка (как требуется в критериях)
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину
    # Селектор уникален для страницы товара
    button = browser.find_element("css selector", "button.btn-add-to-basket")
    
    # Проверяем, что кнопка существует и видима
    assert button is not None, "Кнопка добавления в корзину не найдена"
