from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time




class Locomotion_score():
   
    

    def __init__(self,driver, group):
       self.driver = driver
       #//input[@type='number' and @inputmode = 'numeric' and @class = 'score-count score-count--sm']
       locom_dict = {
           "closed": self.closed_locom,
           "faroff": self.faroff_locom,
           "fresh": self.fresh_locom,
           "lactating": self.lactating_locom
           }
       locom_dict[group]()
       
       
       
    def closed_locom(self):
       
       self.driver.find_element(By.XPATH,"//input[@value='grazing_cattle']").click()
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[1]/div[2]/div[2]/input").send_keys("25")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[2]/input").send_keys("15")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[3]/input").send_keys("5")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[4]/input").send_keys("2")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[5]/input").send_keys("1")
       
    def faroff_locom(self):
       
       self.driver.find_element(By.XPATH,"//input[@value='confined_cattle']").click()
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[1]/div[2]/div[2]/input").send_keys("22")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[2]/input").send_keys("15")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[3]/input").send_keys("5")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[4]/input").send_keys("2")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[5]/input").send_keys("0")

    def fresh_locom(self):
       
       self.driver.find_element(By.XPATH,"//input[@value='confined_cattle']").click()
       self.driver.find_element(By.XPATH, "//label[@for='on']").click()
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[1]/div[2]/div[2]/input").send_keys("17")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[2]/input").send_keys("12")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[3]/input").send_keys("10")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[4]/input").send_keys("9")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[5]/input").send_keys("8")
       
    def lactating_locom(self):
       
       self.driver.find_element(By.XPATH,"//input[@value='grazing_cattle']").click()
       self.driver.find_element(By.XPATH, "//label[@for='on']").click()
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[1]/div[2]/div[2]/input").send_keys("7")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[2]/input").send_keys("8")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[3]/input").send_keys("9")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[4]/input").send_keys("10")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[5]/input").send_keys("10")


        