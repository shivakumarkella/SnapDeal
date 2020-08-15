from test_results.logger import customLogger
import logging
import unittest
import pytest

from test_page.test_home.Test_HomePage import TestHomePage
from test_page.tests_giftCard.test_giftcard import TestsGiftcard

@pytest.mark.usefixtures("oneTimeSetUp")
class test_snapDeal(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def thisClassConfig(self):
        self.log = customLogger(logLevel=logging.DEBUG)
        self.obj_homePage=TestHomePage(driver=self.driver)
        self.obj_GiftCard=TestsGiftcard(driver=self.driver)


    @pytest.mark.run(order=1)
    def tests_snapDeal(self):
        self.log.info('Browser opened ')
        self.log.info('Going To Home Page ')
        self.obj_homePage.test_signIn()
        self.obj_GiftCard.test_ValidGiftCard()

