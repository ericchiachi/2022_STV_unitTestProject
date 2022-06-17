import unittest
from MyWebOperator import MyWebOperator

class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
        self.webOperator.add_post("TC-POST-ADD-01")
    
    def test(self):
        self.webOperator.post_exist("TC-POST-ADD-01")
    
    def tearDown(self):
        self.webOperator.delete_post("TC-POST-ADD-01")
        self.webOperator.sign_out()
        self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()