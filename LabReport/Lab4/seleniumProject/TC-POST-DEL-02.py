import unittest
from MyWebOperator import MyWebOperator
from selenium.webdriver.common.by import By

class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    driver = webOperator.driver
    wait = webOperator.wait
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
        self.webOperator.add_post("TC-POST-DEL-01")
        self.webOperator.post_exist("TC-POST-DEL-01")
    
    def test(self):
        self.webOperator.into_edit_post_page("TC-POST-DEL-01")
        self.webOperator.click_delete_post_button()
        btn_delete_cancelDelete = self.driver.find_element(By.XPATH, "//*[contains(@data-button-type, 'cancel')]")
        btn_delete_cancelDelete.click()
        self.webOperator.from_post_edit_page_to_post_page()
        self.webOperator.post_exist("TC-POST-DEL-01")
    
    def tearDown(self):
        self.webOperator.delete_post("TC-POST-DEL-01")
        self.webOperator.sign_out()
        self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()