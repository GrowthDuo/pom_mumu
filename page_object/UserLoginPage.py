# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from base.BasePage import BasePage
#
# class UserLoginPage(BasePage):
#
#     user_name = (By.XPATH, "//input[@class='el-input__inner']")
#     user_password = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div[1]/input')
#     user_button = (By.XPATH, '//*[@id="app"]/div/form/div[3]/div/button')
#     user_title = (By.XPATH, "//div[@class='el-submenu__title']")
#
#     # def goto_user_login_page(self):
#     #     # 网页地址
#     #     self.url = url()
#     #     self.driver.get(self.url)
#     #     # 等待页面加载完成
#     #     self.driver.wait_for_page_load()
#     #     # 等待元素消失
#     #     self.driver.wait_for_element_gone()
#     #     # 最大化窗口
#     #     self.driver.maximize_window()
#
#     def input_username(self, username):
#         # 等待元素可见
#         self.wait_for_element_visible(*self.user_name)
#         self.clear_input(*self.user_name)
#         self.input_text(username, *self.user_name)
#
#     def input_pwd(self, pwd):
#         self.wait_for_element_visible(*self.user_password)
#         self.clear_input(*self.user_password)
#         self.input_text(pwd, *self.user_password)
#
#     def login_click(self):
#         # 等待元素可点击
#         self.wait_for_element_clickable(*self.user_button)
#         self.click(*self.user_button)
#     # 登录成功后，等待标题可见
#     def wait_for_title(self):
#         self.wait_for_element_visible(*self.user_title)
#
#     # ????????...
from selenium.webdriver.common.by import By
from base.BasePage import BasePage

class UserLoginPage(BasePage):
    user_name = (By.XPATH, "//input[@class='el-input__inner']")
    user_password = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div[1]/input')
    user_button = (By.XPATH, '//*[@id="app"]/div/form/div[3]/div/button')
    user_title = (By.XPATH, "//div[@class='el-submenu__title']")

    def input_username(self, username):
        self.wait_for_element_visible(*self.user_name)
        self.clear_input(*self.user_name)
        self.input_text(username, *self.user_name)

    def input_pwd(self, pwd):
        self.wait_for_element_visible(*self.user_password)
        self.clear_input(*self.user_password)
        self.input_text(pwd, *self.user_password)

    def login_click(self):
        self.wait_for_element_clickable(*self.user_button)
        self.click(*self.user_button)

    def wait_for_title(self):
        self.wait_for_element_visible(*self.user_title)
