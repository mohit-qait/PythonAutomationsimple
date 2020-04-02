from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest

class SeleniumEasy(unittest.TestCase):
    def testsetup(self):
        global driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.seleniumeasy.com/test/")
        
        
        element=driver.find_element_by_id("btn_basic_example")
        element.click()
        driver.find_elements_by_css_selector("#basic > div > a:nth-child(1)").click()
       
        
        element=driver.find_elements_by_css_selector("#treemenu > li > ul > li:nth-child(1) > a")
        element.click()
        

if __name__ == "__main__":
    unittest.main()
    
