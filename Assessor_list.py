from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
sys.path.append("C:/Users/CDC.CDC-PC/source/repos/Automation-Zinpro/Locators_xpath/Assessors_access")
sys.path.append("C:/Users/Muhammad Abbas Khan/Source/Repos/Automation-Zinpro/Locators_xpath/Assessors_access")
sys.path.append("C:/Users/Muhammad Abbas Khan/Source/Repos/Automation-Zinpro/Locators_xpath")
from Dirt_Alot import Dirt_alot;
from Locomotion import Locomotion_score;
from Locators import locators;
from BioSecurity import BioSecurity;
from Heat_Abatement import heat_assessor


class assessors_list():
   
    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, 1800);")
        

    def click_next(self):
        self.driver.find_element(By.XPATH, locators.Next_path).click()
        self.driver.find_element(By.XPATH, locators.assesor_sort_path).click()
        time.sleep(3)
        
    def herd_click_next(self):
        self.driver.find_element(By.XPATH, locators.herd_next_path).click()
        self.driver.find_element(By.XPATH, locators.herd_assessor_sort_path).click()
        time.sleep(3)
        

    
    #checking that if Both Reports, Next Assessor buttons are not && in assessor details page it should be clicked on Reports
    #else only Next Assessor button clicked
    
    def click_Assessor_Filter_btn(self,ask):
        self.ask= ask
        for i in range(len(self.ask)):
            print(i,self.ask[i])
           # print(self.ask[i],self.ask[-1],type(self.ask[-1]))
            self.select_assessor(self.ask[i])
            if i == (len(self.ask)-1):
                #clicking report button
                self.driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-full--sm pull-right']").click()
                time.sleep(3)
                break;
            self.driver.find_element(By.XPATH,"//span[normalize-space()='Next Assessor']").click()    
            print("Next Assessor clicked")
            time.sleep(3)
            
      
       

    def select_assessor(self,arg):
        self.arg = arg 
        print(self.arg)
        if "1" == self.arg:
            #---Selecting DirAlot CheckBox
                #self.driver.find_element(By.XPATH,((locators.locomotion_checkbox))).click() 
             print("Locomotion Assessor is Temporarely Selected...")
             Locomotion_score(self.driver)
             self.arg=None
             #self.click_Assessor_Filter_btn(self.ask)
             time.sleep(2)


        elif "8" == self.arg:
            print("Bio Security is selected")
            BioSecurity(self.driver)
            self.arg=None
            time.sleep(2)


        elif "14" == self.arg:
            print("Dirt Alot is selected...")
            dirt_alot_start = Dirt_alot(self.driver)
            self.arg=None
            time.sleep(2)


        elif "15" == self.arg:
                #---Selecting Heat-Abatement CheckBox
                #self.driver.find_element(By.NAME,"evaluation_name").clear()
                #self.driver.find_element(By.NAME,"evaluation_name").send_keys("Quick-Evaluation-Heat-Abatement")
             print("Heat Abatement is selected...")
             heat_assessor_start = heat_assessor(self.driver)
             heat_assessor_start.selecting_dropdown()
             heat_assessor_start.input_values()
             self.arg=None
             time.sleep(1)
        

    def click_assessor_checkbox(self, ask):
        #check the array number for ticking the box
        
        if "1" in ask:
            self.driver.find_element(By.XPATH,((locators.locomotion_checkbox))).click()
    
        if "14" in ask:
            self.driver.find_element(By.XPATH,((locators.Dirt_Alot_checkbox))).click() 

        if "15" in ask:
            self.driver.find_element(By.XPATH,((locators.heat_abatement_checbox))).click() 

        if "8" in ask:
            self.driver.find_element(By.XPATH,((locators.Bio_security))).click()
       
        
        time.sleep(2)
