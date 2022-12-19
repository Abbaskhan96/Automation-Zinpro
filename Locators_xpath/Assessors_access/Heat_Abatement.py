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
        (self.driver.find_element(By.XPATH, i).click() for i in loc)
        for i in loc:
            self.driver.find_element(By.XPATH, i).click()
#        self.driver.find_element(By.XPATH, loc).click()
#        [i for i in loc.path_yes.keys()]
        #input data into fields....

        
#        self.driver.find_element(By.XPATH, loc.Fan_FA_temp).send_keys("20")
#        self.driver.find_element(By.XPATH, loc.Fan_FA_space).send_keys("12")
#        self.driver.find_element(By.XPATH, loc.Fan_RA_temp).send_keys("21")
#        self.driver.find_element(By.XPATH, loc.Fan_RA_space).send_keys("5")
#        self.driver.find_element(By.XPATH, loc.Soak_temp).send_keys("21")
#        self.driver.find_element(By.XPATH, loc.Soak_time).send_keys("15")
#        self.driver.find_element(By.XPATH, loc.Soak_freq).send_keys("60")
#        time.sleep(2)

        # selecting Dropdowns fields
        index = [7,3]
        self.selecting_dropdown(index)


    def faroff_HeatAbatement(self):
        self.driver.find_element(By.XPATH, loc.accessible_water_pen).send_keys("600")
        func = lambda : [i for i in loc.path_no]
        [self.driver.find_element(By.XPATH, i).click() for i in func()]
        time.sleep(2)


    
    def fresh_HeatAbatement(self):
        self.driver.find_element(By.XPATH, loc.accessible_water_pen).send_keys("1100")
        func = lambda : [i for i in loc.path_N_A]
        [self.driver.find_element(By.XPATH, i).click() for i in func()]
        time.sleep(2)


    def lactating_HeatAbatement(self):
        func = lambda : [i for i in loc.path_yes_no]
        [self.driver.find_element(By.XPATH, i).click() for i in func()]
        time.sleep(2)


        #inserting Data into Fields
        self.driver.find_element(By.XPATH, loc.accessible_water_pen).send_keys("3000")
        self.driver.find_element(By.XPATH, loc.Fan_FA_temp).send_keys("32")
        self.driver.find_element(By.XPATH, loc.Fan_FA_space).send_keys("29")
        self.driver.find_element(By.XPATH, loc.Fan_RA_temp).send_keys("38")
        self.driver.find_element(By.XPATH, loc.Fan_RA_space).send_keys("41")
        self.driver.find_element(By.XPATH, loc.Soak_temp).send_keys("26")
        self.driver.find_element(By.XPATH, loc.Soak_time).send_keys("30")
        self.driver.find_element(By.XPATH, loc.Soak_freq).send_keys("120")
        time.sleep(2)

        # selecting Dropdowns fields
        index = [9,1]
        self.selecting_dropdown(index)