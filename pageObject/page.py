from selenium.webdriver.common.by import By

class login_page():
    username = 'user-name'
    password = 'password'
    login_btn = 'login-button'
    error_msg = "[data-test='error']"

    find_username = (By.NAME, 'user-name')
    find_password = (By.CSS_SELECTOR, '[data-test="password"]')
    find_loginbtn = (By.ID, 'login-button')
    find_errormsg = (By.CSS_SELECTOR, '[data-test="error"]')
