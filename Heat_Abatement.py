from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from xpath_heat_abate import Assessors_xpath as loc;
import time


class heat_assessor():
    
    def __init__(self, driver):
        self.driver=driver
        print("Heat Abatement");
        

    def clicking_values(self):
        self.driver.find_element(By.XPATH,loc.WA_yes).click()
        self.driver.find_element(By.XPATH,((loc.Warea_yes))).click()
        self.driver.find_element(By.XPATH,loc.FL_FA_yes).click()
        self.driver.find_element(By.XPATH,loc.HVLS_FA_no).click()
        self.driver.find_element(By.XPATH,loc.FL_Ra_yes).click()
        self.driver.find_element(By.XPATH,loc.HVLS_RA_no).click()
        self.driver.find_element(By.XPATH,loc.Soak_FA_yes).click()
        self.driver.find_element(By.XPATH,loc.Soak_RA_yes).click()
        self.driver.find_element(By.XPATH,loc.drop_yes).click()
        self.driver.find_element(By.XPATH,loc.SoakFreq_VT_yes).click()
        self.driver.find_element(By.XPATH,loc.Shade_FA_yes).click()
        self.driver.find_element(By.XPATH,loc.Shade_RA_yes).click()
        self.driver.find_element(By.XPATH,loc.Shada_unit_yes).click()
        self.water_pen = self.driver.find_element(By.XPATH,loc.accessible_water_pen).send_keys("1500")
        print(self.water_pen)
        time.sleep(3)
