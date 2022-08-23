import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page
from pages.main_page import Main_page
from selenium.webdriver.chrome.options import Options


def test_buy_product_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\bomj\\PycharmProjects\\resource\\chromedriver.exe',
                              chrome_options=options)

    print("Start test 1")
    """Заходим на страницу с вакансиями"""
    mp = Main_page(driver)
    mp.click_login()

    """Проходим авторизацию"""
    lp = Login_page(driver)
    lp.login_with_pass()

    """Заполняем отклики"""
    i=0
    while i < 180:
        mp.accept_vacancy_on_page()
        i += 1
        print("Вы отправили откликов : " + str(i))

    print("Все отклики были отправлены успешно!")
    time.sleep(1)
