#-*- coding:utf-8 -*-
import pytest
import businessView.dateView
from common.myunit_py import StartEnd
from common.delayedAssert import expect, assert_expectations
from businessView.loginView import LoginView
from businessView.dateView import DateView
import unittest
import logging,allure



@allure.title('创建任务')
class TestFixture(StartEnd):
    @allure.severity("critical")  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
    @allure.feature("测试模块_demo1")  # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
    @allure.story("测试模块_demo2")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    @allure.issue("BUG号：123")  # 问题表识，关联标识已有的问题，可为一个url链接地址
    @allure.testcase("用例名：测试字符串相等")  # 用例标识，关联标识用例，可为一个url链接地址
    def test_create_task(self):
        with allure.step("创建任务"):
            allure.attach("第一个步骤","pass")

        l = DateView(self.driver)
        title=l.get_timestamp()
        task=l.create_task(title)
        expect (task==title,"任务名称错误")
        l.delete_task()
        assert_expectations()






if __name__ == "__main__":
    # pytest.main(["-s", "test_login.py"])
    pytest.main(['-s',"test_create_tasks.py", '-q', '--alluredir', 'D:\\PycharmProjects\\appproject\\report\\xml'])