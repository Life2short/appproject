#-*- coding:utf-8 -*-
from appium import webdriver
import yaml
import logging
import logging.config
import os
from common.loadconf import ReadConfig

# log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config\\log.conf')
# CON_LOG='D:/PycharmProjects/appproject/config/log.conf'
# CON_LOG=log_file_path.replace("\\","/")
# print(CON_LOG)
root_path = os.path.abspath(os.path.dirname(__file__)).split('appproject')[0]
log_file_path = os.path.join(root_path,'appproject','config\\log.conf')
logging.config.fileConfig(log_file_path)
logging=logging.getLogger()

def appium_desired():
    '''
    启动app
    '''

    desired_caps=ReadConfig().get_appconf()
    service_info=ReadConfig().get_service()

    logging.info('start app...')
    driver=webdriver.Remote('http://'+str(service_info ['ip'])+':'+str(service_info['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()

    # with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
    #     data = yaml.load(file)
    #
    # base_dir=os.path.dirname(os.path.dirname(__file__))
    # print(os.path.dirname(__file__))
    # print(base_dir)
    #
    # app_path=os.path.join(base_dir,'app',data['appname'])
    # print(app_path)
    # file_path=os.path.dirname(os.path.abspath(__file__))
    # log_file_path = os.path.join(file_path, 'config\\log.conf')
    # print (log_file_path)