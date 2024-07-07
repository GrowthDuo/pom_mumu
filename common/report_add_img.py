from time import sleep

import allure

def add_img(driver, step_name, need_sleep =True):
    '''
    ��ͼ������allure����
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    '''
    if need_sleep:
       sleep(1)
    allure.attach(
        # ��ͼ
        driver.get_screenshot_as_png(),
        # ��ͼ����
        step_name + '.png',
        # ��ͼ����
        allure.attachment_type.PNG)