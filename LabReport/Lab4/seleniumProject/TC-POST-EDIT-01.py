import unittest
from MyWebOperator import MyWebOperator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep


class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    driver = webOperator.driver
    wait = webOperator.wait
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
        self.webOperator.add_post("TC-POST-EDIT-01")
    
    def test(self):
        self.webOperator.into_edit_post_page("TC-POST-EDIT-01")
        postName_text_box = self.webOperator.driver.find_element(By.XPATH, "//*[@name='name']")
        postName_text_box.clear()
        postName_text_box.send_keys("TC-POST-EDITED")
        self.webOperator.click_save_post_button()
        self.webOperator.from_post_edit_page_to_post_page()
        self.webOperator.post_exist("TC-POST-EDITED")
    
    def tearDown(self):
        self.webOperator.delete_post("TC-POST-EDITED")
        self.webOperator.sign_out()
        self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()