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
        self.assessor_details.click_next(self)
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
        [self.ask.append(input("Enter Array no of selected Assessor no {} : ".format(i+1))) for i in range(self.numbers_assessors)]
        self.ask.sort()
        print(self.ask)
        return self.ask


class herd_evaluation_form():
    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0, 1800);")
        self.driver.find_element(By.XPATH, locators.herd_btn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.NAME,"evaluation_name").send_keys("Herd-Evaluation {}".format(date.today()))

    
    def company(self):
        company_name = Select(self.driver.find_element(By.XPATH, locators.company_name))
        company_name.select_by_index(2);
        company_country = Select(self.driver.find_element(By.XPATH, locators.company_country))
        company_country.select_by_visible_text("United States")
        company_state=Select(self.driver.find_element(By.XPATH,locators.company_state))
        company_state.select_by_visible_text("California")
        self.driver.find_element(By.XPATH, locators.company_address).clear()
        self.driver.find_element(By.XPATH, locators.company_address).send_keys("Los Angeles, California")
        self.driver.find_element(By.XPATH, locators.company_city).clear()
        self.driver.find_element(By.XPATH, locators.company_city).send_keys("California City")
        self.driver.find_element(By.XPATH, locators.company_postal_code).clear()   
        self.driver.find_element(By.XPATH, locators.company_postal_code).send_keys("90066")   
        
    def dairy(self):
        company_name = Select(self.driver.find_element(By.XPATH, locators.dairy_name))
        company_name.select_by_index(2);
        company_country = Select(self.driver.find_element(By.XPATH, locators.dairy_country))
        company_country.select_by_visible_text("United States")
        company_state=Select(self.driver.find_element(By.XPATH,locators.dairy_state))
        company_state.select_by_visible_text("California")
        self.driver.find_element(By.XPATH, locators.dairy_address).clear()
        self.driver.find_element(By.XPATH, locators.dairy_address).send_keys("Los Angeles, California")
        self.driver.find_element(By.XPATH, locators.dairy_city).clear()
        self.driver.find_element(By.XPATH, locators.dairy_city).send_keys("California City")
        self.driver.find_element(By.XPATH, locators.dairy_postal_code).clear()   
        self.driver.find_element(By.XPATH, locators.dairy_postal_code).send_keys("90066")   

    def contact(self):
        contact_name_select = Select(self.driver.find_element(By.XPATH, locators.contact_name_select))
        contact_name_select.select_by_index(2)
        contact_email = self.driver.find_element(By.XPATH,locators.contact_email).clear()
        contact_email = self.driver.find_element(By.XPATH,locators.contact_email).send_keys("email@email.com")
        contact_business_phone = self.driver.find_element(By.XPATH,locators.contact_business_phone).clear()
        contact_business_phone = self.driver.find_element(By.XPATH,locators.contact_business_phone).send_keys("Business_Phones")


    def characteristics(self):
        consultation_date = self.driver.find_element(By.XPATH,locators.consultation_date).click()
        select_Date = self.driver.find_element(By.XPATH,locators.select_Date).click()
        herd_size = self.driver.find_element(By.XPATH,locators.herd_size).clear()
        herd_size = self.driver.find_element(By.XPATH,locators.herd_size).send_keys("600")
        currency = Select(self.driver.find_element(By.XPATH,locators.currency))
        currency.select_by_index(25)
        milk_production = self.driver.find_element(By.XPATH,locators.milk_production).clear()
        milk_production = self.driver.find_element(By.XPATH,locators.milk_production).send_keys("1500")
        milk_price = self.driver.find_element(By.XPATH, locators.milk_price).clear()
        milk_price = self.driver.find_element(By.XPATH, locators.milk_price).send_keys("0.5")

        
            
# .............Factory Design Method------------------

class herd_evaluation(login_before_evaluation):
    def __init__(self, driver):
        super(). __init__(driver)
    def Client(self, driver):
        _client_data= herd_evaluation_form(self.driver)
        _client_data.company()
        _client_data.dairy()
        _client_data.contact()
        _client_data.characteristics()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-full--sm mt-4 float-right']").click()
 


