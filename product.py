from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class LoginSystem(unittest.TestCase):
    def setUp(self):
        PATH = "C:\Program Files (x86)\Chromedriver\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://app.jubelio.com/login")
        loginword = self.driver.find_element(By.CSS_SELECTOR,"h1").text
        self.assertEqual("Login", loginword)

        # Input data
        self.driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
        self.driver.find_element(By.CSS_SELECTOR,"button").click()
        time.sleep(2)

        # Inventory submenu
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="wrapper"]/nav/div/div/ul/li[2]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="wrapper"]/nav/div/div/ul/li[2]/ul/li[2]/a').click()
    
    # def test_exportInventory(self):
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH,"//button[contains(text(), 'Eksport')]").click()
    #     self.driver.current_url == "https://app.jubelio.com/home/reports/exports"
    #     self.driver.find_element(By.XPATH,"//span[contains(text(), 'Refresh')]").click()

    # def test_searchInventory(self):    
    #     time.sleep(5)
    #     data = 'RM-CHO-IJH'
    #     self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Nama, SKU, Merek Lain']").send_keys(data)
    #     self.driver.find_element(By.XPATH,"//span[contains(@class,'glyphicon')]").click()

    #     #Response
    #     assertData = self.driver.find_element(By.XPATH,f"//button[contains(text(), '{data}')]").text
    #     self.assertRegexpMatches(assertData, data)

    # def test_inventoryAdjustment(self):
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH,"//span[contains(text(), 'Penyesuaian Persediaan')]").click()

    #     time.sleep(5)
    #     data = 'RM-CHO-IJH'
    #     self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Scan']").send_keys(data)
    #     self.driver.find_element(By.XPATH,"//span[contains(text(), 'Scan')]").click()

    def test_importProduct(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[contains(text(), 'Import Stock')]").click()

        
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()