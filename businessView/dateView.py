#-*- coding:utf-8 -*-
import logging
from common.common_fun import Common,NoSuchElementException,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import time
import allure

class DateView(Common):
    recite_words=(By.ID,'com.tal.kaoyan:id/home_fix_item_contentlayout')#背单词
    calendarBtn=(By.ID,'com.tal.kaoyan:id/mainactivity_button_calendar')#日历
    word_txt=(By.ID,'com.tal.kaoyan:id/englishword_book_item_name')
    tasks_list=(By.ID,"com.tal.kaoyan:id/home_task_title")#任务列表


    #添加任务页面
    add_tasks=(By.ID,"com.tal.kaoyan:id/task_no_task") #添加任务
    task_title=(By.ID,"com.tal.kaoyan:id/activity_date_addtask_tasktitle")#任务标题
    confirm_time=(By.ID,"com.tal.kaoyan:id/activity_date_addtask_selectdate_commitbtn")#确定选择时间
    confirm_add_tasks=(By.ID, "com.tal.kaoyan:id/myapptitle_RightButton_textview")#确定添加任务

    #任务详情页面
    delete_task_butn=(By.ID, "com.tal.kaoyan:id/ivDelete")#删除
    delete_all_task=(By.ID,"com.tal.kaoyan:id/btnDeleteAllTask")#删除所有任务
    delete_qr=(By.ID,"android:id/button1")

    # loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')





    # def click_action(self):
    #     logging.info('============login_action==============')
    #     logging.info('click calendarBtn')
    #     self.wait_element(self.calendarBtn).click()
    #
    #     logging.info('click sent_backkey')
    #     self.sent_backkey()
    #
    #     logging.info('click recite_words')
    #     time.sleep(2)
    #     self.wait_element(self.recite_words).click()
    #
    # def check_res(self):
    #     try :
    #         self.wait_element(self.word_txt)
    #     except TimeoutException:
    #         logging.error('Fail!')
    #         self.getScreenShot('fail')
    #         return False
    #     else:
    #         logging.info('success!')
    #         self.click_back()
    #         return True
    @allure.step("创建任务")
    def create_task(self,title):
        logging.info('============create_task==============')
        self.wait_element(self.calendarBtn).click()
        self.click(self.add_tasks)
        self.inputText(self.task_title,title)
        self.click(self.confirm_add_tasks)

        try:
            restitle=self.gettxt(self.tasks_list)
            return restitle
        except TimeoutException:
            logging.error('Fail!')
            self.getScreenShot('fail')
            return RuntimeError("获取任务元素超时")

    @allure.step("删除任务")
    def delete_task(self):
        try:
            restitle=self.gettxt(self.tasks_list)
            logging.info("任务名称：%s"%str(restitle))
        except TimeoutException:
            logging.error('无任务')
        else:
            logging.info('存在任务，并进行删除')
            self.click(self.tasks_list)
            self.click(self.delete_task_butn)
            self.click(self.delete_qr)
