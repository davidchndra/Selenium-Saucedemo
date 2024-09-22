from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=option)
browser.get('https://www.saucedemo.com/')

assert 'Swag Labs' in browser.title

browser.find_element(By.ID, "user-name").send_keys('usernameInput')
browser.find_element(By.XPATH, "//input[@id='password']").send_keys('passwordInput')
browser.find_element(By.XPATH, "//input[@id='login-button']").click()
