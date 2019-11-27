#-*- coding:utf-8 -*-
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import os,time
import allure

class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def wait_element(self,loc):
        try:
            logging.info("find_element：%s" % str(loc))
            elem = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(loc))
            return elem
        except TimeoutException as timee:
            logging.info("find_element：%s" % str(loc) + "超时")
            raise timee
        except Exception as e:
            logging.info("未寻找到元素find_element：%s" % str(loc))
            raise e

    def inputText(self, loc, text):
        # return self.findView(way, value).send_keys(text)
        try:
            elem=self.wait_element(loc)
            elem.clear()
            elem.send_keys(text)
            logging.info( "输入：" + text)
        except Exception as e:
            logging.info("输入失败：" + text)
            raise e

    def click(self,loc):
        # return self.findView(way,value).click()
        try:
            element = self.wait_element(loc)
            element.click()
            logging.info("点击成功")
        except Exception as e:
            logging.info("点击失败")
            raise e


    def gettxt(self,loc):
        return self.wait_element(loc).text

    def find_element(self,*loc):
        logging.info("find_element：%s"%str(*loc))
        return self.driver.find_elements(*loc)

    def find_elements(self,*loc):
        logging.info("find_elements：%s"%str(*loc))
        return self.driver.find_elements(*loc)

    def get_timestamp(self):
        return str(int(time.time()))


    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,direction):
        screen_width = self.get_window_size()['width']
        screen_height = self.get_window_size()['height']
        if(direction == 'down'):
            TouchAction(self.driver).press(x=screen_width/2,y=screen_height/4).move_to(x=screen_width/2,y=screen_height*3/4).release().perform()
        elif (direction == 'up'):
            TouchAction(self.driver).press(x=screen_width/2,y=screen_height*3/4).move_to(x=screen_width/2,y=screen_height/4).release().perform()
        elif(direction == 'left'):
            TouchAction(self.driver).press(x=screen_width*5/6,y=screen_height/2).move_to(x=screen_width/6,y=screen_height/2).release().perform()
        elif(direction == 'right'):
            TouchAction(self.driver).press(x=screen_width/6,y=screen_height/2).move_to(x=screen_width*5/6,y=screen_height/2).release().perform()
        else:
            raise RuntimeError("无效的方向")

    def assertDtEquals(self,actual,expect):
        '''
          断言实际值等于期望值
        '''

        try:
            # actual = self.wait_element(way, value).text
            assert (actual == expect)
        # except TimeoutException as timee:
        #     logging.info("断言相等失败，通过" + way + "方式定位元素：" + value + "超时")
        #     raise timee
        except Exception as e:
            logging.info("断言相等失败，实际值：" + actual + "；" + "期望值：" + expect)
            raise e

    def saveScreenshotPNG(self,module):
        now_time=time.strftime("%Y-%m-%d %H_%M_%S")
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,now_time)
        # screen =self.driver.save_screenshot(pic_dir_path+"/"+date+".png")
        self.driver.get_screenshot_as_file(image_file)
        with allure.step('screenshots'):
            allure.attach.file(image_file, attachment_type=allure.attachment_type.PNG)


    def run_adb_cmd(self,cmd):
        '''
        执行adb命令
        :return:
        '''
        try:
            result=os.popen(cmd)
            res=result.readlines()
        except Exception as err:
            raise RuntimeError("执行失败：%s"%err)
        else:
            if "error" in res:
                raise RuntimeError(res)
            return res

    def run_shell_cmd(self,cmd):
        '''
        执行shell命令
        :param cmd:
        :return:
        '''

        res=self.run_adb_cmd("adb shell '%s'"%cmd)
        return res

    def push_file(self,pc_path,mo_path):
        '''
        导入文件
        :param pc_path:电脑文件路径
        :param mo_path: 手机路径
        :return:
        '''
        res = self.run_adb_cmd("adb push %s %s"%(pc_path,mo_path))
        return res

if __name__=="__main__":
    pass