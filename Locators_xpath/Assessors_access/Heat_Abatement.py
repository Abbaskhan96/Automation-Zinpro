from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
sys.path.append('C:/Users/Muhammad Abbas Khan/source/repos/Automation-Zinpro/All_assessors_xpath');
sys.path.append('C:/Users/CDC.CDC-PC/source/repos/Automation-Zinpro/All_assessors_xpath')
from xpath_heat_abate import Assessors_HeatAbatement_xpath;

class heat_assessor():
    
    def __init__(self, driver, group):
        
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, 1000);")

        _HeatAbatment_dict = {
           "closed": self.closed_HeatAbatement,
           "faroff": self.faroff_HeatAbatement,
           "fresh": self.fresh_HeatAbatement,
           "lactating": self.lactating_HeatAbatement
           }
        _HeatAbatment_dict[group]()
        
       
    
    
#    def selecting_dropdown(self, index):    
#        for i,j in zip(loc.select_fields,index):
#            drop_field = Select(self.driver.find_element(By.XPATH,i))
#            drop_field.select_by_index(j)
#            time.sleep(1)
#        time.sleep(2)

   
    def closed_HeatAbatement(self):
        loc = Assessors_HeatAbatement_xpath(self.driver)
#        func = lambda : [i for i in loc]
        data = loc.data_sheet(10,21,7)
        for i in data:
           # print(i,"\n")
            self.driver.find_element(By.XPATH, i).click()
        time.sleep(2)
    
        

    def faroff_HeatAbatement(self):
 
        loc = Assessors_HeatAbatement_xpath(self.driver)
#        func = lambda : [i for i in loc]
        data = loc.data_sheet(10,21,9)
        for i in data:
          #  print(i,"\n")
            self.driver.find_element(By.XPATH, i).click()
        time.sleep(2)


    
    def fresh_HeatAbatement(self):
        

        loc = Assessors_HeatAbatement_xpath(self.driver)
#        func = lambda : [i for i in loc]
        data = loc.data_sheet(10,21,11)
        for i in data:
          #  print(i,"\n")
            self.driver.find_element(By.XPATH, i).click()
        time.sleep(2)


    def lactating_HeatAbatement(self):
        

        loc = Assessors_HeatAbatement_xpath(self.driver)
#        func = lambda : [i for i in loc]
        data = loc.data_sheet(10,21,13)
        for i in data:
          #  print(i,"\n")
            self.driver.find_element(By.XPATH, i).click()
        time.sleep(2)