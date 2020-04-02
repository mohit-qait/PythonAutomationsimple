import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')
        driver.get("https://bing.com")
        titleOfWebPage = driver.title
        # verify title is bing
        self.assertEqual("Bing", titleOfWebPage, "webpage title is not matching")
if __name__ == "__main__":
    unittest.main()