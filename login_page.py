import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    # Locals
    your_email = "input here"
    your_pass = "input here"
    

    # Locators
    login_with_pass_locator = "//*[@id='HH-React-Root']/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/form/div[4]/button[2]"
    mail_bar_locator = "//*[@id='HH-React-Root']/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[1]/fieldset/input"
    password_locator = "//*[@id='HH-React-Root']/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[2]/fieldset/input"
    enter_locator = "//*[@id='HH-React-Root']/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[4]/div/button[1]"

    
   # Getters

    def get_mail_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail_bar_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))

    def get_login_with_pass(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.login_with_pass_locator)))

    def get_enter(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.enter_locator)))



    # Actions

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


    # Methods
    def login_with_pass(self):
        self.click_login_with_pass()
        self.get_current_url()
        self.input_mail(your_email)
        self.input_password(your_pass)
        self.click_enter()


