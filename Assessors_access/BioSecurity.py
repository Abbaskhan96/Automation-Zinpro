from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class BioSecurity():

    _yes = ["//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[{}]/div[2]/div[2]/label".format(i) for i in range(9)]
    

    _no = ["//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[{}]/div[2]/div[1]/label".format(i) for i in range(9)]

    def __init__(self,driver):
        self.driver = driver
        [self.driver.find_element(By.XPATH, i).click() for i in self._yes]
        time.sleep(2)