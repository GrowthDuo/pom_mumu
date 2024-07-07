import pytest
import allure
from page_object.UserLoginPage import UserLoginPage
from page_object.ProjectManagementPage import ProjectManagementPage
from config.config_driver import initialize_driver
from common.yaml_config import UserConfig
from util import util

class TestHomePage:
    @classmethod
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

        with allure.step("第五步: 输入项目名称"):
            project_name = "测试项目"
            self.project_page.input_project_name(project_name)
            self.logger.debug('输入项目名称: %s', project_name)

        with allure.step("第六步: 点击查询"):
            self.project_page.click_project()
            self.logger.debug('点击查询')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
if __name__ == '__main__':
    pytest.main(['-s', 'test_home_page.py'])