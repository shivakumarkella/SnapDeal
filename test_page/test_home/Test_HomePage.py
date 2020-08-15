from pages.HomePage.homepage import HomePage
from test_page.testData import testDatafile as TD
import logging
from test_results.logger import customLogger

class TestHomePage(object):

    def __init__(self,driver):
        self.driver=driver
        self.obj_homePage=HomePage(driver=self.driver)
        self.obj_log=customLogger(logLevel=logging.DEBUG)

    def test_signIn(self):
        self.obj_homePage.signIn(homepage=TD.homePageURL,userName=TD.validUserName,password=TD.validPassword)
        self.obj_log.debug("login successfull")


    # def test_invalidpasssword(self):
    #     self.obj_homePage.signIn(homepage=TD.homePageURL,userName=TD.validUserName,password=TD.invalidPassword)
    #     result2=self.obj_homePage.verifyloginFailed()
    #     assert result2==True
    #     self.obj_log.info("invalid password")
    #
    #
    # def test_invalidusername(self):
    #     self.obj_homePage.signIn(homepage=TD.homePageURL,userName=TD.invalidUserName,password=TD.validPassword)
    #     result3=self.obj_homePage.verifyloginFailed()
    #     assert result3==True
    #     self.obj_log.info("invalid username")
    #
    # def test_invalidcredentials(self):
    #     self.obj_homePage.signIn(homepage=TD.homePageURL,userName=TD.invalidUserName,password=TD.invalidPassword)
    #     result4=self.obj_homePage.verifyloginFailed()
    #     assert result4==True
    #     self.obj_log.info("username and password invalid")

