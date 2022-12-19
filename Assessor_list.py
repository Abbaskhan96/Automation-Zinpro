from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
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
#import autoit
import pyautogui


class assessors_list():
   
    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, 2500);")
        

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
    

    def returning_mydict(self,names,assessors):
        dict2 = dict(zip(names,assessors))
        return dict2

    def by_group(self,names,assessors):
        dict2 = dict(zip(names,assessors))
        print(dict2)
        for key in dict2.keys():
            self.driver.find_element(By.XPATH, locators.group_dropdown).click()
            print(key)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//a[@class='dropdown-item__link'][normalize-space()='{}']".format(key)).click()
            time.sleep(3)
            for values in dict2.get(key):
                self.select_assessor(key, values, names, assessors, dict2)


    def for_clicking_next_report(self, key, values, names, assessors, dict2):
        if not (key == (names[-1]) or values == dict2.get(key)[-1]):
            print("Next selected", names[-1], key, assessors[-1], values, "the dict is : ", dict2.get(key)[-1])
            self.driver.find_element(By.XPATH,"//span[normalize-space() = 'Next Assessor']").click()
        elif values in assessors[-1]:
            print(key)
            if (key == (names[-1]) and values == assessors[-1][-1]):
                print(values)
                #clicking report button
                self.driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-full--sm pull-right']").click()
               # self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-full--sm pull-right']")
                time.sleep(4)
            if (key == (names[-1]) and not values == assessors[-1][-1]):
                self.driver.find_element(By.XPATH,"//span[normalize-space() = 'Next Assessor']").click()




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
            
      
       

    def select_assessor(self, arg, values, names, assessors, dict2):
        self.values = values
        print(arg)
        print(self.values)
        print(names)
        print(assessors)
        if ("1" == self.values):
            #---Selecting DirAlot CheckBox
                #self.driver.find_element(By.XPATH,((locators.locomotion_checkbox))).click() 
             print("Locomotion Assessor is Temporarely Selected...")
             Locomotion_score(self.driver, arg)
             #self.click_Assessor_Filter_btn(self.ask)
             self.upload_img(self.values)
             self.for_clicking_next_report(arg, self.values, names, assessors, dict2)
             self.arg=None
             self.values = None
             time.sleep(2)


        elif "8" == self.values:
            print("Bio Security is selected")
            BioSecurity(self.driver, arg)
            self.upload_img(self.values)
            self.for_clicking_next_report(arg, self.values, names, assessors, dict2)
            self.arg=None
            self.values = None
            time.sleep(2)



        elif "14" == self.values:
            print("Dirt Alot is selected...")
            dirt_alot_start = Dirt_alot(self.driver, arg)
            self.upload_img(self.values)
            self.for_clicking_next_report(arg, self.values, names, assessors, dict2)
            self.arg=None
            self.values = None
            time.sleep(2)



        elif "15" == self.values:
                #---Selecting Heat-Abatement CheckBox
                #self.driver.find_element(By.NAME,"evaluation_name").clear()
                #self.driver.find_element(By.NAME,"evaluation_name").send_keys("Quick-Evaluation-Heat-Abatement")
             print("Heat Abatement is selected...")
             heat_assessor_start = heat_assessor(self.driver, arg)
             self.upload_img(self.values)
             self.for_clicking_next_report(arg, self.values, names, assessors, dict2)
             self.arg=None
             self.values = None
             time.sleep(2)

        

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


    def upload_img(self, assessor_no):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Upload Images']").click()
        self.driver.find_element(By.XPATH, "//label[@for='files']").click()
       # autoit.win_active("Open") 
       # autoit.control_send("Open","Edit1","E:/01.jpg")
       # autoit.control_send("Open", "Edit1", "{ENTER}")
       # file.send_keys("C:/Users/Muhammad Abbas Khan/Documents/pics/01.jpg")
        time.sleep(2)
        pyautogui.write(r"C:\Users\Muhammad Abbas Khan\Documents\pics\Kbs-size\_{}.jpg".format(assessor_no))
        #pyautogui.write(r"C:\Users\CDC.CDC-PC\Documents\_{}.jpg".format(assessor_no))
        time.sleep(1)
        pyautogui.press("enter")
        self.driver.find_element(By.XPATH, "//div[@class='col-md-12']//button[@type = 'button']").click()
       # time.sleep(9)
        self.wait = wait(self.driver, 10, poll_frequency=5) 
        Done=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Done']" )))
        Done.click()
        #self.driver.find_element(By.XPATH, "//button[normalize-space()='Done']").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        