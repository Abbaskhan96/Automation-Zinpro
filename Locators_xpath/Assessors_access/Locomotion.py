from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time




class Locomotion_score():
   def __init__(self,driver):
       
       #//input[@type='number' and @inputmode = 'numeric' and @class = 'score-count score-count--sm']

       self.driver = driver
       self.driver.find_element(By.XPATH,"//input[@value='grazing_cattle']").click()
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[1]/div[2]/div[2]/input").send_keys("25")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[2]/input").send_keys("15")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[3]/input").send_keys("5")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[4]/input").send_keys("2")
       self.driver.find_element(By.XPATH,"//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[5]/input").send_keys("1")
       



        