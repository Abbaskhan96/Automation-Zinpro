from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as expWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import locators
import time

class Forget_pass():

    def __init__(self,driver):
        self.driver = driver;
        self.var_wait = expWait(self.driver,10)
        

    def forget_click(self):
        forgetLink = self.var_wait.until(EC.element_to_be_clickable((By.XPATH,locators.forget_link)))
        forgetLink.click()
        time.sleep(2)

    def forget_success(self):
        self.driver.find_element(By.XPATH, locators.forget_email_path).clear()
        forget_email = self.var_wait.until(EC.presence_of_element_located((By.XPATH,locators.forget_email_path)))
        forget_email.send_keys(locators.forget_email)
        forget_email.submit()
        success_msg = self.var_wait.until(EC.presence_of_element_located((By.XPATH,locators.forget_success_msg_path))).text
        return success_msg
        time.sleep(3)
      
    def forget_fail(self):
        pass


class Forget_fail(Forget_pass):

    def __init__(self, driver):
        super().__init__(self, driver)
        self.forget_click()

    def forget_fail(self):
        self.driver.find_element(By.X)