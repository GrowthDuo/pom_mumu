import yaml
import os

# 假设YAML配置文件与当前脚本位于同一目录下，且文件名为environment.yaml
yaml_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'environment.yaml')

class UserConfig:
    def __init__(self, file_path=yaml_file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.config = yaml.safe_load(file)
            self.users = self.config.get('users', {})  # 假设users是存储用户信息的键
            self.url = self.config.get('url', '')  # 假设url是存储登录URL的键

    def get_user(self, username):
        return self.users.get(username, None)

    def get_credentials(self, username):
        user_info = self.get_user(username)
        if user_info:
            # 简化了获取密码的逻辑，直接尝试获取'password'键，如果不存在则返回空字符串
            return user_info['username'], user_info.get('password', '')
        return None, None

    def get_url(self):
        # 返回配置文件中指定的URL
        return self.url