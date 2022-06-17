import unittest
from MyWebOperator import MyWebOperator
from selenium.webdriver.common.by import By

class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    driver = webOperator.driver
    wait = webOperator.wait
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
        self.webOperator.add_post("TC-POST-SEARCH-01")
        self.webOperator.post_exist("TC-POST-SEARCH-01")
    
    def test(self):
        self.webOperator.search_post("TC-POST-SEARCH-01")
        self.webOperator.post_exist("TC-POST-SEARCH-01")
        self.webOperator.search_post("TC-POST-SEARCH-02")
        postResultXpath = "//*[contains(@class, 'ItemList__col')]//*[text() = 'TC-POST-DEL-02']"
        postList = self.driver.find_elements(By.XPATH, postResultXpath)
        self.assertTrue( len(postList) == 0 ) # 檢查頁面搜尋不到
        
    def tearDown(self):
        self.webOperator.cancel_search() 
        self.webOperator.delete_post("TC-POST-SEARCH-01")
        self.webOperator.sign_out()
        self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()