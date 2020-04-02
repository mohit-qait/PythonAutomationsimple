from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest

class DummyTest(unittest.TestCase):
    
    def testsetup(self):
        global driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        
    #def testlogin(self):
        element=driver.find_element_by_id("user-name")
        element.send_keys("standard_user")
        element=driver.find_element_by_id("password")
        element.send_keys("secret_sauce")
        element=driver.find_element_by_class_name("btn_action")
        element.click();
        element=driver.find_element_by_class_name("product_label")
        print(element.text)
        self.assertEqual("Products",element.text,"Test is PAssed")
        self.assertTrue(True, "Test passed")
        self.assertTrue(True, "Test passed")
        self.assertTrue(True, "Test passed")
        self.assertTrue(True, "Test passed")
        self.assertTrue(True, "Test passed")
        self.assertTrue(True, "Test passed")

               
if __name__ == "__main__":
    unittest.main()        
        
