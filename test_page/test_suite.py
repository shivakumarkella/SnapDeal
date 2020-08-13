from test_results.logger import customLogger
import logging
import unittest
import pytest

from test_page.test_home.Test_HomePage import TestHomePage

@pytest.mark.usefixtures("oneTimeSetUp")
class test_snapDeal(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def thisClassConfig(self):
        self.obj_homePage=TestHomePage(driver=self.driver)
        self.log=customLogger(logLevel=logging.DEBUG)

    @pytest.mark.run(order=1)
    def tests_snapDeal(self):
        self.log.info('Browser opened ')
        self.log.info('Going To Home Page ')
        self.obj_homePage.test_signIn()
