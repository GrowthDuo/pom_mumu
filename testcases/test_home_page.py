import time

import pytest
import allure
from page_object.UserLoginPage import UserLoginPage
from page_object.ProjectManagementPage import ProjectManagementPage
from config.config_driver import initialize_driver
from common.yaml_config import UserConfig
from util import util

class TestHomePage:
    def setup_class(cls):
        cls.driver = initialize_driver('chrome')
        cls.login_page = UserLoginPage(cls.driver)
        cls.project_page = ProjectManagementPage(cls.driver)

    def test_home_page(self):
        config = UserConfig()
        login_url = config.get_url()
        self.driver.get(login_url)
        self.logger = util.get_logger()
        self.logger.info('测试首页')

        username, password = config.get_credentials('will')

        with allure.step("第一步: 输入用户名"):
            self.login_page.input_username(username)
            self.logger.debug('输入用户名称: %s', username)

        with allure.step("第二步: 输入密码"):
            self.login_page.input_pwd(password)
            self.logger.debug('输入密码: %s', password)

        with allure.step("第三步: 点击登录"):
            self.login_page.login_click()
            self.logger.debug('点击登录')
            #
            self.login_page.wait_for_title()

        with allure.step("第四步: 点击项目管理"):
            self.project_page.click_pro()
            self.logger.debug('点击项目管理')
            time.sleep(3)
        # 点击项目管理
        with allure.step("第四步: 点击项目管理"):
            self.project_page.click_proguanli()
            self.logger.debug('点击项目管理')
            time.sleep(3)

        with allure.step("第五步: 输入项目名称"):
            time.sleep(3)
            project_name = "测试项目"
            self.project_page.input_project_name(project_name)
            self.logger.debug('输入项目名称: %s', project_name)

        with allure.step("第六步: 点击查询"):
            self.project_page.click_project()
            self.logger.debug('点击查询')

        with allure.step('第七步: 点击修改'):
            time.sleep(3)
            self.project_page.click_xiugai()
            self.logger.debug('点击修改')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
if __name__ == '__main__':
    pytest.main(['-v' ,'-s', 'test_home_page.py'])
import pytest
# from page_object.UserLoginPage import UserLoginPage
# from page_object.ProjectManagementPage import ProjectManagementPage
# from common.yaml_config import UserConfig
# from testcases.test_LoginPage01 import TestLoginPage
# from util import util
# class TestHomePage:
#     def test_home_page(self, driver):
#         login_page = UserLoginPage(driver)
#         project_page = ProjectManagementPage(driver)
#         config = UserConfig()
#
#         # 调用 TestLoginPage 的 test_login 方法
#         self.test_login(driver)
#
#         # 执行项目管理操作
#         project_page.click_pro()
#         project_name = "测试项目"
#         project_page.input_project_name(project_name)
#         project_page.click_project()