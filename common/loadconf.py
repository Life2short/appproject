#-*- coding:utf-8 -*-

import yaml
import os

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filename=None):
        if filename:
            configpath = "../config/"+ filename
        else:
            configpath ="../config/kyb_caps.yaml"
        with open(configpath, 'r', encoding='utf-8') as file:
            self.data = yaml.load(file, Loader=yaml.FullLoader)

        with open("./android.yaml", "a") as file:
            yaml.dump(self.data, file, default_flow_style=False, encoding='utf-8', allow_unicode=True)



    def get_appconf(self):
        '''
        获取app配置
        :return:
        '''
        desired_caps = {}
        desired_caps['platformName'] = self.data['platformName']
        desired_caps['platformVersion'] = self.data['platformVersion']
        desired_caps['deviceName'] = self.data['deviceName']

        base_dir = os.path.dirname(os.path.dirname(__file__))
        app_path = os.path.join(base_dir, 'app', self.data['appname'])
        desired_caps['app'] = app_path

        desired_caps['appPackage'] = self.data['appPackage']
        desired_caps['appActivity'] = self.data['appActivity']
        desired_caps['noReset'] = self.data['noReset']

        desired_caps['unicodeKeyboard'] = self.data['unicodeKeyboard']
        desired_caps['resetKeyboard'] = self.data['resetKeyboard']

        return desired_caps

    def get_service(self):
        service_info={}
        service_info['ip']=self.data['ip']
        service_info['port'] = self.data['port']

        return service_info

    def get_user(self):
        user_info={}
        user_info["account"]=self.data['USER_ACCOUNT']
        user_info["password"] = self.data['USER_PASSWORD']
        return user_info