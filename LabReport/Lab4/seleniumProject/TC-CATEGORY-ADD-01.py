import unittest
from MyWebOperator import MyWebOperator

class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
    
    def test(self):
        self.webOperator.add_category("TC-CATEGORY-ADD-01")
        self.webOperator.category_exist("TC-CATEGORY-ADD-01")
    
    def tearDown(self):
        self.webOperator.delete_category("TC-CATEGORY-ADD-01")
        self.webOperator.sign_out()
        self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()