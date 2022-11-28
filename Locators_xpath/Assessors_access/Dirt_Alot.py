from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Dirt_alot():
    
    #|------------------HeadLock_FeedSpace Atleast_one---------------------
    headlock_FS_no="/html/body/div/main/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/label"
    headlock_FS_yes="/html/body/div/main/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[2]/label"

    #|------------------Concreate_FeedSpace Scraped Atleast_one---------------------
    Scrapped_FS_no="/html/body/div/main/div[1]/div[1]/div/div[2]/div[4]/div[2]/div[1]/label"
    Scrapped_FS_yes="/html/body/div/main/div[1]/div[1]/div/div[2]/div[4]/div[2]/div[2]/label"
    
    #|------------------Bedding Dry Free of Wet---------------------
    bedding_Dry_no="/html/body/div/main/div[1]/div[1]/div/div[2]/div[5]/div[2]/div[1]/label"
    bedding_Dry_yes="/html/body/div/main/div[1]/div[1]/div/div[2]/div[5]/div[2]/div[2]/label"
    
    #|------------------atleast 7.5 cm loose dirt in bedding area`---------------------
    looseDirt_no="/html/body/div/main/div[1]/div[1]/div/div[2]/div[6]/div[2]/div[1]/label"
    looseDirt_yes="/html/body/div/main/div[1]/div[1]/div/div[2]/div[6]/div[2]/div[2]/label"

    #|------------------Knee Drop Test---------------------
    KneeDrop_no="/html/body/div/main/div[1]/div[1]/div/div[2]/div[7]/div[2]/div[1]/label"
    KneeDrop_yes="/html/body/div/main/div[1]/div[1]/div/div[2]/div[7]/div[2]/div[2]/label"

    
    path= {
            headlock_FS_yes: "/html/body/div/main/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[2]/label",
            Scrapped_FS_yes : "/html/body/div/main/div[1]/div[1]/div/div[2]/div[4]/div[2]/div[2]/label",
            bedding_Dry_yes : "/html/body/div/main/div[1]/div[1]/div/div[2]/div[5]/div[2]/div[2]/label",
            looseDirt_yes : "/html/body/div/main/div[1]/div[1]/div/div[2]/div[6]/div[2]/div[2]/label",
            KneeDrop_yes : "/html/body/div/main/div[1]/div[1]/div/div[2]/div[7]/div[2]/div[2]/label"
            }
    def __init__(self,driver):
        self.driver = driver
        self.func = lambda : [i for i in self.path]
        [self.driver.find_element(By.XPATH, i).click() for i in self.func()]

        self.corral_area = self.driver.find_element(By.XPATH,"//input[@type='number']")
        self.corral_area.clear()
        self.corral_area.send_keys("1500")
        time.sleep(3)