from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as expWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
#sys.path.append("C:/Users/CDC.CDC-PC/source/repos/Automation-Zinpro/Locators_xpath/");
sys.path.append("C:/Users/CDC.CDC-PC/source/repos/Automation-Zinpro/Locators_xpath/");
#sys.path.append("C:/Users/Muhammad Abbas Khan/Source/Repos/Automation-Zinpro/Locators_xpath");
from Locators import locators

class Login():
        
    def __init__(self, driver):

        self.driver = driver
        self.var_wait = expWait(self.driver,5)
        self.username_xpath = locators.username_xpath
        self.password_xpath = locators.password_xpath
        self.btn_xpath = locators.btn_xpath

    def enter_username(self,username):
        self.driver.find_element(By.XPATH, self.username_xpath).clear();
        userID = self.var_wait.until(EC.presence_of_element_located((By.XPATH,self.username_xpath)))
        userID.send_keys(username)
        


    def enter_password(self,password):
        passwordID=self.driver.find_element(By.XPATH,self.password_xpath).clear();
        passwordID=self.var_wait.until(EC.presence_of_element_located((By.XPATH,self.password_xpath)))
        passwordID.send_keys(password)
        
    
    def submitBtn(self):
        loginBtn=self.var_wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_xpath)))
        loginBtn.click()

class Logout():
    
    def __init__(self,driver):
        self.driver=driver
        self.logout_xpath = locators.logout_xpath
        self.var_wait = expWait(self.driver,10)

    def signout(self):
        sign_out=self.var_wait.until(EC.presence_of_element_located((By.XPATH,self.logout_xpath)))
        time.sleep(3)
        sign_out.click()


class invalid_Login():

    def __init__(self, driver):
        # username/password/buttons Xpaths will be same as Valid fields
        self.driver=driver
        self.var_wait = expWait(self.driver,10)
    
    def cookies_notification(self):
         self.driver.find_element(By.XPATH,"//div[@class='close']").click()

    def invalid_username(self, invalid_usernames):
     
        self.cookies_notification()
        invalidUser=self.driver.find_element(By.XPATH, locators.username_xpath).clear();
        invalidUser = self.var_wait.until(EC.presence_of_element_located((By.XPATH,locators.username_xpath)))
        invalidUser.send_keys("")
        invalidUser.send_keys(locators.invalid_usernames)

    def invalid_password(self, invalid_passwords):
        
        invalidPassword=self.driver.find_element(By.XPATH,locators.password_xpath).clear();
        invalidPassword=self.var_wait.until(EC.presence_of_element_located((By.XPATH,locators.password_xpath)))
        invalidPassword.send_keys(locators.invalid_passwords)

    def submitBtn(self):
        self.driver.maximize_window()
        loginBtn=self.var_wait.until(EC.element_to_be_clickable((By.XPATH,locators.btn_xpath)))
        loginBtn.click()
    
    def error_credential_msg(self):
        msg=self.var_wait.until(EC.presence_of_element_located((By.XPATH,locators.invalid_credential_msg_xpath))).text
        return msg
