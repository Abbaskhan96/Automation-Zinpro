
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class heat_assessor():

    def __new__(cls,driver):
        self.driver= driver
        print("Heat Abatement");
        