class groups():

    def grp1(self,driver):
        self.driver = driver
        animal_type=Select(self.driver.find_element(By.NAME,("group_type_of_animal")));
        animal_type.select_by_visible_text("Far-off");
        animal_size = Select(self.driver.find_element(By.NAME,("cow_size")));
        animal_size.select_by_index(3)
        self.driver.find_element(By.NAME,"group_name").send_keys("Faroff")
        self.driver.find_element(By.NAME, "group_size").send_keys("100")
        grp1_total_assessors = quick_evaluation_form.number_of_assessors(self)
        grp1_assessors = quick_evaluation_form.input_assessor_array(self)
        assessors_list.click_assessor_checkbox(self,grp1_assessors)
        print(grp1_total_assessors,grp1_assessors)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Group']").click()
       # self.driver.find_element(By.XPATH,"//div[contains(@data-toggle , 'collapse') and @aria-expanded = 'true']").click()
        time.sleep(2)


    def grp2(self,driver):
        self.driver = driver
        animal_type=Select(self.driver.find_element(By.XPATH,("(//select[@data-vv-as='Type of Animal'])[1]")));
        animal_type.select_by_index("1");
        animal_size = Select(self.driver.find_element(By.XPATH,("(//select[@data-vv-as='Avg. Cow Size'])[1]")));
        animal_size.select_by_index(3)
        self.driver.find_element(By.XPATH,"//div[@class='col-md-12']//input[@name='group_name']").send_keys("Closed")
        self.driver.find_element(By.XPATH,"//div[@class='col-md-6']//input[@name='group_size']").send_keys("90")
        grp2_total_assessors = quick_evaluation_form.number_of_assessors(self)
        grp2_assessors = quick_evaluation_form.input_assessor_array(self)
        assessors_list.click_assessor_checkbox(self,grp2_assessors)
        print(grp2_total_assessors,grp2_assessors)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Group']").click()
       # self.driver.find_element(By.XPATH,"//div[contains(@data-toggle , 'collapse') and @aria-expanded = 'true']").click()



    def grp3(self,driver):
        self.driver = driver
        animal_type=Select(self.driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/select"));
        animal_type.select_by_visible_text("Fresh");
        animal_size = Select(self.driver.find_element(By.XPATH,("(//select[@data-vv-as='Avg. Cow Size'])[1]")));
        animal_size.select_by_index(2)
        self.driver.find_element(By.XPATH,"//div[@class='col-md-12']//input[@name='group_name']").send_keys("Fresh")
        self.driver.find_element(By.XPATH,"//div[@class='col-md-6']//input[@name='group_size']").send_keys("75")
        #self.driver.find_element(By.XPATH,"//input[@name='group_milk_prod']").send_keys("200")
        grp3_total_assessors = quick_evaluation_form.number_of_assessors(self)
        grp3_assessors = quick_evaluation_form.input_assessor_array(self)
        assessors_list.click_assessor_checkbox(self,grp3_assessors)
        print(grp3_total_assessors,grp3_assessors)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Group']").click()
       # self.driver.find_element(By.XPATH,"//div[contains(@data-toggle , 'collapse') and @aria-expanded = 'true']").click()

    def grp4(self,driver):
        self.driver = driver
        animal_type=Select(self.driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/select"));
        animal_type.select_by_index("4");
        animal_size = Select(self.driver.find_element(By.XPATH,("(//select[@data-vv-as='Avg. Cow Size'])[1]")));
        animal_size.select_by_index(2)
        self.driver.find_element(By.XPATH,"//div[@class='col-md-12']//input[@name='group_name']").send_keys("Lactating")
        self.driver.find_element(By.XPATH,"//div[@class='col-md-6']//input[@name='group_size']").send_keys("220")
        self.driver.find_element(By.XPATH,"//input[@name='group_milk_prod']").send_keys("1000")
        grp4_total_assessors = quick_evaluation_form.number_of_assessors(self)
        grp4_assessors = quick_evaluation_form.input_assessor_array(self)
        assessors_list.click_assessor_checkbox(self,grp3_assessors)
        print(grp4_total_assessors,grp4_assessors)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Group']").click()
       # self.driver.find_element(By.XPATH,"//div[contains(@data-toggle , 'collapse') and @aria-expanded = 'true']").click()

    def grp5(self):
        pass


