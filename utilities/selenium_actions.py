
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from test_results.logger import customLogger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import time
from test_page.testData import testDatafile as TD

class Se_actions():

    def __init__(self,driver):
        self.driver=driver
        self.log=customLogger(logLevel=logging.DEBUG)
        self.actions = ActionChains(driver=self.driver)

    def getUrl(self, url):
        self.driver.get(url)


    def getBytype(self, locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
             bytype=By.ID
        elif locatortype == "name":
            bytype=By.NAME
        elif locatortype == "classname":
            bytype=By.CLASS_NAME
        elif locatortype == "xpath":
            bytype=By.XPATH
        elif locatortype == "cssselector":
            bytype=By.LINK_TEXT
        elif locatortype == "linktext":
            bytype=By.LINK_TEXT
        elif locatortype == "tagname":
            bytype=By.TAG_NAME
        else:
            print("bytype is not found")
        return bytype


    def getElement(self,locator, locatortype):
        bytype=self.getBytype(locatortype=locatortype)
        element=self.driver.find_element(bytype,locator)
        return element




    def SendKeys(self,element,message):
        element.send_keys(message)

    def clickon(self,element):
        element.click()

    def mouseHoverToElement(self,element):
        self.actions.move_to_element(element).perform()

    def switchToiframe(self,switchToFrame):
        self.driver.switch_to.frame(switchToFrame)

    def screenshots(self):
        filename=str(round(time.time()*1000)) + ".png"
        screenshotspath=TD.screenshotpath
        destinationpath=TD.screenshotpath+filename
        self.driver.save_screenshot(destinationpath)

    def explicitwait(self,locator,locatortype):
        wait=WebDriverWait(self.driver,timeout=10,poll_frequency=1,
                           ignored_exceptions=[NoSuchElementException,
                                               ElementNotVisibleException,
                                               ElementNotSelectableException])
        element=wait.until(EC.element_to_be_clickable((locator,locatortype)))
        return element

    def isElementPresent(self, locator, locatorType):
        element = self.getElement(locator, locatorType)
        if element is not None:
            return True
        else:
            return False

    def getslider(self,element,leftElement):
        self.actions.click_and_hold(on_element=leftElement).move_by_offset(25,0).release(on_element=element).perform()


    def scrollElementIntoView(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(0, -100);")


