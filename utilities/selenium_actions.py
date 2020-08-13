
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from test_results.logger import customLogger
import logging

class Se_actions():

    def __init__(self,driver):
        self.driver=driver
        self.log=customLogger(logLevel=logging.DEBUG)

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
        actions=ActionChains(driver=self.driver)
        actions.move_to_element(element).perform()

    def switchToiframe(self,switchToFrame):
        self.driver.switch_to.frame(switchToFrame)







