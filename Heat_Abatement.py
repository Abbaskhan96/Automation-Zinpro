from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from xpath_heat_abate import Assessors_xpath as loc;


class heat_assessor():
    
    def __init__(self, driver):
        self.driver=driver
        print("Heat Abatement");
        self.driver.find_element(By.XPATH,(("//label[@for='3z15ad']"))).submit()

        #for i in self.clickable_xpath:
        #    self.driver.find_element(By.XPATH,(i)).click()
        #    time.sleep(10)

  