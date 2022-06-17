import unittest
from MyWebOperator import MyWebOperator

class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    commentID = None
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
        self.webOperator.add_post("demoPost")
        self.webOperator.from_post_page_to_main_page()
    
    def test(self):
        self.commentID = self.webOperator.add_comment("Demo User", "demoPost")
        self.webOperator.comment_exist(self.commentID)
        author = self.webOperator.get_comment_author(self.commentID)
        post = self.webOperator.get_comment_post(self.commentID)
        self.assertEqual( "Demo User", author )
        self.assertEqual( "demoPost", post )
        
    def tearDown(self):
        self.webOperator.delete_comment(self.commentID)
        self.webOperator.from_comment_page_into_main_page()
        self.webOperator.into_post_page()
        self.webOperator.delete_post("demoPost")
        self.webOperator.sign_out()
        self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()