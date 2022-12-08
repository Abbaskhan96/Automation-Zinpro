from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class BioSecurity():

    _yes = ["//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[{}]/div[2]/div[2]/label".format(i) for i in range(2,8)]
    

    _no = ["//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[{}]/div[2]/div[1]/label".format(i) for i in range(2,8)]

    _half_yes = ["//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[{}]/div[2]/div[2]/label".format(i) for i in range(2,5)]
    _half_no = ["//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[{}]/div[2]/div[1]/label".format(i) for i in range(5,8)]

    _one_each_yes = ["//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[{}]/div[2]/div[2]/label".format(i) for i in range(2,8,2)]
    _one_each_no = ["//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[{}]/div[2]/div[1]/label".format(i) for i in range(3,8,2)]



    def __init__(self,driver, group):
        self.driver = driver
        Bio_dict = {
           "closed": self.closed_Bio,
           "faroff": self.faroff_Bio,
           "fresh": self.fresh_Bio,
           "lactating": self.lactating_Bio
           }
        Bio_dict[group]()

    def closed_Bio(self):
        [self.driver.find_element(By.XPATH, i).click() for i in self._yes]
        time.sleep(1)

    def faroff_Bio(self):
        [self.driver.find_element(By.XPATH, i).click() for i in self._no]
        time.sleep(1)

    def fresh_Bio(self):
        [self.driver.find_element(By.XPATH, i).click() for i in self._half_yes]
        [self.driver.find_element(By.XPATH, i).click() for i in self._half_no]
        time.sleep(1)

    def lactating_Bio(self):
        [self.driver.find_element(By.XPATH, i).click() for i in self._one_each_yes] 
        [self.driver.find_element(By.XPATH, i).click() for i in self._one_each_no]        
        time.sleep(1)