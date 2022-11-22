from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as expWait
from selenium.webdriver.support import expected_conditions as EC
from LoginPage import Login;
from Assessor_list import assessors_list;
import time
from datetime import date;
from Locators import locators 


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
        self.assessor_details = assessors_list(self.driver);
        self.assessor_details.click_assessor_checkbox(self.ask)
        #assessor_details.select_assessor(self.ask)
        self.assessor_details.click_Assessor_Filter_btn(self.ask)
   

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
        self.driver.find_element(By.NAME,"evaluation_name").send_keys("Quick-Evaluation {}".format(datetime.now()))
        self.driver.find_element(By.NAME,"pen_name").send_keys("pen-01-Faroff")
        self.driver.find_element(By.NAME, "pen_size").send_keys("100")
        time.sleep(1);

    def number_of_assessors(self):
        self.ask =[]
        self.numbers_assessors = int(input("How Many Assessors, Do you want to add??"))
        return self.numbers_assessors

    def input_assessor_array(self):
        self.number_of_assessors()
        [self.ask.append(input("Enter Array no of selected Assessor no {} : ".format(i+1))) for i in range(self.numbers_assessors)]
        print(self.ask)
        return self.ask.sort()


class herd_evaluation_form():
    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, 1800);")
        self.driver.find_element(By.XPATH, locators.herd_btn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.NAME,"evaluation_name").send_keys("Quick-Evaluation {}".format(date.today()))

    
        def company(self,driver):
            company_name = Select(self.driver.find_element(By.XPATH, locators.comapny_name))
            company_name.select_by_index(2);
            company_country = Select(self.driver.find_element(By.XPATH, locators.company_country))
            company_country.select_by_visible_text("United States")
            company_state=Select(self.driver.find_element(By.XPATH,locators.company_state))
            company_state.select_by_visible_text("California")
            self.driver.find_element(By.XPATH, locators.company_address).send_keys("Los Angeles, California")
            self.driver.find_element(By.XPATH, locators.company_city).send_keys("California City")
            self.driver.find_element(By.XPATH, locators.company_postal_code).send_keys("90066")        



class herd_evaluation(login_before_evaluation):
    def __init__(self, driver):
        super(). __init__(driver)

      
      #  self.grp1(self,driver)

class groups(herd_evaluation):

    def grp1(self,driver):
        animal_type=Select(self.driver.find_element(By.NAME,("group_type_of_animal")));
        animal_type.select_by_visible_text("Far-off");
        animal_size = Select(self.driver.find_element(By.NAME,("cow_size")));
        animal_size.select_by_index(3)
        self.driver.find_element(By.NAME,"pen_name").send_keys("pFaroff")
        self.driver.find_element(By.NAME, "pen_size").send_keys("100")
        self.grp1_total_assessors = self.number_of_assessors()
        self.grp1_assessors = self.input_assessor_array()
        print(self.grp1_total_assessors,self.grp1_assessors)


    def grp2(self):
        pass

    def grp3(self):
        pass

    def grp4(self):
        pass

    def grp5(self):
        pass


