import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    page = 0
    """Put ulr with your resume search area here"""
    url = 'https://hh.ru/search/vacancy?area=1&excluded_text=senior&resume=aa712ae1ff00d95d610039ed1f503475673845' \
          '&search_field=name&search_field=description&search_field=company_name&forceFiltersSaving=true&from' \
          '=resumelist&page=0&hhtmFrom=resume_list '

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_button_locator = "//*[@id='HH-React-Root']/div/div[2]/div[1]/div/div/div/div[6]/a"
    login_with_pass_locator = "//*[@id='HH-React-Root']/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/form/div[4]/button[2]"
    mail_bar_locator = "//*[@id='HH-React-Root']/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[1]/fieldset/input"
    password_locator = "//*[@id='HH-React-Root']/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[2]/fieldset/input"
    enter_locator = "//*[@id='HH-React-Root']/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[4]/div/button[1]"
    vacancy_locator = "//a[@data-qa='vacancy-serp__vacancy_response']"
    cover_letter_locator ="// *[ @ id = 'RESPONSE_MODAL_FORM_ID'] / div / div / div[3] / button"
    letter_bar_locator = "//textarea[@maxlength='10000']"
    response_button_locator = "//button[@data-qa='vacancy-response-submit-popup']"
    letter_text = "Добрый день! Я работал в фирме с agile системой kanban, готов к scrum спринтам. Выполнял smoke, black box, gray box и регрессионные тестирования. \
Hard skills: Python3, Си шарп, Lua, Jira, Selenium и Postman. Примеры скриптов по автоматизации лежат в github. \
Soft skills: Быстро и с интересом обучаюсь, предельно стрессоустойчив, в работе по качеству внимателен, въедлив, дотошен. При этом легок и приятен в общении. Умею гуглить. Английский - advanced, свободно читаю техническую документацию."


   # Getters
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button_locator)))

    def get_mail_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail_bar_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))

    def get_login_with_pass(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.login_with_pass_locator)))

    def get_enter(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.enter_locator)))

    def get_vacancy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.vacancy_locator)))

    def get_cover_letter(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cover_letter_locator)))

    def get_letter_bar(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.letter_bar_locator)))

    def get_response_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.response_button_locator)))

    # Actions
    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def input_mail(self, your_mail):
        self.get_mail_bar().send_keys(your_mail)
        print("Input mail : " + str(your_mail))


    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password : " + str(password))

    def click_login_with_pass(self):
        self.get_login_with_pass().click()
        print("Click login with pass")

    def click_enter(self):
        self.get_enter().click()
        print("Click enter button")

    def click_vacancy(self):
        self.get_vacancy().click()
        print("Click vacancy button")

    def click_cover_letter(self):
        self.get_cover_letter().click()
        print("Click vacancy button")

    def input_letter(self):
        self.get_letter_bar().send_keys(self.letter_text)
        print("Cover letter pasted")

    def click_response_button(self):
        self.get_response_button().click()
        print("Click send response button")

    # Methods

    def click_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_login_button()


    def accept_vacancy_on_page(self):
        self.click_vacancy()
        self.click_cover_letter()
        self.input_letter()
        self.click_response_button()
        self.driver.refresh()
        print("Отправлено откликов : " + str(num))
        time.sleep(5)


