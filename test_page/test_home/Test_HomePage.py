from pages.HomePage.homepage import HomePage
from test_page.testData import testDatafile as TD

class TestHomePage(object):

    def __init__(self,driver):
        self.driver=driver
        self.obj_homePage=HomePage(driver=self.driver)

    def test_signIn(self):
        self.obj_homePage.signIn(homepage=TD.homePageURL,userName=TD.validUserName,password=TD.validPassword)