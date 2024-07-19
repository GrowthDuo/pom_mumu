import time
import allure
from page_object.UserLoginPage import UserLoginPage
from config.config_driver import initialize_driver
from common.yaml_config import UserConfig  # 假设你将上面的类保存在config/user_config.py中
from util import util
# 使用pytest类启动
# @pytest.mark.parametrize('username, password', [('will', '<PASSWORD>'), ('tom', '123456')])
class TestLoginPage():
    @classmethod
    def setup_class(cls):
        """
        测试用例执行前执行
        :return:
        """
        # 初始化浏览器驱动
        cls.driver = initialize_driver('chrome')
        # 实例化页面对象
        cls.login_page = UserLoginPage(cls.driver)
    def test_login(self):
        # driver = initialize_driver('chrome')  # 假设使用Chrome浏览器
        # # 实例化页面对象
        # login_page = UserLoginPage(driver)

        # 加载用户配置
        config = UserConfig()  # 单一实例
        login_url = config.get_url()
        self.driver.get(login_url)
        # 获取日志对象
        logger = util.get_logger()
        logger.info('测试用户登录')

        # 获取用户名和密码
        username, password = config.get_credentials('will')

        # 输入用户名和密码
        with allure.step("第一步: 输入用户名"):

            self.login_page.input_username(username)
            logger.debug('输入用户名称: %s', username)

        with allure.step("第二步: 输入密码"):
            self.login_page.input_pwd(password)
            logger.debug('输入密码: %s', password)

            # 在打开网页前截屏
            before_screenshot = self.driver.get_screenshot_as_png()
            allure.attach(before_screenshot, name='登录网页', attachment_type=allure.attachment_type.PNG)

        with allure.step("第三步: 点击登录"):
            self.login_page.login_click()
            logger.debug('点击登录')
            print(self.driver.title)
            time.sleep(3)
            # # 等待页面加载完成，这里以等待某个特定元素出现为例
            # login_page.wait_for_title()
            # 登录后截屏
            after_screenshot = self.driver.get_screenshot_as_png()
            allure.attach(after_screenshot, name='登录成功后进入首页', attachment_type=allure.attachment_type.PNG)

        # 这里可以添加断言来验证登录是否成功
        with allure.step("登录"):
            try:
                assert 'AutoMeter' == self.driver.title
            except AssertionError:
                allure.attach(after_screenshot, name='登录失败', attachment_type=allure.attachment_type.PNG)
                logger.error("注意，注意,  %s", "报错了", exc_info=1)
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
# #
# import time
# import pytest
# import allure
# from page_object.UserLoginPage import UserLoginPage
# from config.config_driver import initialize_driver
# from common.yaml_config import UserConfig  # 假设你将上面的类保存在config/user_config.py中
# from util import util
#
# class TestLoginPage:
#     @classmethod
#     def setup_class(cls):
#         cls.driver = initialize_driver('chrome')
#         cls.login_page = UserLoginPage(cls.driver)
#
#     def test_login(self):
#         config = UserConfig()  # 单一实例
#         login_url = config.get_url()
#         self.driver.get(login_url)
#         logger = util.get_logger()
#         logger.info('测试用户登录')
#         before_screenshot = self.driver.get_screenshot_as_png()
#         allure.attach(before_screenshot, name='登录网页', attachment_type=allure.attachment_type.PNG)
#         # 获取用户名和密码
#         username, password = config.get_credentials('will')
#         print(f"Username: {username}, Password: {password}")
#
#         # 在打开网页前截屏
#
#         with allure.step("第一步: 输入用户名"):
#             self.login_page.input_username(username)
#             logger.debug('输入用户名称: %s', username)
#
#         with allure.step("第二步: 输入密码"):
#             self.login_page.input_pwd(password)
#             logger.debug('输入密码: %s', password)
#
#         with allure.step("第三步: 点击登录"):
#             self.login_page.login_click()
#             logger.debug('点击登录')
#             time.sleep(3)
#
#         with allure.step("登录"):
#             try:
#                 assert 'AutoMeter' == self.driver.title
#                 # 登录后截屏
#                 after_screenshot = self.driver.get_screenshot_as_png()
#                 allure.attach(after_screenshot, name='登录成功后进入首页', attachment_type=allure.attachment_type.PNG)
#             except AssertionError:
#                 logger.error("注意，注意,  %s", "报错了", exc_info=1)
#                 allure.attach(after_screenshot, name='登录失败', attachment_type=allure.attachment_type.PNG)
#
#
#     @classmethod
#     def teardown_class(cls):
#         cls.driver.quit()
# if  __name__ == '__main__':
#     pytest.main(['-s', 'test_LoginPage01.py'])
# test_login.py
import pytest
from page_object.UserLoginPage import UserLoginPage
from page_object.ProjectManagementPage import ProjectManagementPage
from common.yaml_config import UserConfig
from util import util

# class TestLoginPage:
#     def test_login(self, driver):
#         login_page = UserLoginPage(driver)
#         config = UserConfig()
#         login_url = config.get_url()
#         driver.get(login_url)
#
#         # 执行登录操作
#         username, password = config.get_credentials('will')
#         login_page.input_username(username)
#         login_page.input_pwd(password)
#         login_page.login_click()
#         login_page.wait_for_title()
#
#         # 添加断言
#         assert 'AutoMeter' == driver.title