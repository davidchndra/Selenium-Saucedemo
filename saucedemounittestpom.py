import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pageObject.page import login_page
from pageObject.input import inputan
import baselogin

class SauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.saucedemo.com/"

    def test_page_title(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Swag Labs", driver.title)

    def test_login_failed_wrong_credential(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Swag Labs", driver.title)

        driver.find_element(*login_page.find_username).send_keys(inputan.wrong_username)
        driver.find_element(*login_page.find_password).send_keys(inputan.wrong_password)
        driver.find_element(*login_page.find_loginbtn).click()
        error_message = driver.find_element(*login_page.find_errormsg).text
        self.assertIn(inputan.error_msg_wrong_pass, error_message)

    def test_login_failed_locked_user(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Swag Labs", driver.title)

        driver.find_element(*login_page.find_username).send_keys('locked_out_user')
        driver.find_element(*login_page.find_password).send_keys('secret_sauce')
        driver.find_element(*login_page.find_loginbtn).click()

        error_message = driver.find_element(*login_page.find_errormsg).text
        self.assertIn("this user has been locked out", error_message)
        
    def test_login_success(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Swag Labs", driver.title)

        driver.find_element(*login_page.find_username).send_keys('standard_user')
        driver.find_element(*login_page.find_password).send_keys('secret_sauce')
        driver.find_element(*login_page.find_loginbtn).click()

        get_url = driver.current_url
        self.assertIn('/inventory.html', get_url)

    def test_success_add_to_cart(self):
        driver = self.driver
        driver.get(self.url)

        baselogin.test_login(driver)
        
        #assert new login url after login
        get_url = driver.current_url
        self.assertIn('/inventory.html', get_url)

        #add to cart
        driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]').click()
        cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link').text
        
        #assert angka 1
        self.assertEqual(cart, '1')
        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

        #get link setelah click checkout
        get_url2 = driver.current_url
        self.assertIn('/cart.html', get_url2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()