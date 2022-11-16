from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Locators import locators;
from Locomotion import Locomotion_score;
from Heat_Abatement import heat_assessor;
import time



class assessors_list():
   
    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, 1000);")
        

    def click_next(self):
        self.driver.find_element(By.XPATH, locators.Next_path).click()
        self.driver.find_element(By.XPATH, locators.assesor_sort_path).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 1000);")

    def select_assessor(self,ask):
        self.ask = ask
        for i in self.ask: 
            if i == "1":
                #---Selecting DirAlot CheckBox
                #self.driver.find_element(By.XPATH,((locators.locomotion_checkbox))).click() 
                print("Assessor no {} is selected....".format(i))
                #self.click_next()


            elif i == "15":
                #---Selecting Heat-Abatement CheckBox
                #self.driver.find_element(By.NAME,"evaluation_name").clear()
                #self.driver.find_element(By.NAME,"evaluation_name").send_keys("Quick-Evaluation-Heat-Abatement")
                self.click_next()
                heat_assessor_start = heat_assessor(self.driver)
                heat_assessor_start.selecting_dropdown()
                heat_assessor_start.input_values()
                self.driver.find_element(By.XPATH,"//*[@class = 'col-md-24']//a[@href='/reports']").click()
                time.sleep(3)
            else:
                raise KeyboardInterrupt(self.ask)

    def click_assessor_checkbox(self, ask):
        #check the array number for ticking the box
        if "15" in ask:
            self.driver.find_element(By.XPATH,((locators.heat_abatement_checbox))).click() 

        if "1" in ask:
            self.driver.find_element(By.XPATH,((locators.locomotion_checkbox))).click()
        time.sleep(2)
