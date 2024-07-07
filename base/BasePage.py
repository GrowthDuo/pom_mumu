# from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage(object):
#     def __init__(self, driver):
#         self.driver = driver
#
#     # 元素定位
#     def get_element(self, *loc):
#         try:
#             return self.driver.find_element(*loc)
#         except NoSuchElementException as e:
#             print(f"Element not found: {e}")
#             # 可以选择返回None，抛出自定义异常，或者记录错误并继续
#             return None
#
#     # 输入
#     def input_text(self, text, *loc):
#         try:
#             element = self.get_element(*loc)
#             element.send_keys(text)
#         except Exception as e:
#             print(f"Error while inputting text: {e}")
#
#     # 清空内容
#     def clear_input(self, *loc):
#         try:
#             element = self.get_element(*loc)
#             element.clear()
#         except Exception as e:
#             print(f"Error while clearing input: {e}")
#
#     # 点击
#     def click(self, *loc):
#         try:
#             element = self.get_element(*loc)
#             element.click()
#         except Exception as e:
#             print(f"Error while clicking: {e}")
#
#     # 标题
#     def get_title(self):
#         return self.driver.title
#
#     # 提示框
#     # 获取提示框文本
#     def get_alert_text(self):
#         try:
#             alert = self.driver.switch_to.alert
#             return alert.text
#         except NoAlertPresentException as e:
#             print(f"No alert is present: {e}")
#             # 可以选择返回None，抛出自定义异常，或者记录错误并继续
#             return None
#
#     def wait_for_element_visible(self, *loc):
#         # 等待元素可见
#         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
#
#     def wait_for_element_clickable(self, *loc):
#         # 等待元素可点击
#         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
#
#     # 等待元素不可见
#     def wait_for_element_invisible(self, *loc):
#         # 等待元素不可见
#         WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc))
#
#     # 等待页面元素都加载完成
#     def wait_for_page_load(self):
#         # 等待页面元素都加载完成
#         WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located)
#
#     # 等待页面元素都加载完成,直到某个元素可见
#     def wait_for_page_load2(self, *loc):
#         # 等待页面元素都加载完成,直到某个元素可见
#         WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located)
#     # 跳转地址后等待元素消失
#     def wait_for_element_gone(self, *loc):
#         # 等待元素消失
#         WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(loc))
#
#     # 句柄切换，窗口到最新的窗口
#     def switch_to_newest_window(self):
#         # 句柄切换，窗口到最新的窗口
#         handles = self.driver.window_handles
#         if len(handles) > 1:
#             for handle in handles:
#                 self.driver.switch_to.window(handle)
#                 break

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待网页上的某个元素变得可见。
    def wait_for_element_visible(self, by, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))
    # 等待网页上的某个元素变得不可见。
    def wait_for_element_clickable(self, by, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    # 用于点击元素
    def click(self, by, locator):
        self.driver.find_element(by, locator).click()
    # 用于输入值
    def input_text(self, text, by, locator):
        self.driver.find_element(by, locator).send_keys(text)
    # 用于清空输入框中的内容。
    def clear_input(self, by, locator):
        self.driver.find_element(by, locator).clear()
    # 用于捕获当前网页的截图并保存到一个指定的路径。
    def get_screenshot(self, name='screenshot'):
        path = f'screenshots/{name}.png'
        self.driver.save_screenshot(path)
        return path
