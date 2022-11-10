from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Locators import locators;
from Locomotion import Locomotion_score;
import time



class assessors_list():
   
    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, 1000);")
        

    def click_next(self):
        self.driver.find_element(By.XPATH, locators.Next_path).click()
        self.driver.find_element(By.XPATH, locators.assesor_sort_path).click()
        time.sleep(3)

    def select_assessor(self,ask):
        self.ask = ask
        if self.ask == "1":
            #---Selecting Locomotion CheckBox
            self.driver.find_element(By.XPATH,((locators.locomotion_checkbox))).click() 
            self.click_next()


        elif self.ask == "15":
            #---Selecting Heat-Abatement CheckBox
            self.driver.find_element(By.XPATH,((locators.heat_abatement_checbox))).click() 
            self.click_next()
            time.sleep(2)