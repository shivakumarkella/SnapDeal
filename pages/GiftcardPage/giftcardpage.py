
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
    gcp_customerratng_Locator = list(Locator['customerratng'].items())[0][1]
    gcp_customerratng_Locatortype = list(Locator['customerratng'].items())[0][0]
    gcp_product_Locator = list(Locator['product'].items())[0][1]
    gcp_product_Locatortype = list(Locator['product'].items())[0][0]
    gcp_buynow_Locator = list(Locator['buynow'].items())[0][1]
    gcp_buynow_Locatortype = list(Locator['buynow'].items())[0][0]
    gcp_recipientName_Locator = list(Locator['recipientName'].items())[0][1]
    gcp_recipientName_Locatortype = list(Locator['recipientName'].items())[0][0]
    gcp_recipientEmail_Locator = list(Locator['recipientEmail'].items())[0][1]
    gcp_recipientEmail_Locatortype = list(Locator['recipientEmail'].items())[0][0]
    gcp_Message_Locator = list(Locator['message'].items())[0][1]
    gcp_Message_Locatortype = list(Locator['message'].items())[0][0]
    gcp_fullname_Locator = list(Locator['fullname'].items())[0][1]
    gcp_fullname_Locatortype = list(Locator['fullname'].items())[0][0]
    gcp_mobile_Locator = list(Locator['mobile'].items())[0][1]
    gcp_mobile_Locatortype = list(Locator['mobile'].items())[0][0]
    gcp_clickbutton_Locator = list(Locator['clickbutton'].items())[0][1]
    gcp_clickbutton_Locatortype = list(Locator['clickbutton'].items())[0][0]
    gcp_payment_Locator = list(Locator['payment'].items())[0][1]
    gcp_payment_Locatortype = list(Locator['payment'].items())[0][0]
    gcp_cashondeliver_Locator = list(Locator['cashondeliver'].items())[0][1]
    gcp_cashondeliver_Locatortype = list(Locator['cashondeliver'].items())[0][0]

    def __init__(self,driver):
        self.obj_SA=Se_actions(driver=driver)

    def gotogiftpage(self):
        element=self.obj_SA.getElement(locator=self.gcp_gifticon_Locator,locatortype=self.gcp_gifticon_Locatortype)
        # self.obj_SA.explicitwait(locator=self.gcp_gifticon_Locator,locatortype=self.gcp_gifticon_Locatortype)
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

    def customerrate(self):
        element=self.obj_SA.getElement(locator=self.gcp_customerratng_Locator,locatortype=self.gcp_customerratng_Locatortype)
        self.obj_SA.scrollElementIntoView(element)
        self.obj_SA.clickon(element)


    def product(self):
        element=self.obj_SA.getElement(locator=self.gcp_product_Locator,locatortype=self.gcp_product_Locatortype)
        self.obj_SA.scrollElementIntoView(element)
        self.obj_SA.clickon(element)

    def switchwindow(self):
        self.obj_SA.switchtowindow()

    def scroll(self):
        self.obj_SA.scrolldown()

    def buynow(self):
        element=self.obj_SA.getElement(locator=self.gcp_buynow_Locator,locatortype=self.gcp_buynow_Locatortype)
        self.obj_SA.clickon(element)

    def recipientname(self,recipientName):
        element = self.obj_SA.getElement(locator=self.gcp_recipientName_Locator,
                                         locatortype=self.gcp_recipientName_Locatortype)
        self.obj_SA.SendKeys(element,message=recipientName)

    def recipientmail(self,recipientEmail):
        element = self.obj_SA.getElement(locator=self.gcp_recipientEmail_Locator,
                                         locatortype=self.gcp_recipientEmail_Locatortype)
        self.obj_SA.SendKeys(element, message=recipientEmail)

    def message(self,messgae):
        element = self.obj_SA.getElement(locator=self.gcp_Message_Locator, locatortype=self.gcp_Message_Locatortype)
        self.obj_SA.SendKeys(element, message=messgae)

    def fullname(self,fullname):
        element = self.obj_SA.getElement(locator=self.gcp_fullname_Locator, locatortype=self.gcp_fullname_Locatortype)
        self.obj_SA.SendKeys(element, message=fullname)

    def clickbutton(self):
        button = self.obj_SA.getElement(locator=self.gcp_clickbutton_Locator,
                                        locatortype=self.gcp_clickbutton_Locatortype)
        self.obj_SA.clickon(button)

    def payment(self):
        payment = self.obj_SA.getElement(locator=self.gcp_payment_Locator, locatortype=self.gcp_payment_Locatortype)
        self.obj_SA.clickon(payment)

    def mobilenum(self,mobile):
        element = self.obj_SA.getElement(locator=self.gcp_mobile_Locator, locatortype=self.gcp_mobile_Locatortype)
        self.obj_SA.SendKeys(element,message=mobile)

    def cashondelivery(self):
        element=self.obj_SA.getElement(locator=self.gcp_cashondeliver_Locator,locatortype=self.gcp_cashondeliver_Locatortype)
        self.obj_SA.clickon(element)








    def giftcards(self,rName,rEmail,msge,fulnam):
        self.gotogiftpage()
        self.select00_10Discount()
        time.sleep(5)
        self.PriceAdjustSlider()
        time.sleep(5)
        self.customerrate()
        time.sleep(5)
        self.product()
        time.sleep(3)
        self.switchwindow()
        self.scroll()
        self.buynow()
        self.recipientname(recipientName=rName)
        self.recipientmail(recipientEmail=rEmail)
        self.message(messgae=msge)
        self.fullname(fullname=fulnam)
        time.sleep(3)
        self.clickbutton()
        self.payment()
        self.cashondelivery()




