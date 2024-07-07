# from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage(object):
#     def __init__(self, driver):
#         self.driver = driver
#
#     # Ԫ�ض�λ
#     def get_element(self, *loc):
#         try:
#             return self.driver.find_element(*loc)
#         except NoSuchElementException as e:
#             print(f"Element not found: {e}")
#             # ����ѡ�񷵻�None���׳��Զ����쳣�����߼�¼���󲢼���
#             return None
#
#     # ����
#     def input_text(self, text, *loc):
#         try:
#             element = self.get_element(*loc)
#             element.send_keys(text)
#         except Exception as e:
#             print(f"Error while inputting text: {e}")
#
#     # �������
#     def clear_input(self, *loc):
#         try:
#             element = self.get_element(*loc)
#             element.clear()
#         except Exception as e:
#             print(f"Error while clearing input: {e}")
#
#     # ���
#     def click(self, *loc):
#         try:
#             element = self.get_element(*loc)
#             element.click()
#         except Exception as e:
#             print(f"Error while clicking: {e}")
#
#     # ����
#     def get_title(self):
#         return self.driver.title
#
#     # ��ʾ��
#     # ��ȡ��ʾ���ı�
#     def get_alert_text(self):
#         try:
#             alert = self.driver.switch_to.alert
#             return alert.text
#         except NoAlertPresentException as e:
#             print(f"No alert is present: {e}")
#             # ����ѡ�񷵻�None���׳��Զ����쳣�����߼�¼���󲢼���
#             return None
#
#     def wait_for_element_visible(self, *loc):
#         # �ȴ�Ԫ�ؿɼ�
#         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
#
#     def wait_for_element_clickable(self, *loc):
#         # �ȴ�Ԫ�ؿɵ��
#         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
#
#     # �ȴ�Ԫ�ز��ɼ�
#     def wait_for_element_invisible(self, *loc):
#         # �ȴ�Ԫ�ز��ɼ�
#         WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc))
#
#     # �ȴ�ҳ��Ԫ�ض��������
#     def wait_for_page_load(self):
#         # �ȴ�ҳ��Ԫ�ض��������
#         WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located)
#
#     # �ȴ�ҳ��Ԫ�ض��������,ֱ��ĳ��Ԫ�ؿɼ�
#     def wait_for_page_load2(self, *loc):
#         # �ȴ�ҳ��Ԫ�ض��������,ֱ��ĳ��Ԫ�ؿɼ�
#         WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located)
#     # ��ת��ַ��ȴ�Ԫ����ʧ
#     def wait_for_element_gone(self, *loc):
#         # �ȴ�Ԫ����ʧ
#         WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(loc))
#
#     # ����л������ڵ����µĴ���
#     def switch_to_newest_window(self):
#         # ����л������ڵ����µĴ���
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

    # �ȴ���ҳ�ϵ�ĳ��Ԫ�ر�ÿɼ���
    def wait_for_element_visible(self, by, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))
    # �ȴ���ҳ�ϵ�ĳ��Ԫ�ر�ò��ɼ���
    def wait_for_element_clickable(self, by, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    # ���ڵ��Ԫ��
    def click(self, by, locator):
        self.driver.find_element(by, locator).click()
    # ��������ֵ
    def input_text(self, text, by, locator):
        self.driver.find_element(by, locator).send_keys(text)
    # �������������е����ݡ�
    def clear_input(self, by, locator):
        self.driver.find_element(by, locator).clear()
    # ���ڲ���ǰ��ҳ�Ľ�ͼ�����浽һ��ָ����·����
    def get_screenshot(self, name='screenshot'):
        path = f'screenshots/{name}.png'
        self.driver.save_screenshot(path)
        return path
