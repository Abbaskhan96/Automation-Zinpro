from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as expWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import locators;
from LoginPage import Login;
from Assessor_list import *;
import time


class login_before_evaluation():
    def __init__(self, driver):
        self.driver = driver
        signin = Login(self.driver)
        signin.enter_username(locators.usernames[0])
        signin.enter_password(locators.passwords[0])
        time.sleep(3)
        signin.submitBtn()
        time.sleep(3)



class quick_evaluation_form():
    def __init__(self,driver):
        self.driver=driver
        self.driver.find_element(By.XPATH,locators.eval_quick_bton_xpath).click()
   

    def select_Animal_type(self):
        animal_type=Select(self.driver.find_element(By.NAME,("group_type_of_animal")));
        animal_type.select_by_visible_text("Far-off");
        

    def select_Animal_size(self):
        animal_size = Select(self.driver.find_element(By.NAME,("cow_size")));
        animal_size.select_by_index(2)
        
     
 #   def select_assessor(self):
 #       locom_assessor = self.driver.find_element(By.XPATH,locators.Locomotion_assessor_xpath)
 #       locom_assessor.click()
 #       time.sleep(3)

    def select_currency(self):
        currency = Select(self.driver.find_element(By.NAME,("currency_qs")))
        currency.select_by_index(25)
        time.sleep(3)

    def measurements(self):
       
        for i in locators.values:
            self.driver.find_element(By.XPATH, ((locators.measurement_path).format(i))).click()
            


    def date_picker(self):
        self.driver.find_element(By.NAME,("consultation_date")).click()
        self.driver.find_element(By.XPATH,(("//span[normalize-space()='6']"))).click()
        time.sleep(1)

    def eval_name(self):
        self.driver.find_element(By.NAME,"evaluation_name").send_keys("Quick-Evaluation")
        self.driver.find_element(By.NAME,"pen_name").send_keys("pen-01-Faroff")
        self.driver.find_element(By.NAME, "pen_size").send_keys("100")
        time.sleep(1);

    def number_of_assessors(self):
        self.ask =[]
        self.numbers_assessors = int(input("How Many Assessors, Do you want to add??"))

    def input_assessor_array(self):
        self.number_of_assessors()
        [self.ask.append(input("Enter Array no of selected Assessor no {} : ".format(i+1))) for i in range(self.numbers_assessors)]
  #      print(self.ask)

        locom = assessors_list(self.driver);
        locom.click_assessor_checkbox(self.ask)
       #locom.select_assessor(self.ask);






class herd_evaluation(login_before_evaluation):
    def __init__(self, driver):
        super(). __init__(driver)