from selenium import webdriver




class webdriverfactory():

    def webdriver_instance(self,browser):
        driver=None
        if browser=="Firefox":
             driver= webdriver.Firefox()
        elif browser=="Chrome":
            driver= webdriver.Chrome()
        elif browser=="ie":
            driver= webdriver.Ie()
        else:
            print("browser not found")

        driver.maximize_window()
        driver.implicitly_wait(3)
        return driver

