import unittest
from MyWebOperator import MyWebOperator

class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
    
    def test(self):
        self.webOperator.add_user("FN", "LN", "userEmail@gmail.com", "userpassword123", "userpassword123")
        self.webOperator.user_exist("FN", "LN")
    
    def tearDown(self):
        # issue on delete user(can't delete user by UI)
        self.webOperator.sign_out()
        self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()