import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep
from businessView.loginView import LoginView
from common.loadconf import ReadConfig

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp====')
        self.driver=appium_desired()
        logging.info('======test_login_zxw2018=====')
        l = LoginView(self.driver)
        user_info = ReadConfig().get_user()
        l.login_action(user_info["account"], user_info["password"])
        self.assertTrue(l.check_loginStatus())

    def tearDown(self):
        logging.info('====tearDown====')
        sleep(5)
        l=LoginView(self.driver)
        logging.info('====logout====')
        l.logout_action()
        self.driver.close_app()