class locators():

#======================ALL-TEST-DATA=====================================
#Valid - username/password data
    usernames = [
           ("abbasAdvCustomer@mailinator.com"),
           ("abbasAdmin@mailinator.com"),
           ("abbasZinPro@mailinator.com"),
           ("moiz@mailinator.com")
           ]
    passwords=["Abbas@123"]

#InValid - username/password data
    invalid_usernames = [
        ('invalid')
        ]
    invalid_passwords = [
        ("invalid")
        ]

#Forget-Pass_Email
    forget_email= ["abbasAdmin@mailinator.com"]
    
#=======================ALL-XPATH-ELEMENTS-LOCATION=====================
#Login Page-Element username/password Xpaths---
    username_xpath = "//input[@id='email']"
    password_xpath = "//input[@id='password']";
    btn_xpath= "//button[@type='submit']";
    invalid_credential_msg_xpath="//div[@role='alert']"

#Logout - linkBtn---
    logout_xpath = "//a[text() = 'Log Out']"


#forget-pass - XPATHS---
    forget_link = "//a[@class='pull-right focus reset-password-link']"
    forget_email_path = "//input[@id='username']";
    forget_submit="//button[@type='submit']";
    forget_success_msg_path = "//div[@role='alert']"


#quick-Evaluations Xpath
    eval_quick_bton_xpath = "//a[normalize-space()='Quick Start Evaluation']"


#-------------quick-Evaluation------------------------|

    values=[("imperial"),("metric")]
    measurement_path = "//input[@value='{}']";
    Next_path = "//button[@class='btn btn-primary btn-full--sm mt-4 float-right']"
    assesor_sort_path = "//button[@class='btn btn-primary btn-block--xs pull-right']"

    locomotion_checkbox = "//div[12]//div[1]//label[1]//span[1]"
    heat_abatement_checbox = "//div[@class='row checkbox-grid']//div[6]//div[1]//label[1]//span[1]"
    #Dirt_Alot_checkbox = "//div[@class='card-body card-body--group mt-4']//div[3]//div[1]//label[1]//span[1]"
    #Dirt_Alot_checkbox = "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div/div[5]/div[3]/div/label[1]/span"
    Dirt_Alot_checkbox = "/html/body/div/main/div[1]/div[1]/div/div[2]/div/div[1]/div[5]/div[3]/div/label[1]/span"
