from selenium import webdriver
import unittest
from pages.loginpage import LoginPage
from pages.logoutpage import HomePage
import HtmlTestRunner

class FB_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Valid_Login(self):
        driver = self.driver
        self.driver.get("http://facebook.com")
        Log_in = LoginPage(driver)

        Log_in.enter_username("tardtypical@gmail.com")
        Log_in.enter_password("01120090020k")
        Log_in.click_login()

        Log_out = HomePage(driver)

        Log_out.click_navigator()
        Log_out.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Shiva Ravi Raja/Desktop/logos'))
