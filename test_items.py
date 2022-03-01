import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_should_have_add_to_basket_button(browser):
    browser.get(link)
    marker = browser.find_elements_by_css_selector('[class = "btn btn-lg btn-primary btn-add-to-basket"]')
    assert marker, "Кнопка не найдена"