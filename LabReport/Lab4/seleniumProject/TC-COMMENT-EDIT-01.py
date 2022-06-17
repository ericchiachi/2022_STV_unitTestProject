import unittest
from MyWebOperator import MyWebOperator

class testAddPost(unittest.TestCase):
    
    webOperator = MyWebOperator()
    commentID = None
    
    def setUp(self):
        self.webOperator.login("demo@keystonejs.com", "demo")
        self.webOperator.add_post("demoPost2")
        self.webOperator.from_post_page_to_main_page()
        self.webOperator.add_post("demoPost1")
        self.webOperator.from_post_page_to_main_page()
        self.commentID = self.webOperator.add_comment("Demo User", "demoPost1")
        self.webOperator.comment_exist(self.commentID)
    
    def test(self):
        self.webOperator.into_edit_comment_page(self.commentID)
        self.webOperator.change_comment_post("demoPost2")
        self.webOperator.click_save_comment_button()
        self.webOperator.from_comment_edit_page_to_comment_page()
        # author = self.webOperator.get_comment_author(self.commentID)
        post = self.webOperator.get_comment_post(self.commentID)
        # self.assertEqual( "Demo User", author )
        self.assertEqual( "demoPost2", post )
        
    # def tearDown(self):
        # self.webOperator.delete_comment(self.commentID)
        # self.webOperator.from_comment_page_into_main_page()
        # self.webOperator.into_post_page()
        # self.webOperator.delete_post("demoPost2")
        # self.webOperator.delete_post("demoPost1")
        # self.webOperator.sign_out()
        # self.webOperator.close_browser()


if __name__ == "__main__":
    unittest.main()