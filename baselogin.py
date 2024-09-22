from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pageObject.page import login_page
from pageObject.input import inputan

def test_login(driver):
    driver.find_element(*login_page.find_username).send_keys('standard_user')
    driver.find_element(*login_page.find_password).send_keys('secret_sauce')
    driver.find_element(*login_page.find_loginbtn).click()