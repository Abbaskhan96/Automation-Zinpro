from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time




class Locomotion_score():
   def __init__(self,driver):
       
       #//input[@type='number' and @inputmode = 'numeric' and @class = 'score-count score-count--sm']

       self.driver = driver
       fetched = self.driver.find_element(By.CSS_SELECTOR,((".score-position__score"))).text
       print('fetched-->',fetched)




        