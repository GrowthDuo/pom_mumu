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
#     #     # ��ҳ��ַ
#     #     self.url = url()
#     #     self.driver.get(self.url)
#     #     # �ȴ�ҳ��������
#     #     self.driver.wait_for_page_load()
#     #     # �ȴ�Ԫ����ʧ
#     #     self.driver.wait_for_element_gone()
#     #     # ��󻯴���
#     #     self.driver.maximize_window()
#
#     def input_username(self, username):
#         # �ȴ�Ԫ�ؿɼ�
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
#         # �ȴ�Ԫ�ؿɵ��
#         self.wait_for_element_clickable(*self.user_button)
#         self.click(*self.user_button)
#     # ��¼�ɹ��󣬵ȴ�����ɼ�
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
