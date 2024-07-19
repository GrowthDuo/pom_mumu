from selenium.webdriver.common.by import By
from base.BasePage import BasePage

class ProjectManagementPage(BasePage):
    # 点击项目
    pro_xpath = (By.XPATH, '/html/body/div[1]/div/div[1]/ul/div/li[2]/div/i')
    # 点击项目管理
    proguanli =(By.XPATH, '/html/body/div[1]/div/div[1]/ul/div/li[2]/ul/div/a/li')
    # 输入
    input_pro_xpath = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/form/span/div[1]/div/div/input')
    # 点击查询
    an_xpath = (By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div[1]/form/span/div[3]/div/button/span')
    # 点击修改按钮
    xiugai = (By.XPATH, '/html/body/div/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]')


    # 点击项目
    def click_pro(self):
        self.wait_for_element_visible(*self.pro_xpath)
        self.click(*self.pro_xpath)
    # 点击项目管理
    def click_proguanli(self):
        self.wait_for_element_visible(*self.proguanli)
        self.click(*self.proguanli)
    # 输入
    def input_project_name(self, name):
        self.wait_for_element_visible(*self.input_pro_xpath)
        self.input_text(name, *self.input_pro_xpath)
    # 点击查询
    def click_project(self):
        self.wait_for_element_visible(*self.an_xpath)
        self.click(*self.an_xpath)

    # 点击“修改”按钮
    def click_xiugai(self):
        self.wait_for_element_visible(*self.xiugai)
        self.click(*self.xiugai)
