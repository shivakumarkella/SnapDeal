
from utilities.selenium_actions import Se_actions
from pages import locatorsData as ld
import time

class GiftcardPage():
    # locators
    Locator=ld.giftcardpage
    gcp_gifticon_Locator=list(Locator['gifticon'].items())[0][1]
    gcp_gifticon_Locatortype = list(Locator['gifticon'].items())[0][0]
    gcp_digitalmini_Locator = list(Locator['digitalmini'].items())[0][1]
    gcp_digitalmini_Locatortype = list(Locator['digitalmini'].items())[0][0]
    gcp_slider_Locator = list(Locator['slider'].items())[0][1]
    gcp_slider_Locatortype = list(Locator['slider'].items())[0][0]
    gcp_left_Locator = list(Locator['leftSlide'].items())[0][1]
    gcp_left_Locatortype = list(Locator['leftSlide'].items())[0][0]
    gcp_discount_Locator = list(Locator['discount'].items())[0][1]
    gcp_discount_Locatortype = list(Locator['discount'].items())[0][0]
    gcp_discountViewMore_Locator = list(Locator['discount'].items())[0][1]
    gcp_discountViewMore_Locatortype = list(Locator['discount'].items())[0][0]
    def __init__(self,driver):
        self.obj_SA=Se_actions(driver=driver)

    def gotogiftpage(self):
        element=self.obj_SA.getElement(locator=self.gcp_gifticon_Locator,locatortype=self.gcp_gifticon_Locatortype)
        self.obj_SA.clickon(element=element)

    def digitalminimise(self):
        element=self.obj_SA.getElement(locator=self.gcp_digitalmini_Locator,locatortype=self.gcp_digitalmini_Locatortype)
        self.obj_SA.clickon(element=element)

    def PriceAdjustSlider(self):
        element=self.obj_SA.getElement(locator=self.gcp_slider_Locator,locatortype=self.gcp_slider_Locatortype)
        Leftelement = self.obj_SA.getElement(locator=self.gcp_left_Locator, locatortype=self.gcp_left_Locatortype)
        self.obj_SA.getslider(element=element,leftElement=Leftelement)

    def select00_10Discount(self):
        element=self.obj_SA.getElement(locator=self.gcp_discount_Locator,locatortype=self.gcp_discount_Locatortype)
        self.obj_SA.scrollElementIntoView(element)
        self.obj_SA.clickon(element)


    def giftcards(self):
        self.gotogiftpage()
        self.select00_10Discount()
        time.sleep(5)
        self.PriceAdjustSlider()




