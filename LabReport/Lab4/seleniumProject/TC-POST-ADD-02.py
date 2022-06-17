import unittest
from MyWebOperator import MyWebOperator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    driver = webOperator.driver
    wait = webOperator.wait
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
    
    def test(self):
        self.webOperator.into_add_post_page()
        self.webOperator.input_post_name_and_save("")
        self.wait.until(expected_conditions.visibility_of(self.driver.find_element(By.XPATH, "//*[text()='Name is required']")))
    
    def tearDown(self):
        self.webOperator.click_cancel_create_post_button()
        self.webOperator.sign_out()
        self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()