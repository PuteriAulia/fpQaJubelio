from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class LoginSystem(unittest.TestCase):
    def setUp(self):
        PATH = "C:\Program Files (x86)\Chromedriver\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://app.jubelio.com/login")

    def test_LoginWithRegisteredData(self):
        loginword = self.driver.find_element(By.CSS_SELECTOR,"h1").text
        self.assertEqual("Login", loginword)

        # Input data
        self.driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
        self.driver.find_element(By.CSS_SELECTOR,"button").click()
        
        # Response
        self.driver.current_url == "https://app.jubelio.com/home/getting-started"

    def test_LoginWithInvalidEmail(self):
        loginword = self.driver.find_element(By.CSS_SELECTOR,"h1").text
        self.assertEqual("Login", loginword)

        # Input data
        self.driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubeliogmail.com")
        failAlert = self.driver.find_element(By.CLASS_NAME,"help-block").text
        self.assertRegexpMatches(failAlert, "Format Email tidak valid.")

        self.driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
        self.driver.find_element(By.CSS_SELECTOR,"button").click()

        # Response
        self.driver.current_url == "https://app.jubelio.com/login"
        time.sleep(2)
        failAlert = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]').text
        self.assertRegexpMatches(failAlert, "Format Email tidak valid.")

    def test_LoginWithUnregisteredEmail(self):
        loginword = self.driver.find_element(By.CSS_SELECTOR,"h1").text
        self.assertEqual("Login", loginword)

        # Input data
        self.driver.find_element(By.NAME, "email").send_keys("rakamin.jubelio@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
        self.driver.find_element(By.CSS_SELECTOR,"button").click()

        # Response
        self.driver.current_url == "https://app.jubelio.com/login"
        time.sleep(2)
        failAlert = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]').text
        self.assertRegexpMatches(failAlert, "Password atau email anda salah.")

    def test_LoginWithUnregisteredPassword(self):
        loginword = self.driver.find_element(By.CSS_SELECTOR,"h1").text
        self.assertEqual("Login", loginword)

        # Input data
        self.driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Jubelio123")
        self.driver.find_element(By.CSS_SELECTOR,"button").click()

        # Response
        self.driver.current_url == "https://app.jubelio.com/login"
        time.sleep(2)
        failAlert = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]').text
        self.assertRegexpMatches(failAlert, "Password atau email anda salah.")
    
    def test_LoginWithoutInputAnydata(self):
        loginword = self.driver.find_element(By.CSS_SELECTOR,"h1").text
        self.assertEqual("Login", loginword)

        # Input data
        self.driver.find_element(By.CSS_SELECTOR,"button").click()

        # Response
        self.driver.current_url == "https://app.jubelio.com/login"
        time.sleep(2)
        failAlertEmail = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[1]/div/span').text
        self.assertRegexpMatches(failAlertEmail, "Email harus diisi.")

        failAlertPassword = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/div[2]/div/span').text
        self.assertRegexpMatches(failAlertPassword, "Password harus diisi.")
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()