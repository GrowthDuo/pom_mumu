from selenium import webdriver

def initialize_driver(browser_type):
    if browser_type == 'chrome':
        driver = webdriver.Chrome()
    elif browser_type == 'firefox':
        driver = webdriver.Firefox()
    # 可以添加更多浏览器类型的支持
    else:
        raise ValueError("Unsupported browser type")
    return driver

class DriverConfig:
    def driver_config(self):
        options = webdriver.ChromeOptions()
        # 设置全屏
        options.add_argument('start-maximized')
        # 添加无头模式
        options.add_argument('headless')
        # 设置无痕
        options.add_argument('incognito')
        # 解决卡顿
        options.add_argument('disable-gpu')
        options.add_argument("--no-sandbox")
        # 去除 chrome 正受自动化测试软件的控制提示
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 解决 无法访问https问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略 本机 TLS/SSL错误
        options.add_argument('--allow-insecure-localhost')

        # 添加代理
        # options.add_argument('--proxy-server=http://127.0.0.1:8080')
        driver = webdriver.Chrome(chrome_options=options)
        # 删除cookins
        driver.delete_all_cookies()
        return driver



