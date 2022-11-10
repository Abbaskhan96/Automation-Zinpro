from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as expWait
from selenium.webdriver.support import expected_conditions as EC
from LoginPage import Login, Logout, invalid_Login,locators;
from Forget_password import Forget_pass;
from herd_eval import herd_evaluation,quick_evaluation_form;
import time
import unittest
import HtmlTestRunner



class TestClass(unittest.TestCase):
    def setUp(self):
        self.option = Options()
        self.option.binary_location= (r"C:/Program Files/Mozilla Firefox/firefox.exe")
        #path = r"C:/Users/Muhammad Abbas Khan/Desktop/Login.unittest/geckodriver.exe"
        #path = r"C:/Users/CDC.CDC-PC/source/repos/PythonProj_1/unittest.login/Login.unittest/geckodriver.exe"
        path = r"C:/Users/CDC.CDC-PC/source/repos/Automation-Zinpro/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path = path, options = self.option)
        self.wait_key=5;
        self.var_wait = expWait(self.driver, self.wait_key)
        self.usernames = locators.usernames
        self.passwords = locators.passwords
        self.invalid_usernames = locators.invalid_usernames
        self.invald_passwords= locators.invalid_passwords
        
        
    def Launch_driver(self):
        #link = "https://sgp2.zinprofirststep.com/login" 
        link = "https://sgp1.zinprofirststep.com/login" 
        #link = "https://firststep.zinpro.com/"
        self.driver.get(link)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        

    def test_01_login(self):
        self.Launch_driver()
        lpage =Login(self.driver)         
        for i in self.usernames:
           for j in self.passwords:
               lpage.enter_username(i)
               time.sleep(2)
               lpage.enter_password(j);
               lpage.submitBtn();
               signingout = Logout(self.driver)
               signingout.signout()
        print("Valid-Login-Test-Completed-----")       

   
    def test_02_invalid_login(self):
       self.Launch_driver()
       lpage =invalid_Login(self.driver)
       for username in self.invalid_usernames:
           for password in self.invald_passwords:
               lpage.invalid_username(username)
               time.sleep(2)
               lpage.invalid_password(password);
               lpage.submitBtn();
               lpage.error_credential_msg()
               msg=self.var_wait.until(EC.presence_of_element_located((By.XPATH,locators.invalid_credential_msg_xpath))).text
               assert ((msg =="Please enter a valid email, Password must be between 8 and 50 characters") or 
                      (msg == "Please enter a valid email") or
                      (msg == "Email field is required, Password field is required") or 
                      (msg == "Please enter a valid email, Password field is required") or
                      (msg == "Email field is required"))  
  
       
    def test_03_forget_pass(self):
        self.Launch_driver()
        forget_link= Forget_pass(self.driver)
        forget_link.forget_click()
        forget_link.forget_success()
        success_msg = self.var_wait.until(EC.presence_of_element_located((By.XPATH,locators.forget_success_msg_path))).text
        assert(success_msg,"Email Sent")
            
    def test_04_Quick_evaluation(self):
        self.Launch_driver()
        eval = herd_evaluation(self.driver)
        eval_form = quick_evaluation_form(self.driver);
        eval_form.select_Animal_type();
        eval_form.select_Animal_size();
        eval_form.select_currency();
        eval_form.measurements()
        eval_form.date_picker()
        eval_form.eval_name()
        eval_form.input_assessor_array();

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

suite = unittest.TestSuite()
suite.addTest(TestClass("test_04_Quick_evaluation"))

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite)
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:/Users/CDC.CDC-PC/source/repos/PythonProj_1/unittest.login/Login.unittest/reports"))
       