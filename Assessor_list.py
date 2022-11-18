from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Locomotion import Locomotion_score;
import time
from Locators import locators
import sys
sys.path.append("C:/Users/CDC.CDC-PC/source/repos/Automation-Zinpro/Assessors_access")
sys.path.append("C:/Users/Muhammad Abbas Khan/source/repos/Automation-Zinpro/Assessors_access")
from Heat_Abatement import heat_assessor;


class assessors_list():
   
    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, 1000);")
        

    def click_next(self):
        self.driver.find_element(By.XPATH, locators.Next_path).click()
        self.driver.find_element(By.XPATH, locators.assesor_sort_path).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 1000);")

    
    #checking that if Both Reports, Next Assessor buttons are not && in assessor details page it should be clicked on Reports
    #else only Next Assessor button clicked
    
    def click_Assessor_Filter_btn(self,ask):
        self.ask= ask
        select_filter = Select(self.driver.find_element(By.CSS_SELECTOR,("//a[@class='btn btn-primary btn-full--sm pull-right']")))
        for i in range((len(self.ask))):
            select_filter.select_by_index(i)
            select_assessor(ask[i])
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-full--sm pull-right']" )


    def select_assessor(self,ask):
        self.ask = ask 
        if "1" in self.ask:
            #---Selecting DirAlot CheckBox
                #self.driver.find_element(By.XPATH,((locators.locomotion_checkbox))).click() 
            print("Locomotion Assessor is Temporarely Selected...")
            time.sleep(1)


        if "15" in self.ask:
                #---Selecting Heat-Abatement CheckBox
                #self.driver.find_element(By.NAME,"evaluation_name").clear()
                #self.driver.find_element(By.NAME,"evaluation_name").send_keys("Quick-Evaluation-Heat-Abatement")
           heat_assessor_start = heat_assessor(self.driver)
           heat_assessor_start.selecting_dropdown()
           heat_assessor_start.input_values()
           self.click_report_or_Next_Assessor_btn()
           time.sleep(3)
        else:
           #raise KeyboardInterrupt(self.ask)
           raise ValueError("Incorrect Given Key")

    def click_assessor_checkbox(self, ask):
        #check the array number for ticking the box
       
        if "1" in ask:
            self.driver.find_element(By.XPATH,((locators.locomotion_checkbox))).click()

        if "15" in ask:
            self.driver.find_element(By.XPATH,((locators.heat_abatement_checbox))).click() 

        self.click_next()
        time.sleep(2)
