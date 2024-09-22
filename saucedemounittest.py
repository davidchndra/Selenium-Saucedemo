import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

        driver.find_element(By.ID, "user-name").send_keys('inputUsername')
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('inputPassword')
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        error_msg = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
        self.assertIn("Username and password do not match", error_msg)

    def test_login_failed_locked_user(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Swag Labs", driver.title)

        driver.find_element(By.ID, "user-name").send_keys('locked_out_user')
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        error_msg = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
        self.assertIn("this user has been locked out", error_msg)
        
    def test_login_success(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Swag Labs", driver.title)

        driver.find_element(By.ID, "user-name").send_keys('standard_user')
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        get_url = driver.current_url
        self.assertIn('/inventory.html', get_url)

    def test_login_success_add_to_cart(self):
        driver = self.driver
        driver.get(self.url)
        self.assertIn("Swag Labs", driver.title)

        driver.find_element(By.ID, "user-name").send_keys('standard_user')
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        #assert new url setelah login
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