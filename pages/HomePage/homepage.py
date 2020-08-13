from utilities.selenium_actions import Se_actions
from pages import locatorsData as ld

class HomePage(object):

    # locators
    Locator = ld.homepage
    hp_userIcon_Locator = list(Locator['userIcon'].items())[0][1]
    hp_userIcon_LocatorType = list(Locator['userIcon'].items())[0][0]
    hp_login_Locator = list(Locator['login'].items())[0][1]
    hp_login_LocatorType = list(Locator['login'].items())[0][0]
    hp_username_Locator = list(Locator['UserName'].items())[0][1]
    hp_username_LocatorType = list(Locator['UserName'].items())[0][0]
    hp_loginIFrmae_Locator = list(Locator['loginIFrmae'].items())[0][1]
    hp_loginIFrmae_LocatorType = list(Locator['loginIFrmae'].items())[0][0]
    hp_countinue_Locator=list(Locator['countinue'].items())[0][1]
    hp_countinue_LocatorType=list(Locator['countinue'].items())[0][0]
    hp_password_Locator=list(Locator['password'].items())[0][1]
    hp_password_Locatortype=list(Locator['password'].items())[0][0]
    hp_submittlogin_Locator=list(Locator['submitlogin'].items())[0][1]
    hp_submittlogin_Locatortype=list(Locator['submitlogin'].items())[0][0]

    def __init__(self,driver):
        self.driver=driver
        self.obj_Selenium=Se_actions(driver=self.driver)

    def goToHomePage(self,homepageUrl):
        self.obj_Selenium.getUrl(url=homepageUrl)

    def clickOnUserIcon(self):
        element=self.obj_Selenium.getElement(locator=self.hp_userIcon_Locator,locatortype=self.hp_userIcon_LocatorType)
        self.obj_Selenium.mouseHoverToElement(element=element)

    def clicklogin(self):
        element=self.obj_Selenium.getElement(locator=self.hp_login_Locator,locatortype=self.hp_login_LocatorType)
        self.obj_Selenium.clickon(element=element)

    def goToiframe(self):
        self.obj_Selenium.switchToiframe(switchToFrame=self.hp_loginIFrmae_Locator)


    def enterUserName(self,email):
        userNameElement=self.obj_Selenium.getElement(locator=self.hp_username_Locator,locatortype=self.hp_username_LocatorType)
        self.obj_Selenium.SendKeys(element=userNameElement,message=email)

    def clickcontinue(self):
        clickcountinue=self.obj_Selenium.getElement(locator=self.hp_countinue_Locator,locatortype=self.hp_countinue_LocatorType)
        self.obj_Selenium.clickon(element=clickcountinue)

    def enterpassword(self,password):
        password1=self.obj_Selenium.getElement(locator=self.hp_password_Locator,locatortype=self.hp_password_Locatortype)
        self.obj_Selenium.SendKeys(element=password1,message=password)

    def submitlogin(self):
        submitbutton=self.obj_Selenium.getElement(locator=self.hp_submittlogin_Locator,locatortype=self.hp_submittlogin_Locatortype)
        self.obj_Selenium.clickon(element=submitbutton)

    def signIn(self,homepage,userName,password):
        self.goToHomePage(homepageUrl=homepage)
        self.clickOnUserIcon()
        self.clicklogin()
        self.goToiframe()
        self.enterUserName(email=userName)
        self.clickcontinue()
        self.enterpassword(password=password)
        self.submitlogin()
