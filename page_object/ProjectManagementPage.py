from selenium.webdriver.common.by import By
from base.BasePage import BasePage

class ProjectManagementPage(BasePage):
    # �����Ŀ
    pro_xpath = (By.XPATH, '/html/body/div[1]/div/div[1]/ul/div/li[2]/div/i')
    # �����Ŀ����
    proguanli =(By.XPATH, '/html/body/div[1]/div/div[1]/ul/div/li[2]/ul/div/a/li')
    # ����
    input_pro_xpath = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/form/span/div[1]/div/div/input')
    # �����ѯ
    an_xpath = (By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div[1]/form/span/div[3]/div/button/span')
    # ����޸İ�ť
    xiugai = (By.XPATH, '/html/body/div/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]')


    # �����Ŀ
    def click_pro(self):
        self.wait_for_element_visible(*self.pro_xpath)
        self.click(*self.pro_xpath)
    # �����Ŀ����
    def click_proguanli(self):
        self.wait_for_element_visible(*self.proguanli)
        self.click(*self.proguanli)
    # ����
    def input_project_name(self, name):
        self.wait_for_element_visible(*self.input_pro_xpath)
        self.input_text(name, *self.input_pro_xpath)
    # �����ѯ
    def click_project(self):
        self.wait_for_element_visible(*self.an_xpath)
        self.click(*self.an_xpath)

    # ������޸ġ���ť
    def click_xiugai(self):
        self.wait_for_element_visible(*self.xiugai)
        self.click(*self.xiugai)
