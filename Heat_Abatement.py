from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from xpath_heat_abate import Assessors_xpath as loc;
import time


class heat_assessor():
    
    def __init__(self, driver):
        self.driver=driver
        print("Heat Abatement");
        
        func = lambda : [i for i in loc.path]
        [self.driver.find_element(By.XPATH, i).click() for i in func()]



