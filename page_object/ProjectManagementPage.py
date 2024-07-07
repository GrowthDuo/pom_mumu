from selenium.webdriver.common.by import By
from base.BasePage import BasePage

class ProjectManagementPage(BasePage):
    pro_xpath = (By.XPATH, '/html/body/div[1]/div/div[1]/ul/div/li[2]/div/i')
    input_pro_xpath = (By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div[1]/form/span/div[1]/div/div/input')
    an_xpath = (By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div[1]/form/span/div[3]/div/button/span')
    # 点击项目
    def click_pro(self):
        self.wait_for_element_visible(*self.pro_xpath)
        self.click(*self.pro_xpath)
    # 输入
    def input_project_name(self, name):
        self.wait_for_element_visible(*self.input_pro_xpath)
        self.input_text(name, *self.input_pro_xpath)
    # 点击查询
    def click_project(self):
        self.wait_for_element_visible(*self.an_xpath)
        self.click(*self.an_xpath)
