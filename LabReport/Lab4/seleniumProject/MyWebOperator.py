import unittest
from requests import delete
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import Select

class MyWebOperator:
    
    driver = None
    wait = None
    
    def __init__(self):
        chromedriver = Service("/usr/local/bin/chromedriver")
        self.driver = webdriver.Chrome(service=chromedriver, options=webdriver.ChromeOptions())
        self.wait = WebDriverWait(self.driver, timeout=12, poll_frequency=100)
        self.driver.implicitly_wait(10)
    
    def login(self, account, password):
        driver = self.driver
        driver.get("http://127.0.0.1:3000/")
        self.wait.until(expected_conditions.title_is("Keystone Demo"))
        print("==== Title is Appear ====")
        elem_signIn = driver.find_element(By.LINK_TEXT, "Sign In")
        elem_signIn.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "css-1frap0z")))
        print("==== Load in sign in page finish ====")
        elem_emailTextBox = driver.find_element(By.NAME, "email")
        elem_passwordTextBox = driver.find_element(By.NAME, "password")
        elem_emailTextBox.send_keys(account)
        elem_passwordTextBox.send_keys(password)
        elem_signInBtn = driver.find_element(By.XPATH, "//*[@class='auth-box__col']//*[@type='submit']")
        elem_signInBtn.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.CLASS_NAME, "dashboard-group__heading")))
        print("==== Sign in finish ====")

    def sign_out(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//*[@class='octicon octicon-sign-out']").click()

    def close_browser(self):
        self.driver.close()
        
        
    ############### 主頁面 ################
    def into_post_page(self):
        # 在主頁面才可使用
        driver = self.driver
        btn_intoPostList = driver.find_element(By.XPATH, "//*[@href='/keystone/posts']//*[@class='dashboard-group__list-label']")
        btn_intoPostList.click()
        # self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[contains(@title, 'Create Post')]")))
        sleep(3)
    
    def add_post(self, postName):
        # 在主頁面才可使用
        driver = self.driver
        self.into_add_post_page()
        self.input_post_name_and_save(postName)
        self.from_post_edit_page_to_post_page()
        print("==== add post finish ====")
    
    def add_comment(self, author, postName):
        # 在主頁面才可使用
        driver = self.driver
        self.into_add_comment_page()
        self.input_author_and_post_and_save(author, postName)
        commentID = driver.find_element(By.CLASS_NAME, "EditForm__name-field").text
        self.from_comment_edit_page_to_comment_page()
        return commentID

    def add_category(self, categoryName):
        # 在主頁面才可使用
        driver = self.driver
        self.into_add_category_page()
        self.input_category_name_and_save(categoryName)
        self.from_category_edit_page_to_category_page()
        print("==== add category finish ====")
 
    def add_user(self, firstName, lastName, email, password, confirmpassword):
        # 在主頁面才可使用
        driver = self.driver
        self.into_add_user_page()
        self.input_user_info_and_save(firstName, lastName, email, password, confirmpassword)
        self.from_user_edit_page_to_user_page()
        print("==== add user finish ====") 
    
    def into_add_post_page(self):
        # 在主頁面才可使用
        driver = self.driver
        elem_addPostBtn = driver.find_element(By.XPATH, "//*[@class='dashboard-group__list-create octicon octicon-plus' and contains(@href,'posts')]")
        elem_addPostBtn.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.NAME, "name")))
 
    def into_add_comment_page(self):
        # 在主頁面才可使用
        driver = self.driver
        elem_addCommentBtn = driver.find_element(By.XPATH, "//*[@class='dashboard-group__list-create octicon octicon-plus' and contains(@href,'comments')]")
        elem_addCommentBtn.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[@for='author']//*[@class='Select-multi-value-wrapper']")))

    def into_add_category_page(self):
        # 在主頁面才可使用
        driver = self.driver
        elem_addPostBtn = driver.find_element(By.XPATH, "//*[@class='dashboard-group__list-create octicon octicon-plus' and contains(@href,'categories')]")
        elem_addPostBtn.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[text()='Create a new Category']")))

    def into_add_user_page(self):
        # 在主頁面才可使用
        driver = self.driver
        elem_addPostBtn = driver.find_element(By.XPATH, "//*[@class='dashboard-group__list-create octicon octicon-plus' and contains(@href,'users')]")
        elem_addPostBtn.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[text()='Create a new User']")))
    
    ############### post頁面 ################
    def post_exist(self, postName):
        # 在post頁面才能使用
        driver = self.driver
        postResultXpath = "//*[contains(@class, 'ItemList__col')]//*[text() = '" + postName + "']"
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, postResultXpath)))
        print("==== post exist ====")
    
    def into_edit_post_page(self, postName):
        # 在post頁面才能使用
        driver = self.driver
        postlinkXpath = "//*[contains(@class, 'ItemList__col')]//*[text() = '" + postName + "']"
        elem_btnPost = driver.find_element(By.XPATH, postlinkXpath)
        elem_btnPost.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[@class='Toolbar__section Toolbar__section--left']//*[@href='/keystone/posts']")))
        
    def delete_post(self, postName):
        # 在post頁面才能使用
        driver = self.driver
        self.into_edit_post_page(postName)
        self.click_delete_post_button()
        btn_delete_doDelete = driver.find_element(By.XPATH, "//*[contains(@data-button-type, 'confirm')]")
        btn_delete_doDelete.click()
        # self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[contains(@title, 'Create Post')]")))
        sleep(3)
    
    def search_post(self, postName):
        # 在post頁面才能使用
        driver = self.driver
        search_textBox = driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='Search']")
        search_textBox.clear()
        search_textBox.send_keys(postName)
        sleep(2) # 無法確實驗證搜尋結果，直接等待

    def from_post_page_to_main_page(self):
        # 在post頁面才能使用
        self.wait.until(expected_conditions.visibility_of(self.driver.find_element(By.XPATH, "//*[@class='octicon octicon-home']")))
        self.driver.find_element(By.XPATH, "//*[@class='octicon octicon-home']").click()
        self.wait.until(expected_conditions.visibility_of(self.driver.find_element(By.CLASS_NAME, "dashboard-group__heading")))

    def cancel_search(self):
        self.driver.find_element(By.XPATH, "//*[@title='Clear search query' and @type='button']").click()


    ############### comment頁面 ################
    def comment_exist(self, commentID):
        # 在comment頁面才能使用
        driver = self.driver
        commentXpath = "//*[contains(@title, '" + commentID + "')]"
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, commentXpath)))
        print("==== comment exist ====")

    def delete_comment(self, commentID):
        # 在comment頁面才能使用
        driver = self.driver
        self.into_edit_comment_page(commentID)
        self.click_delete_comment_button()
        btn_delete_doDelete = driver.find_element(By.XPATH, "//*[contains(@data-button-type, 'confirm')]")
        btn_delete_doDelete.click()
        # self.wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, "//*[contains(@data-button, 'delete')]")))
        sleep(3)

    def into_edit_comment_page(self, commentID):
        # 在comment頁面才能使用
        driver = self.driver
        commentXpath = "//*[contains(@title, '" + commentID + "')]"
        elem_btnPost = driver.find_element(By.XPATH, commentXpath)
        elem_btnPost.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[contains(@data-button, 'delete')]")))

    def from_comment_page_into_main_page(self):
        # 在comment頁面才能使用
        self.wait.until(expected_conditions.visibility_of(self.driver.find_element(By.XPATH, "//*[@class='octicon octicon-home']")))
        self.driver.find_element(By.XPATH, "//*[@class='octicon octicon-home']").click()
        self.wait.until(expected_conditions.visibility_of(self.driver.find_element(By.CLASS_NAME, "dashboard-group__heading")))
    
    def get_comment_author(self, commentID):
        author = self.driver.find_elements(By.XPATH, "//*[@class='ItemList__col']//*[@href='/keystone/post-comments/" + commentID + "']/../..//*[contains(@href, '/keystone/users/')]")[0].text
        print(author)
        return author
    
    def get_comment_post(self, commentID):
        post = self.driver.find_elements(By.XPATH, "//*[@class='ItemList__col']//*[@href='/keystone/post-comments/" + commentID + "']/../..//*[contains(@href, '/keystone/posts/')]")[0].text
        print(post)
        return post    

    ############### category頁面 ################
    def category_exist(self, categoryName):
        # 在category頁面才能使用
        driver = self.driver
        postResultXpath = "//*[contains(@class, 'ItemList__col')]//*[text() = '" + categoryName + "']"
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, postResultXpath)))
        print("==== post exist ====")
    
    def delete_category(self, categoryName):
        driver = self.driver
        self.into_edit_category_page(categoryName)
        self.click_delete_category_button()
        btn_delete_doDelete = driver.find_element(By.XPATH, "//*[contains(@data-button-type, 'confirm')]")
        btn_delete_doDelete.click()
        # self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[contains(@title, 'Create Post')]")))
        sleep(3)
        
    def into_edit_category_page(self, categoryName):
        driver = self.driver
        postlinkXpath = "//*[contains(@class, 'ItemList__col')]//*[text() = '" + categoryName + "']"
        elem_btnPost = driver.find_element(By.XPATH, postlinkXpath)
        elem_btnPost.click()
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, "//*[@class='Toolbar__section Toolbar__section--left']//*[@href='/keystone/post-categories']")))


    ############### user頁面 ################
    def user_exist(self, firstName, lastName):
        driver = self.driver
        postResultXpath = "//*[contains(@class, 'ItemList__col')]//*[text() = '" + firstName + " " + lastName + "']"
        self.wait.until(expected_conditions.visibility_of(driver.find_element(By.XPATH, postResultXpath)))
        print("==== user exist ====")

    ############### 創立post頁面 ################
    def input_post_name_and_save(self, postName):
        # 在創立post頁面才可使用
        driver = self.driver
        elem_addPostTextBox = driver.find_element(By.NAME, "name")
        elem_addPostTextBox.send_keys(postName)
        elem_btnCreate = driver.find_element(By.XPATH, "//*[contains(@data-button-type,'submit')]")
        elem_btnCreate.click()

    def click_cancel_create_post_button(self):
        # 在創立post頁面才可使用
        elem_btn_cancel = self.driver.find_element(By.XPATH, "//*[@data-button-type='cancel']")
        elem_btn_cancel.click()
    
    
    ############### 創立comment頁面 ################
    def input_author_and_post_and_save(self, author, postName):
        # 在創立comment頁面才可使用
        driver = self.driver
        elem_authorTextBox = driver.find_element(By.XPATH, "//*[@for='author']//*[@class='Select-multi-value-wrapper']")
        elem_authorTextBox.click()
        driver.find_elements(By.XPATH, "//*[@class='Select-menu-outer']")[0].click()
        elem_postTextBox = driver.find_element(By.XPATH, "//*[@for='post']//*[@class='Select-multi-value-wrapper']")
        elem_postTextBox.click()
        driver.find_elements(By.XPATH, "//*[@class='Select-menu-outer']")[0].click()
        elem_btnCreate = driver.find_element(By.XPATH, "//*[contains(@data-button-type,'submit')]")
        elem_btnCreate.click()
    
    
    ############### 創立category頁面 ################
    def input_category_name_and_save(self, categoryName):
        # 在創立category頁面才可使用
        driver = self.driver
        elem_addPostTextBox = driver.find_element(By.NAME, "name")
        elem_addPostTextBox.send_keys(categoryName)
        elem_btnCreate = driver.find_element(By.XPATH, "//*[contains(@data-button-type,'submit')]")
        elem_btnCreate.click()

    ############### 創立user頁面 ################
    def input_user_info_and_save(self, firstName, lastName, email, password, confirmpassword):
        driver = self.driver
        firstName_textBox = driver.find_element(By.NAME, "name.first")
        firstName_textBox.send_keys(firstName)
        lastName_textBox = driver.find_element(By.NAME, "name.last")
        lastName_textBox.send_keys(lastName)
        email_textBox = driver.find_element(By.NAME, "email")
        email_textBox.clear()
        email_textBox.send_keys(email)
        password_textBox = driver.find_element(By.NAME, "password")
        password_textBox.clear()
        password_textBox.send_keys(password)
        password_confirm_textBox = driver.find_element(By.NAME, "password_confirm")
        password_confirm_textBox.send_keys(confirmpassword)
        elem_btnCreate = driver.find_element(By.XPATH, "//*[contains(@data-button-type,'submit')]")
        elem_btnCreate.click()

    ############### post編輯頁面 ################
    def click_delete_post_button(self):
        # 在post編輯頁面才可使用
        elem_btn_delete = self.driver.find_element(By.XPATH, "//*[contains(@data-button, 'delete')]")
        elem_btn_delete.click()
    
    def click_save_post_button(self):
        # 在post編輯頁面才可使用
        elem_btn_save = self.driver.find_element(By.XPATH, "//*[@data-button='update']")
        elem_btn_save.click()
        
    def click_reset_post_button(self):
        btn_reset = self.driver.find_element(By.XPATH, "//*[@data-button='reset']")
        btn_reset.click()
    
    def click_reset_and_confirm_button(self):
        self.click_reset_post_button()
        self.wait.until(expected_conditions.visibility_of(self.driver.find_element(By.XPATH, "//*[text()='Reset']")))
        self.driver.find_element(By.XPATH, "//*[text()='Reset']").click()
        self.wait.until(expected_conditions.visibility_of(self.driver.find_element(By.XPATH, "//*[text()='Save']")))

    def from_post_edit_page_to_post_page(self):
        # 在post編輯頁面才可使用
        driver = self.driver
        elem_btnReturnPostList = driver.find_element(By.XPATH, "//*[@class='Toolbar__section Toolbar__section--left']//*[@href='/keystone/posts']")
        elem_btnReturnPostList.click()


    ############### comment編輯頁面 ################
    def from_comment_edit_page_to_comment_page(self):
        # 在comment編輯頁面才可使用
        driver = self.driver
        elem_btnReturnPostList = driver.find_element(By.XPATH, "//*[@class='Toolbar__section Toolbar__section--left']//*[@href='/keystone/post-comments']")
        elem_btnReturnPostList.click()
    
    def click_delete_comment_button(self):
        # 在comment編輯頁面才可使用
        elem_btn_delete = self.driver.find_element(By.XPATH, "//*[contains(@data-button, 'delete')]")
        elem_btn_delete.click()
    
    def click_save_comment_button(self):
        # 在comment編輯頁面才可使用
        elem_btn_save = self.driver.find_element(By.XPATH, "//*[@data-button='update']")
        elem_btn_save.click()
    
    def change_comment_post(self, postName):
        self.driver.find_element(By.XPATH, "//*[@for='post']//*[@class='Select-value']").click()
        options = self.driver.find_elements(By.XPATH, "//*[@class='Select-menu-outer']")
        print(options)
        print(options[0])
        options[0].click()
        
    ############### category編輯頁面 ################
    def from_category_edit_page_to_category_page(self):
        driver = self.driver
        elem_btnReturnPostList = driver.find_element(By.XPATH, "//*[@class='Toolbar__section Toolbar__section--left']//*[@href='/keystone/post-categories']")
        elem_btnReturnPostList.click()

    def click_delete_category_button(self):
        elem_btn_delete = self.driver.find_element(By.XPATH, "//*[contains(@data-button, 'delete')]")
        elem_btn_delete.click()
        
        
    ############### user編輯頁面 ################
    def from_user_edit_page_to_user_page(self):
        driver = self.driver
        elem_btnReturnPostList = driver.find_element(By.XPATH, "//*[@class='Toolbar__section Toolbar__section--left']//*[@href='/keystone/users']")
        elem_btnReturnPostList.click()