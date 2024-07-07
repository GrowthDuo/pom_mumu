from time import sleep

import allure

def add_img(driver, step_name, need_sleep =True):
    '''
    截图并插入allure报告
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    '''
    if need_sleep:
       sleep(1)
    allure.attach(
        # 截图
        driver.get_screenshot_as_png(),
        # 截图名称
        step_name + '.png',
        # 截图类型
        allure.attachment_type.PNG)