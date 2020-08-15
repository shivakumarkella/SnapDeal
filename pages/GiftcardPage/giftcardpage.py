
from utilities.selenium_actions import Se_actions
from pages import locatorsData as ld

class GiftcardPage():
    # locators
    Locator=ld.giftcardpage
    gcp_gifticon_Locator=list(Locator['gifticon'].items())[0][1]
    gcp_gifticon_Locatortype = list(Locator['gifticon'].items())[0][0]
    gcp_digitalmini_Locator = list(Locator['digitalmini'].items())[0][1]
    gcp_digitalmini_Locatortype = list(Locator['digitalmini'].items())[0][0]
    gcp_slider_Locator = list(Locator['slider'].items())[0][1]
    gcp_slider_Locatortype = list(Locator['slider'].items())[0][0]

    def __init__(self,driver):
        self.obj_SA=Se_actions(driver=driver)

    def gotogiftpage(self):
        element=self.obj_SA.getElement(locator=self.gcp_gifticon_Locator,locatortype=self.gcp_gifticon_Locatortype)
        self.obj_SA.clickon(element=element)

    def digitalminimise(self):
        element=self.obj_SA.getElement(locator=self.gcp_digitalmini_Locator,locatortype=self.gcp_digitalmini_Locatortype)
        self.obj_SA.clickon(element=element)

    def slider(self):
        element=self.obj_SA.getElement(locator=self.gcp_slider_Locator,locatortype=self.gcp_slider_Locatortype)
        self.obj_SA.getslider(element=element)

    def giftcards(self):
        self.gotogiftpage()
        self.slider()
        self.digitalminimise()
