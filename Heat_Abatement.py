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
        time.sleep(2)

    def input_values(self):    
        self.driver.find_element(By.XPATH, loc.accessible_water_pen).send_keys("1500")
        self.driver.find_element(By.XPATH, loc.Fan_FA_temp).send_keys("20")
        self.driver.find_element(By.XPATH, loc.Fan_FA_space).send_keys("12")
        self.driver.find_element(By.XPATH, loc.Fan_RA_temp).send_keys("21")
        self.driver.find_element(By.XPATH, loc.Fan_RA_space).send_keys("5")
        self.driver.find_element(By.XPATH, loc.Soak_temp).send_keys("21")
        self.driver.find_element(By.XPATH, loc.Soak_time).send_keys("15")
        self.driver.find_element(By.XPATH, loc.Soak_freq).send_keys("60")
        time.sleep(2)
    
    def selecting_dropdown(self):    
        index = [7,3]
        for i,j in zip(loc.select_fields,index):
            drop_field = Select(self.driver.find_element(By.XPATH,i))
            drop_field.select_by_index(j)
            time.sleep(1)
        time.sleep(2)

        